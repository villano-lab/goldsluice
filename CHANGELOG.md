# Changelog

All notable changes to goldsluice. The format follows [Keep a Changelog](https://keepachangelog.com/), the versions follow [semantic versioning](https://semver.org/).

goldsluice was the folder `goldsluice/` of [NSDF-Data](https://github.com/villano-lab/NSDF-Data) until 2026-11-05. Its history up to then is kept in this repository, and the change of the release made there (0.1.0) is in the `CHANGELOG.md` of NSDF-Data, on the line that says `goldsluice 0.1.0`.

## [Unreleased]

## [0.1.2] - 2026-11-05

No change to the code: the package is the code of 0.1.1. This release carries the new documentation address in its metadata.

### Added

- The documentation of goldsluice (Sphinx, `docs/`): how the pieces fit, guides, and the reference read from the docstrings (the Python mirrors document the algorithms, so the Rust extension is not built), at https://villano-lab.github.io/goldsluice/. A workflow builds it with warnings as errors for every pull request that touches `docs/`, `python/` or `pyproject.toml`, and deploys it to GitHub Pages when a release reaches `main` (or when run by hand). It replaces the pages `docs/api/` that NSDF-Data built from this package. The *Documentation* link of the package on PyPI points here from 0.1.2 (the release before it keeps the old NSDF-Data address, where a page now says the documentation moved).

## [0.1.1] - 2026-11-05

The first release made from this repository. The code is the same as 0.1.0 (`git diff v0.1.0` shows no change in `src/`, `benches/` or `python/` apart from the version number); what changes is where goldsluice lives and how it is published. `pip install goldsluice` is unchanged.

### Added

- The tag `v0.1.0` (the release `goldsluice-v0.1.0` of NSDF-Data, on the same code of the kept history) and a GitHub Release for it.
- `LICENSE`, `CONTRIBUTING.md`, `AGENTS.md`, CI on Linux, Windows and macOS (rustfmt, clippy, `cargo test`, the wheel and the parity tests), and the publish workflow (`.github/workflows/publish-goldsluice.yml`, `tools/check_release.py`): a tag `vX.Y.Z` checks the three version numbers, builds a wheel for each system and a source archive, tests each wheel in a clean environment and, after the maintainer approves the `pypi` environment, uploads with a trusted publisher.

### Changed

- goldsluice is a repository of its own, `villano-lab/goldsluice`, with the history of `goldsluice/`. Its tests install goldpan from PyPI. The test of the registry example needs a folder of detector records and reads it from `GOLDSLUICE_TEST_REGISTRY` (CI checks out the `registry/` of NSDF-Data); it is skipped without it.
- The example `examples/r76-registry.dataset.toml` names the registry as `~/NSDF-Data/registry` instead of `../../registry`.

## [0.1.0] - 2026-11-04

The last release made from NSDF-Data. Ten algorithms with a Rust kernel and a Python mirror each, batch mode (`python -m goldsluice run`) with a revision-based ledger, Parquet and ROOT output, steps that build on each other, and prebuilt wheels for Linux, Windows and macOS (`cp39-abi3`). Details: the `goldsluice 0.1.0` line of NSDF-Data's CHANGELOG, release 0.11.0.
