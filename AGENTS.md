# AGENTS.md: working in goldsluice

Instructions for AI coding agents (Claude Code, Codex, Copilot, Cursor and others) and for human contributors. `CLAUDE.md` points here. The Git rules are in `CONTRIBUTING.md`; read it too.

## What this repository is

goldsluice is the reduction package of the NSDF-Data project (SuperCDMS-type detector data, Run 76): fast kernels in Rust, a Python mirror of every algorithm, and batch mode (`python -m goldsluice run`) that processes a dataset definition into Parquet or ROOT files. It was the folder `goldsluice/` of https://github.com/villano-lab/NSDF-Data until 2026-11-05.

- `src/`: the Rust kernels (the extension module `goldsluice._core`, built with maturin, `abi3-py39`). `benches/kernels.rs`: `cargo bench`.
- `python/goldsluice/`: the Python package: `algorithms.py` (the registry of algorithms), `reference/` (the Python mirror of each), `batch.py` (batch mode), `profile.py`.
- `tests/`, `examples/` (dataset definitions), `PORTING.md` (how to write an algorithm), `tools/check_release.py` (the release checker).

The kernels use nothing from goldpan. Batch mode reads datasets with [goldpan](https://github.com/villano-lab/goldpan), installed from PyPI (`pip install goldsluice[batch]`); **goldpan never imports goldsluice.** What is not here, and stays in NSDF-Data: the detector registry (`registry/`: data, to become repositories of its own), the notebooks, the guides and notes. Nothing in goldsluice may depend on them.

The maintainer is Anthony Villano (@villaa).

## Before you change anything

1. `git status` and `git log --oneline -3`. Pull first. Be on a `feature/*` branch made from an up-to-date `develop`.
2. `python -m pip install maturin pytest numpy "goldpan[parquet]>=0.3"`, `maturin develop --release`, then `cargo test` and `python -m pytest tests -q`.
3. **One working copy per session.** If `git status` shows changes you did not make, or another session may be using this folder, do not touch them: make your own worktree (`git worktree add ../goldsluice-<task> -b feature/<name> origin/develop`) and remove it when done. A running `goldsluice run` holds the compiled extension: do not rebuild it under a run.

## Rules

- Branches and merging: `CONTRIBUTING.md`. Never commit to `main` or `develop`, never force-push, merge commits only. **An agent never merges a pull request without the maintainer's explicit go-ahead, and never pushes a release tag (`vX.Y.Z`): it publishes to PyPI, which cannot be undone.**
- A line under `[Unreleased]` in `CHANGELOG.md` for any change a user would notice. Only a `release/*` or `hotfix/*` branch changes the version (three places, `CONTRIBUTING.md`).
- An algorithm: follow `PORTING.md`: write the mirror in the kernel subset, port it, register it, add the standard inputs (`cases()`), a Rust unit test and a benchmark. `cargo test`, `cargo clippy --all-targets -- -D warnings`, `cargo fmt` and `python -m pytest tests` must pass, and the pull request quotes `cargo bench` and `goldsluice.compare` timings from a `--release` build. A new algorithm has `REVISION = 1`; **a fix that changes what an existing one returns raises its `REVISION` by one in the same pull request.**
- Batch mode and the dataset definition: the definition format is specified in goldpan (`goldpan.dataset`, its docstring); a new key is raised there first (`FORMAT_VERSION`, goldpan's tests), and this repository then needs the goldpan release that has it in the `batch` extra of `pyproject.toml`.
- Processed output (the results of `python -m goldsluice run`) lives outside any repository, by default in `~/goldsluice-output/`; `GOLDSLUICE_OUTPUT` sets one folder. `.gitignore` covers `processed/` and `_goldsluice.json`, and `check` and `run` refuse an output folder inside a Git working tree that does not ignore them. Never use `--allow-output-in-repo` to commit results.
- Docstrings are read by Sphinx as reStructuredText, with single backticks shown as code: a literal block needs `::` before it, a name in backticks may not be followed by a letter (write "`Segment` objects", not "`Segment`s"), and a `|` or `*` in running text needs backticks. The documentation check (build command in `CONTRIBUTING.md`) fails a pull request that breaks it. The pages in `docs/` are hand-written; the reference is generated.
- Write commit messages that say what changed and why. If an AI assistant helped, add a `Co-Authored-By:` trailer naming it. Never commit raw data, credentials or tokens.
- Do not run a reprocessing of the maintainer's data without being asked: it takes hours and disk.
