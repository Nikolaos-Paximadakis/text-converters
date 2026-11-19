# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`text_converters` is a pure Python package (v0.1.0, installed from GitHub; not published on PyPI) for converting accented/special characters from Greek, Swedish, German, French, and Spanish to their English equivalents. Zero runtime dependencies. Supports the Python versions that are not end-of-life (currently 3.11+).

## Commands

```bash
pip install -e ".[dev]"                          # Install with dev dependencies

pytest tests/ -v                                 # Run all tests
pytest tests/ -v --cov=text_converters           # With coverage
pytest tests/test_character_converters.py::TestGreekConversion::test_basic_greek_conversion -v  # Single test

flake8 text_converters/ tests/ --max-line-length=127   # Lint (max-line-length=127, not 88)
black --check text_converters/ tests/                   # Format check
isort --check-only text_converters/ tests/              # Import sort check
mypy text_converters/                                   # Type check
```

## Architecture

Single-module package. All logic lives in `text_converters/character_converters.py`; `__init__.py` re-exports everything as the public API.

**Core pattern:** each language converter (except Greek) is a plain function that does `return "".join(MAPPING.get(c, c) for c in text)` against a static `Dict[str, str]`. All converters are collected in the `CHARACTER_CONVERTERS` dict, keyed by language name string.

The Greek converter needs context, so it walks the text by index: `ου` becomes "ou", and `Θ`/`Χ`/`Ψ` become "Th"/"Ch"/"Ps" or "TH"/"CH"/"PS" depending on whether the neighbouring letters are capitals. Its tables are module-level (`_GREEK_TO_ENGLISH` etc.). Keep it in step with the copy in the author's other package.

**Public API** (from `__init__.py`):
- `convert_greek_characters_to_english(text)`, `convert_swedish_characters_to_english(text)`, `convert_german_characters_to_english(text)`, `convert_french_characters_to_english(text)`, `convert_spanish_characters_to_english(text)`, `no_conversion(text)`
- `CHARACTER_CONVERTERS` — dict mapping language name → converter function
- `get_character_converter(language="none")` — returns the appropriate function or raises `ValueError`

## CI

`.github/workflows/ci.yml` runs three parallel jobs on push to main and on PRs. A ruleset on `main` requires a PR and the Lint and Format checks; no force-push or deletion.
1. **lint** — flake8 (max-line-length=127, max-complexity=10) on package and tests + mypy
2. **format** — black --check + isort --check-only on package and tests
3. **test** — pytest matrix across Python 3.11–3.15 (only versions that are not end-of-life)

Note: flake8 uses `--max-line-length=127`, but black is configured for line-length=88 in `pyproject.toml`. Don't introduce lines between 89–127 chars unless intentional.
