# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`text_converters` is a pure Python package (v0.2.1; first PyPI release pending, see issue #3) for converting accented/special characters from Greek, Swedish, German, French, and Spanish to their English equivalents. Zero runtime dependencies. Supports the Python versions that are not end-of-life (currently 3.11+).

## Commands

```bash
pip install -e ".[dev]"                          # Install with dev dependencies

pytest tests/ -v                                 # Run all tests
pytest tests/ -v --cov=text_converters           # With coverage
pytest tests/test_character_converters.py::TestGreekConversion::test_basic_greek_conversion -v  # Single test

ruff check .                                            # Lint (rule families in pyproject.toml)
ruff format --check .                                   # Format check (replaces black/isort)
mypy                                                    # Type check (strict, config in pyproject.toml)
pyright                                                 # Second type checker (strict)
pre-commit run --all-files                              # Whitespace, ruff, gitleaks (install once: pre-commit install)
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
1. **lint** — ruff check + mypy and pyright, both strict, on the package and the tests. The package ships `py.typed`
2. **format** — ruff format --check
3. **test** — pytest matrix across Python 3.11–3.15 (only versions that are not end-of-life)

Strict settings: pytest treats warnings as errors (`--strict-markers --strict-config`); pyright refuses bare `# type: ignore` (an ignore names its rule and gives a reason). Ruff skips Markdown and allows Greek look-alike letters (RUF001-003) in the converter module and tests; that is deliberate.

4. **package** — builds wheel and sdist, `twine check --strict`, `scripts/check_dist.py` (archive contents incl. `py.typed`; version in `pyproject.toml` == `__version__` == tag), clean install of each archive.

## Releasing

`.github/workflows/release.yml` uses Trusted Publishing: a manual run uploads to TestPyPI, a published GitHub release `vX.Y.Z` uploads to PyPI (environment `pypi`, needs approval). Bump the version in both `pyproject.toml` and `text_converters/__init__.py`, update `CHANGELOG.md`. PyPI never accepts a filename twice: never reuse or move a tag; roll back by yanking and releasing a fixed version.

**Downstream contract** (`tests/test_downstream_contract.py`): sru-generator loads converters by name via `get_character_converter` and checks the Greek probe before using this package. Changing the names, that function or the probe output is a breaking change.
