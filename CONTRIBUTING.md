# Contributing

Thanks for helping keep Country Array accurate and easy to consume.

## Data changes

`countries-array.json` is the only canonical data file. Do not duplicate country data in PHP.

For a data correction:

1. Update `countries-array.json`.
2. Keep the code as exactly two uppercase letters.
3. Use a concise English display name suitable for UI.
4. Add or update `CHANGELOG.md` for user-visible naming changes.
5. Run `python scripts/validate.py`.

If a proposed code is not an officially assigned ISO 3166-1 alpha-2 code, explain why it belongs in the compatibility set and cite a stable upstream reference such as Unicode CLDR.

## Code changes

Keep the project dependency-free unless a dependency is clearly justified. Preserve these compatibility guarantees:

- `countries-array.json` remains valid UTF-8 JSON.
- `require 'countries-array.php'` returns an associative array without printing output.
- `php countries-array.php` prints the canonical dataset as JSON.
- PHP and JSON expose exactly the same keys and values.

## Pull requests

Keep pull requests focused. Include:

- what changed
- why it changed
- any upstream source used for data corrections
- validation results

GitHub Actions must pass before merge.
