# How the pieces fit

## The pieces

| Piece | What it is | Where |
|---|---|---|
| Kernel | A fast per-trace algorithm in Rust (`src/`), built into the extension module `goldsluice._core`. | the Rust source, `cargo doc` |
| Mirror | The same algorithm in Python, written in a small subset of the language so that the port is mechanical. It is the readable definition and the place to develop. | {py:mod}`goldsluice.reference` |
| Algorithm registry | The algorithms by name, with their parameters, their outputs and their `REVISION`; `run` runs one on either backend and `compare` times both. | {py:mod}`goldsluice.algorithms` |
| Batch mode | `python -m goldsluice run`: reads each raw file in chunks, runs the steps of a dataset definition and writes the quantities into a Parquet (or ROOT) dataset, with a ledger that redoes only what is new or whose algorithm or reader changed. | {py:mod}`goldsluice.batch` |
| Dataset definition | One TOML file naming the raw files, how to read them and the processing to run. It is specified and read by [goldpan](https://villano-lab.github.io/goldpan/), which also reads the processed output back. | goldpan's `goldpan.dataset` |

## The flow

```text
raw files --adapter (goldpan)--> pulses --kernels (Rust)--> quantities --Parquet dataset--> goldpan.dataset.Dataset
```

goldsluice's batch mode imports goldpan, which does the reading and the definition file; goldpan never imports goldsluice, and the kernels use nothing from goldpan.

## Principles

- **A quantity has one definition.** Every algorithm has a Rust kernel and a Python mirror; a test requires that they agree on the standard inputs and refuse bad parameters with the same message, and that they agree with the goldpan function of the same quantity (or say why there is none).
- **The readout is never assumed.** `amps_per_adc`, `glitch_samples`, `pretrigger_samples` and every other parameter have no defaults; in a dataset definition, `"@readout.pretrigger_samples"` takes a value from the readout so that the file cannot disagree with itself.
- **Provenance travels with the data.** A processed file carries the steps, parameters, versions and timing that produced it.
- **A fix that changes a result raises the algorithm's `REVISION`**, so `goldsluice run` redoes only the outputs made with the old one.
