# Changelog

All notable changes to this project are documented in this file. The project follows
[Semantic Versioning](https://semver.org/); while the version is 0.x, a minor release
may contain breaking changes, which are listed here.

## [0.2.1] - 2026-11-22

First release on PyPI (`pip install text-converters`). No change to the converters.

### Added
- Release workflow with Trusted Publishing: a manual run uploads to TestPyPI, a GitHub
  release `vX.Y.Z` uploads to PyPI.
- CI checks the built wheel and sdist (contents, versions, a clean install of each).
- Tests that pin what downstream packages rely on: `get_character_converter`, the
  converter names and the Greek output `Θεσσαλονίκη Παπαδόπουλος` →
  `Thessaloniki Papadopoulos`.

### Changed
- Tooling: ruff replaces flake8, black and isort; pytest, mypy and pyright run in strict
  mode on the package and the tests; pre-commit hooks; CI actions pinned to commit SHAs.

## [0.2.0] - 2026-11-19

### Added
- The package ships `py.typed`, so type checkers use its annotations.

### Changed
- French converter writes `œ`/`æ` as `oe`/`ae` (`Œuvre` → `Oeuvre`); they were left
  unchanged.

## [0.1.0] - 2026-11-19

First release: Greek, Swedish, German, French and Spanish converters. The Greek converter
is close to ELOT 743 letter by letter (`η` → `i`, `ου` → `ou`, `Θ`/`Χ`/`Ψ` → `Th`/`Ch`/`Ps`).

[0.2.1]: https://github.com/Nikolaos-Paximadakis/text-converters/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Nikolaos-Paximadakis/text-converters/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Nikolaos-Paximadakis/text-converters/releases/tag/v0.1.0
