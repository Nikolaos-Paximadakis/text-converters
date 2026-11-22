# Text Converters

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange.svg)](https://github.com/Nikolaos-Paximadakis/text-converters)

Small, dependency-free Python functions that replace Greek letters and accented
Swedish, German, French and Spanish letters with plain Latin (mostly ASCII)
equivalents, using one fixed character map per language.

## Scope and limitations

Released under the MIT License and provided "as is", without warranty of any kind.
Each converter is a simple character-by-character lookup. Known limits:

- **Greek** is close to ELOT 743 for single letters, but it is not a full
  implementation of ELOT 743 or ISO 843. `η` → `i` (`Θεσσαλονίκη` → `Thessaloniki`),
  `ου` → `ou` (`Παπαδόπουλος` → `Papadopoulos`), and `Θ`, `Χ`, `Ψ` give `Th`, `Ch`,
  `Ps`, or `TH`, `CH`, `PS` inside an all-capitals word (`ΑΘΗΝΑ` → `ATHINA`).
- Other Greek letter pairs that ELOT 743 treats specially (`αυ`, `ευ`, `μπ`, `ντ`,
  `γγ`, ...) are converted letter by letter (`Ευρώ` → `Eyro`, `Μπαμπάς` → `Mpampas`).
- **German** writes umlauts as `ae`/`oe`/`ue` and `ß` as `ss`. The other converters
  simply drop the accent (Swedish `ä` → `a`).
- **French** writes the ligatures `œ` and `æ` as `oe` and `ae`; like the German
  umlauts, their capitals become `Oe` and `Ae` even in an all-capitals word.
- Characters missing from a language's map are returned unchanged, so the output is
  not guaranteed to be ASCII (for example `¿`, `€` or Cyrillic letters).
- Conversion is one-way and loses information.

## Installation

The package is not published on PyPI. Install it from GitHub:

```bash
pip install git+https://github.com/Nikolaos-Paximadakis/text-converters.git
```

For development:

```bash
git clone https://github.com/Nikolaos-Paximadakis/text-converters.git
cd text-converters
pip install -e ".[dev]"
```

## Usage

### Basic Usage

```python
from text_converters import convert_greek_characters_to_english

# Convert Greek text to English
greek_text = "Αθήνα"
english_text = convert_greek_characters_to_english(greek_text)
print(english_text)  # Output: "Athina"
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
german_result = convert_german_characters_to_english("Grüße")  # "Gruesse"

# French
french_result = convert_french_characters_to_english("Bonjour")  # "Bonjour"
```

## Supported Languages

| Language | Function | Example |
|----------|----------|---------|
| Greek | `convert_greek_characters_to_english` | "Αθήνα" → "Athina" |
| Swedish | `convert_swedish_characters_to_english` | "Göteborg" → "Goteborg" |
| German | `convert_german_characters_to_english` | "Grüße" → "Gruesse" |
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

### Lint, Format and Type Checks

```bash
ruff check .
ruff format --check .
mypy
pyright
```

## License

MIT License. See [LICENSE](LICENSE).

## Contributing

When adding new language converters:

1. Add the conversion function following the existing pattern
2. Add the function to the `CHARACTER_CONVERTERS` dictionary
3. Update the `__all__` list in `__init__.py`
4. Add tests for the new converter
5. Update this README with examples

## Version History

- **0.2.0**: French `œ`/`æ` become `oe`/`ae`; the package ships `py.typed`.
- **0.1.0**: First release: Greek, Swedish, German, French and Spanish converters.
