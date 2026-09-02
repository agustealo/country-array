# Data policy

`countries-array.json` is the canonical dataset for this repository. The PHP adapter reads it at runtime so both formats stay synchronized.

## Intended use

The data is optimized for country/region selectors, forms, lightweight application lookups, and general user-interface display.

Each entry has this shape:

```json
{
  "US": "United States"
}
```

Keys are uppercase two-letter region codes. Values are concise English display names.

## Naming policy

Use current, recognizable English names appropriate for application UI rather than long-form constitutional names.

Examples maintained by validation:

- `CZ`: Czechia
- `MK`: North Macedonia
- `SZ`: Eswatini
- `TR`: Türkiye

Names should remain stable unless there is a clear modern naming change or a correction.

## Code policy

Most keys correspond to ISO 3166-1 alpha-2 country and territory codes. The project also retains several two-letter compatibility codes commonly represented in Unicode CLDR territory data:

| Code | Display name | Note |
| --- | --- | --- |
| `AC` | Ascension Island | CLDR territory code |
| `CP` | Clipperton Island | CLDR territory code |
| `DG` | Diego Garcia | CLDR territory code |
| `EA` | Ceuta and Melilla | CLDR territory code |
| `IC` | Canary Islands | CLDR territory code |
| `TA` | Tristan da Cunha | CLDR territory code |
| `XK` | Kosovo | Widely used user-assigned/CLDR territory code |

This means the dataset is deliberately broader than a strict ISO-only list. Consumers that require ISO-only validation should filter against an authoritative ISO 3166-1 source before accepting a code.

## References

Useful upstream references when reviewing data changes:

- ISO 3166 country codes: https://www.iso.org/iso-3166-country-codes.html
- Unicode CLDR territory information: https://unicode.org/cldr/charts/latest/supplemental/territory_information.html
- Unicode CLDR country/region naming guidance: https://cldr.unicode.org/translation/displaynames/countryregion-territory-names

The presence of a reference here does not imply that this repository republishes an official ISO dataset.

## Updating data

1. Edit `countries-array.json` only.
2. Keep keys uppercase and two characters long.
3. Keep display names non-empty and suitable for UI use.
4. Run `python scripts/validate.py`.
5. Update `CHANGELOG.md` when a user-visible name or compatibility policy changes.

Do not manually duplicate the data inside `countries-array.php`; it is intentionally an adapter around the JSON source.
