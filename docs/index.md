# goldsluice

The reduction package of the NSDF-Data project: fast pulse-reduction kernels in Rust, each with a **Python mirror** that is its readable definition, and a batch mode (`python -m goldsluice run`) that runs a whole dataset and writes the quantities as Parquet or ROOT files. Its companion for analysis is [goldpan](https://villano-lab.github.io/goldpan/), which reads the dataset definition and the processed output.

Install it with `pip install goldsluice` (a wheel for Windows, macOS and Linux; no Rust needed), with `goldsluice[batch]` for batch mode and `goldsluice[root]` for ROOT output. The code is at <https://github.com/villano-lab/goldsluice>.

Nothing about a readout is assumed: the sample period, the baseline window and every algorithm parameter are written down by the user, in code or in the dataset definition file.

```{toctree}
:maxdepth: 2
:hidden:

concepts
guides
reference/index
```

## Where to start

| You want to | Read |
|---|---|
| understand how the pieces fit | {doc}`concepts` |
| run goldsluice, define a dataset, write an algorithm | {doc}`guides` |
| look up an algorithm, function or module | {doc}`reference/index` |

This documentation is generated from the code and the pages in `docs/` of the repository. The project front page, the student guides and the notes are at <https://villano-lab.github.io/NSDF-Data/>.
