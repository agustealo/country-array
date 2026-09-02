#!/usr/bin/env python3
"""Validate the country-array data contract and PHP adapter."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "countries-array.json"
PHP_PATH = ROOT / "countries-array.php"
CODE_PATTERN = re.compile(r"^[A-Z]{2}$")
MODERN_NAMES = {
    "CZ": "Czechia",
    "MK": "North Macedonia",
    "SZ": "Eswatini",
    "TR": "Türkiye",
}
CLDR_COMPATIBILITY_CODES = {"AC", "CP", "DG", "EA", "IC", "TA", "XK"}


class DuplicateKeyError(ValueError):
    pass


def object_without_duplicates(pairs: list[tuple[str, str]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json() -> dict[str, str]:
    with JSON_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle, object_pairs_hook=object_without_duplicates)

    if not isinstance(data, dict):
        raise ValueError("countries-array.json must contain a JSON object")
    return data


def validate_data(data: dict[str, str]) -> None:
    if len(data) < 240:
        raise ValueError(f"unexpectedly small dataset: {len(data)} entries")

    for code, name in data.items():
        if not CODE_PATTERN.fullmatch(code):
            raise ValueError(f"invalid region code: {code!r}")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"invalid display name for {code}: {name!r}")

    for code, expected in MODERN_NAMES.items():
        actual = data.get(code)
        if actual != expected:
            raise ValueError(f"{code} must be {expected!r}, got {actual!r}")

    missing_compat = CLDR_COMPATIBILITY_CODES.difference(data)
    if missing_compat:
        raise ValueError(
            "missing documented compatibility codes: "
            + ", ".join(sorted(missing_compat))
        )


def run_php_checks(data: dict[str, str]) -> None:
    php = shutil.which("php")
    if php is None:
        raise RuntimeError("php is required to validate countries-array.php")

    subprocess.run([php, "-l", str(PHP_PATH)], cwd=ROOT, check=True)

    require_code = (
        "$countries = require 'countries-array.php'; "
        "echo json_encode($countries, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);"
    )
    required = subprocess.run(
        [php, "-r", require_code],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    required_data = json.loads(required.stdout)
    if required_data != data:
        raise ValueError("PHP require result does not exactly match countries-array.json")

    direct = subprocess.run(
        [php, str(PHP_PATH)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    direct_data = json.loads(direct.stdout)
    if direct_data != data:
        raise ValueError("direct PHP JSON output does not exactly match countries-array.json")


def main() -> int:
    try:
        data = load_json()
        validate_data(data)
        run_php_checks(data)
    except (DuplicateKeyError, OSError, RuntimeError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"validation passed: {len(data)} country/territory entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
