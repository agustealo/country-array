<?php

declare(strict_types=1);

/**
 * Country and territory names keyed by two-letter region code.
 *
 * The JSON file is the canonical source so PHP and JSON consumers stay in sync.
 * Requiring this file returns the associative array without producing output.
 * Executing this file directly prints the dataset as UTF-8 JSON.
 *
 * @return array<string, string>
 */
function country_array_load(): array
{
    $path = __DIR__ . '/countries-array.json';
    $json = file_get_contents($path);

    if ($json === false) {
        throw new RuntimeException('Unable to read countries-array.json.');
    }

    $countries = json_decode($json, true, 512, JSON_THROW_ON_ERROR);

    if (!is_array($countries)) {
        throw new RuntimeException('countries-array.json must decode to an object.');
    }

    return $countries;
}

$countries = country_array_load();

$scriptFilename = $_SERVER['SCRIPT_FILENAME'] ?? null;
$isDirectExecution = is_string($scriptFilename)
    && realpath($scriptFilename) === __FILE__;

if ($isDirectExecution) {
    if (!headers_sent()) {
        header('Content-Type: application/json; charset=utf-8');
    }

    echo json_encode(
        $countries,
        JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR
    );
}

return $countries;
