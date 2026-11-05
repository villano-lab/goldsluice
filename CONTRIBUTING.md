# Working on goldsluice

goldsluice uses **Git Flow** and **semantic versioning**, as goldpan, goldmap and NSDF-Data do. `AGENTS.md` has the rules for AI coding agents, which are the same rules.

## Branches

| Branch | What it is |
|---|---|
| `main` | Released code only. Every commit on it is tagged `vX.Y.Z`. |
| `develop` | The integration branch. All work lands here first. |
| `feature/<name>` | One change, made from `develop`, finished by a pull request into `develop`. |
| `release/X.Y.Z` | Made from `develop` to get a release ready (the three version numbers, `CHANGELOG.md`, last fixes). Finished by a pull request into `main`. |
| `hotfix/X.Y.Z` | An urgent fix made from `main`. Finished by a pull request into `main`, then merged back into `develop`. |

Rules:

- Never commit directly to `main` or `develop`. Make a branch and open a pull request.
- Finish a branch with a **merge commit** (not squash, not rebase). Never force-push.
- Delete a branch only after it is merged, and only one you made.
- A change a user would notice gets a line under `[Unreleased]` in `CHANGELOG.md`.
- Only a `release/*` or `hotfix/*` branch changes the version or renames `[Unreleased]`. The version is written in **three places** that must agree: `Cargo.toml`, `pyproject.toml` and `__version__` in `python/goldsluice/__init__.py` (`tests/test_version.py` checks it; `Cargo.lock` follows `Cargo.toml` when you build).
- The tests run on Linux, Windows and macOS for every pull request: `cargo fmt --check`, `cargo clippy --all-targets -- -D warnings`, `cargo test`, then the wheel built with maturin and `python -m pytest tests`. All must pass.

## Building and testing on your computer

```
python -m pip install maturin pytest numpy "goldpan[parquet]>=0.3"
maturin develop --release                    # builds the extension into the active environment (a running processing keeps the old one: stop it first)
cargo test && python -m pytest tests -q
```

One test needs a folder of detector records (the registry): set `GOLDSLUICE_TEST_REGISTRY` to the `registry/` folder of a clone of NSDF-Data, or it is skipped.

## A feature

```
git switch develop && git pull
git switch -c feature/<name>
# ... work, commit ...
git push -u origin feature/<name>
# open a pull request into develop
```

A new algorithm follows **`PORTING.md`**: the Python mirror first, then the Rust kernel, then register both, with the standard inputs, a Rust unit test and a benchmark. A fix that changes what an existing algorithm returns raises its `REVISION` by one in the same pull request (`goldsluice run` then redoes only the outputs made with it).

## A release

```
git switch develop && git pull
git switch -c release/X.Y.Z
# set the version in the three places, rename [Unreleased] in CHANGELOG.md to [X.Y.Z] - date
# open a pull request into main; when it is merged:
git tag vX.Y.Z <the merge commit on main> && git push origin vX.Y.Z
# merge main back into develop (a pull request)
```

## Publishing to PyPI

goldsluice is published as `goldsluice` (https://pypi.org/project/goldsluice/) by `.github/workflows/publish-goldsluice.yml`. It is a Rust extension, so the upload holds a wheel for each system (`cp39-abi3`: one wheel per system serves every Python from 3.9) and the source archive. The workflow runs when a tag `vX.Y.Z` is pushed: it checks that the tag, the three version numbers and the changelog agree (`python tools/check_release.py vX.Y.Z` does the same on your computer) and that the tag is on `main`, builds the wheels and the source archive, installs each wheel in a clean environment and runs the tests there, and then uploads. No token is stored anywhere: PyPI trusts the workflow (a "trusted publisher"), and the upload waits for the maintainer to approve the `pypi` environment. Run by hand (Actions, *Publish goldsluice*, *Run workflow*) it is a dry run that never uploads.

One-time setup (maintainer): GitHub, *Settings*, *Environments*, new environment `pypi`, *Required reviewers* yourself, and under *Deployment branches and tags* allow only tags matching `v*`. PyPI, project `goldsluice`, *Manage*, *Publishing*, *Add a new publisher*, GitHub: owner `villano-lab`, repository `goldsluice`, workflow `publish-goldsluice.yml`, environment `pypi`. The publisher that names the NSDF-Data repository should be removed once this one works. A version on PyPI can never be replaced, so run the dry run first. **An AI agent never pushes a release tag.**
