# Guides

Step-by-step pages for running goldsluice and for writing an algorithm.

```{toctree}
:maxdepth: 1

guides/batch
guides/algorithm
```

## Running goldsluice

- {doc}`guides/batch`: the dataset definition file, `check` and `run`, reading the result with goldpan.
- {doc}`guides/algorithm`: setup (Rust), running and timing, and the path of a new algorithm from the Python mirror to the Rust kernel.

## Writing an algorithm

- [`PORTING.md`](https://github.com/villano-lab/goldsluice/blob/develop/PORTING.md): the rules the Python mirror must follow so that the port is mechanical, a table of the equivalent Python and Rust, and a checklist.

## Writing an adapter for goldpan

- [Writing an adapter](https://villano-lab.github.io/goldpan/guides/writing-an-adapter.html), in the goldpan documentation: so that goldpan reads another file format, which batch mode then uses.

## Working on goldsluice

- [`CONTRIBUTING.md`](https://github.com/villano-lab/goldsluice/blob/develop/CONTRIBUTING.md): Git Flow, building with maturin, tests, releases. [`AGENTS.md`](https://github.com/villano-lab/goldsluice/blob/develop/AGENTS.md) has the rules for AI coding agents.
- [The changelog](https://github.com/villano-lab/goldsluice/blob/main/CHANGELOG.md).
- [Student guides and notes](https://villano-lab.github.io/NSDF-Data/) of the NSDF-Data project.
