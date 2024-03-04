# Country Array Repository

Welcome to the Country Array Repository! This repository contains essential data about countries worldwide in two formats: PHP and JSON.

## Files

### country-array.php

This PHP file stores an array of countries, each identified by a two-letter country code and its corresponding name. 

### country-array.json

The JSON file presents the same list of countries as the PHP file, providing a structured format for easy integration into various applications.

## Usage

1. **Clone or Download:** Start by cloning or downloading this repository to access the country data files.

2. **Integrate into Your Project:** Include the `country-array.php` file in your PHP projects, or utilize the `country-array.json` file in any programming language or application.

3. **Retrieve Country Data:** Use the provided country data to retrieve country names and their corresponding codes as needed in your projects.

## Example

```php
<?php

// Original array of countries
$countries = array(
    "AF" => "Afghanistan (‫افغانستان‬‎)",
    "AX" => "Åland Islands (Åland)",
    "AL" => "Albania (Shqipëri)",
    // Add more countries here...
    "ZW" => "Zimbabwe"
);

// Convert array to JSON
$countries_json = json_encode($countries, JSON_PRETTY_PRINT);

// Display updated list
echo $countries_json;

?>
```

## Contributing

Contributions to this repository are highly encouraged! If you notice any errors, wish to add more countries, or have suggestions for improvements, please feel free to open an issue or create a pull request.

## Change Log

- **v0.01 (01-02-15):** Initial release.
- **v0.02 (04-04-23):**
  - Added the change log section.
  - Improved code structure and readability.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
