# Country Array

A small, dependency-free country and territory dataset for applications that need a simple two-letter region-code lookup.

The repository exposes the same canonical data in JSON and PHP:

- `countries-array.json` — canonical UTF-8 data source.
- `countries-array.php` — PHP adapter that returns the JSON dataset as an associative array.

## Quick start

### JSON

```js
import countries from './countries-array.json' with { type: 'json' };

console.log(countries.US); // United States
console.log(countries.TR); // Türkiye
```

Or load the file in any environment that can parse JSON.

### PHP

```php
<?php

$countries = require __DIR__ . '/countries-array.php';

echo $countries['US']; // United States
```

Requiring the PHP file is side-effect free: it returns the array and does not print output.

Running the file directly prints the canonical dataset as JSON:

```bash
php countries-array.php
```

## Data contract

Each entry is a two-letter uppercase region code mapped to a non-empty English display name.

The collection is designed for country/region selectors and general application UI. It is primarily based on ISO-style country codes, while retaining a small set of Unicode CLDR compatibility territory codes that have historically been part of this project, including `AC`, `CP`, `DG`, `EA`, `IC`, `TA`, and `XK`.

Because of those compatibility entries, consumers **must not assume every key is an officially assigned ISO 3166-1 alpha-2 code**.

See [docs/DATA.md](docs/DATA.md) for naming policy, compatibility codes, and maintenance rules.

## Current naming

The dataset uses modern user-facing English names where appropriate, including:

- `CZ` → Czechia
- `MK` → North Macedonia
- `SZ` → Eswatini
- `TR` → Türkiye

## Validation

Run the repository validator:

```bash
python scripts/validate.py
```

It checks:

- valid UTF-8 JSON
- duplicate-free two-letter uppercase keys
- non-empty names
- expected modern names
- PHP syntax
- silent PHP inclusion
- exact PHP/JSON data parity
- direct PHP JSON output

GitHub Actions runs the same validation for pushes and pull requests.

## Repository layout

```text
countries-array.json      Canonical dataset
countries-array.php       PHP adapter
scripts/validate.py       Data and PHP validation
docs/DATA.md              Data policy and compatibility notes
CONTRIBUTING.md            Contribution workflow
CHANGELOG.md               Release history
LICENSE                    MIT license
```

## Contributing

Corrections and additions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Data changes should update the canonical JSON file; the PHP adapter reads that file automatically.

## License

MIT. See [LICENSE](LICENSE).
