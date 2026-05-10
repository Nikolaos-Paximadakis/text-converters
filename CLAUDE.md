# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`text_converters` is a pure Python PyPI package (v1.0.0) for converting accented/special characters from Greek, Swedish, German, French, and Spanish to their English equivalents. Zero runtime dependencies, Python 3.8+ compatible.

## Commands

```bash
pip install -e ".[dev]"                          # Install with dev dependencies

pytest tests/ -v                                 # Run all tests
pytest tests/ -v --cov=text_converters           # With coverage
pytest tests/test_character_converters.py::TestGreekConversion::test_basic_greek_conversion -v  # Single test

flake8 text_converters/ --max-line-length=127    # Lint (max-line-length=127, not 88)
black --check text_converters/                   # Format check
isort --check-only text_converters/              # Import sort check
mypy text_converters/ --ignore-missing-imports   # Type check
```

## Architecture

Single-module package. All logic lives in `text_converters/character_converters.py`; `__init__.py` re-exports everything as the public API.

**Core pattern:** each language converter is a plain function that does `return "".join(MAPPING.get(c, c) for c in text)` against a static `Dict[str, str]`. All converters are collected in the `CHARACTER_CONVERTERS` dict, keyed by language name string.

**Public API** (from `__init__.py`):
- `convert_greek_characters_to_english(text)`, `convert_swedish_characters_to_english(text)`, `convert_german_characters_to_english(text)`, `convert_french_characters_to_english(text)`, `convert_spanish_characters_to_english(text)`, `no_conversion(text)`
- `CHARACTER_CONVERTERS` — dict mapping language name → converter function
- `get_character_converter(language="none")` — returns the appropriate function or raises `ValueError`

## CI

`.github/workflows/ci.yml` runs three parallel jobs on push/PR:
1. **lint** — flake8 (two passes: strict errors, then warnings with max-line-length=127) + mypy
2. **format** — black --check + isort --check-only
3. **test** — pytest matrix across Python 3.8–3.12 with Codecov upload

Note: flake8 uses `--max-line-length=127`, but black is configured for line-length=88 in `pyproject.toml`. Don't introduce lines between 89–127 chars unless intentional.
