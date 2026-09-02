# Changelog

All notable changes to Country Array are documented here.

## 1.0.0 - 2026-09-02

### Changed

- Made `countries-array.json` the canonical data source.
- Reworked `countries-array.php` into a side-effect-free PHP adapter that returns the canonical array when required and emits JSON only when executed directly.
- Updated current display names for Czechia, North Macedonia, Eswatini, and Türkiye.
- Rewrote the README with current JSON and PHP usage examples.

### Added

- Automated dataset and PHP parity validation.
- GitHub Actions validation for pushes and pull requests.
- Data policy documentation, including the retained Unicode CLDR compatibility codes.
- Contribution guidelines.
- MIT license file matching the repository's documented license.

## 0.2.0 - 2024-03-04

- Added JSON output.
- Updated the PHP file to emit JSON.
- Improved README structure and usage documentation.

## 0.1.0 - 2015-01-02

- Initial country array release.
