"""The example definition that shows every algorithm (`examples/r76-registry.dataset.toml`) keeps showing every algorithm."""
import os
from pathlib import Path

import numpy as np
import pytest

dataset = pytest.importorskip("goldpan.dataset")

from goldsluice.algorithms import ALGORITHMS, kind, run

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "r76-registry.dataset.toml"
REGISTRY = os.environ.get("GOLDSLUICE_TEST_REGISTRY")     # a folder of detector records: the `registry/` of NSDF-Data until the registry has its own repository


@pytest.fixture
def example(tmp_path):
    """The registry example, copied next to its metadata with the registry line pointing at GOLDSLUICE_TEST_REGISTRY."""
    if not REGISTRY or not Path(REGISTRY).is_dir():
        pytest.skip("GOLDSLUICE_TEST_REGISTRY is not set to a folder of detector records (the registry/ of NSDF-Data)")
    text = EXAMPLE.read_text(encoding="utf-8")
    line = 'registry = ["~/NSDF-Data/registry"]'
    assert line in text, "the registry line of the example changed: update this fixture"
    (tmp_path / "r76.series.csv").write_text((EXAMPLE.parent / "r76.series.csv").read_text(encoding="utf-8"), encoding="utf-8")
    path = tmp_path / EXAMPLE.name
    path.write_text(text.replace(line, f'registry = ["{Path(REGISTRY).resolve().as_posix()}"]'), encoding="utf-8")
    return path


def test_the_registry_example_uses_every_algorithm_and_every_step_runs_with_its_parameters(example):
    spec = dataset.load(example)
    assert sorted({s.algorithm for s in spec.steps}) == sorted(ALGORITHMS), \
        "examples/r76-registry.dataset.toml must have a step for every algorithm of goldsluice (add the new one)"
    rng = np.random.default_rng(0)
    traces = rng.normal(3000.0, 5.0, size=(4, 4096))
    traces[:, 600:900] += 800.0                                          # a pulse after the pretrigger window
    config = spec.sources[0].readout                                     # from the registry: the readout of the detector
    for step in spec.steps:
        out = run(step.algorithm, traces, **step.resolve(config))
        assert list(out) == list(ALGORITHMS[step.algorithm].OUTPUTS)


def test_no_two_steps_of_the_registry_example_write_the_same_quantity(example):
    spec = dataset.load(example)
    names = [name + s.suffix for s in spec.steps if kind(s.algorithm) == "quantities" for name in ALGORITHMS[s.algorithm].OUTPUTS]    # a transform writes none
    assert len(names) == len(set(names)), f"two steps give the same quantity: {names}"


def test_the_steps_of_the_registry_example_that_build_on_each_other_run_in_order_on_the_traces_they_name(example):
    spec = dataset.load(example)
    rng = np.random.default_rng(1)
    raw = rng.normal(3000.0, 5.0, size=(4, 4096))
    raw[:, 500:900] += 800.0
    config = spec.sources[0].readout
    traces = {}
    for step in spec.steps:
        data = raw if step.input is None else traces[step.input]                  # the trace of the step it names
        out = run(step.algorithm, data, **step.resolve(config))
        if kind(step.algorithm) == "trace":
            assert step.name and out["trace"].shape == raw.shape
            traces[step.name] = out["trace"]
        else:
            assert all(np.isfinite(v).all() for v in out.values()) or step.algorithm.startswith("rise")
    assert set(traces) == {"lp", "flat"}
