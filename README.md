# Text Converters

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educational Use](https://img.shields.io/badge/Use-Educational%20Only-red.svg)](https://github.com/Nikolaos-Paximadakis/text-converters)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange.svg)](https://github.com/Nikolaos-Paximadakis/text-converters)

A shared Python package for character conversion utilities across multiple languages. This package provides functions to convert characters from various languages to English equivalents.

## ⚠️ Important Disclaimer

**This software is provided for EDUCATIONAL and RESEARCH purposes only.** It is NOT intended for use in critical applications without proper verification and professional review.

### Text Conversion Notice
- The accuracy of character conversions depends entirely on the provided mapping tables
- Users are solely responsible for verifying all conversions and ensuring they meet their requirements
- The authors make no representations about the accuracy or completeness of character mappings
- **Users should verify all conversions independently before using in production**

### No Warranty for Conversion Accuracy
- The software is provided "AS IS" without any warranty regarding conversion accuracy
- The authors disclaim all responsibility for any errors, omissions, or inaccuracies in character conversions
- Users assume all risks and responsibilities for their use of converted text

**By using this software, you acknowledge that you have read and understood these disclaimers.**

## Features

- **Greek to English conversion**: Convert Greek characters (including accented characters) to English equivalents
- **Swedish to English conversion**: Convert Swedish characters to English equivalents
- **German to English conversion**: Convert German characters to English equivalents
- **French to English conversion**: Convert French characters to English equivalents
- **Spanish to English conversion**: Convert Spanish characters to English equivalents
- **Extensible design**: Easy to add new language converters
- **Type hints**: Full type annotation support
- **No dependencies**: Pure Python with no external dependencies

## Installation

### Local Development Installation

Since this is a shared package for local development, install it in development mode:

```bash
cd E:\Python\text_converters
pip install -e .
```

### From Source

```bash
git clone <repository-url>
cd text_converters
pip install -e .
```

## Usage

### Basic Usage

```python
from text_converters import convert_greek_characters_to_english

# Convert Greek text to English
greek_text = "Αθήνα"
english_text = convert_greek_characters_to_english(greek_text)
print(english_text)  # Output: "Athena"
```

### Using the Character Converter Dictionary

```python
from text_converters import CHARACTER_CONVERTERS

# Get a specific converter
greek_converter = CHARACTER_CONVERTERS["greek"]
result = greek_converter("Γεια σας")  # "Geia sas"

# Available converters
print(CHARACTER_CONVERTERS.keys())
# dict_keys(['greek', 'swedish', 'german', 'french', 'spanish', 'none'])
```

### Using the Getter Function

```python
from text_converters import get_character_converter

# Get a converter by language name
converter = get_character_converter("greek")
result = converter("Καλησπέρα")  # "Kalispera"

# Handle unsupported languages
try:
    converter = get_character_converter("unsupported")
except ValueError as e:
    print(e)  # "Unsupported language 'unsupported'. Available: greek, swedish, german, french, spanish, none"
```

### Multiple Language Support

```python
from text_converters import (
    convert_greek_characters_to_english,
    convert_german_characters_to_english,
    convert_french_characters_to_english,
)

# Greek
greek_result = convert_greek_characters_to_english("Γεια σας")  # "Geia sas"

# German
german_result = convert_german_characters_to_english("Grüße")  # "GrUesse"

# French
french_result = convert_french_characters_to_english("Bonjour")  # "Bonjour"
```

## Supported Languages

| Language | Function | Example |
|----------|----------|---------|
| Greek | `convert_greek_characters_to_english` | "Αθήνα" → "Athena" |
| Swedish | `convert_swedish_characters_to_english` | "Göteborg" → "Goteborg" |
| German | `convert_german_characters_to_english` | "Grüße" → "GrUesse" |
| French | `convert_french_characters_to_english` | "Café" → "Cafe" |
| Spanish | `convert_spanish_characters_to_english` | "España" → "Espana" |
| None | `no_conversion` | "Hello" → "Hello" |

## API Reference

### Functions

#### `convert_greek_characters_to_english(text: str) -> str`
Convert Greek characters to English equivalents.

**Parameters:**
- `text` (str): Text containing Greek characters

**Returns:**
- `str`: Text with Greek characters converted to English equivalents

#### `get_character_converter(language: str = "none")`
Get a character converter function by language name.

**Parameters:**
- `language` (str): Language name ('greek', 'swedish', 'german', 'french', 'spanish', 'none')

**Returns:**
- Function: Character converter function

**Raises:**
- `ValueError`: If language is not supported

### Constants

#### `CHARACTER_CONVERTERS`
Dictionary mapping language names to their respective converter functions.

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest
```

### Code Formatting

```bash
black text_converters/
```

### Type Checking

```bash
mypy text_converters/
```

## License

MIT License

## Contributing

This package is designed to be shared between the SRU Generator and Mihalis projects. When adding new language converters:

1. Add the conversion function following the existing pattern
2. Add the function to the `CHARACTER_CONVERTERS` dictionary
3. Update the `__all__` list in `__init__.py`
4. Add tests for the new converter
5. Update this README with examples

## Version History

- **1.0.0**: Initial release with Greek, Swedish, German, French, and Spanish converters


