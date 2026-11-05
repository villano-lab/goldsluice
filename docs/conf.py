"""Sphinx configuration of the documentation of goldsluice (https://villano-lab.github.io/goldsluice/).

Build it from the repository folder::

    python -m pip install -r docs/requirements.txt
    python -m pip install "goldpan[parquet]>=0.3"
    python -m sphinx -b html -W --keep-going docs docs/_build/html

`-W` makes a warning (a broken reference, a docstring Sphinx cannot read) an error, as the pull-request check does. The Rust extension
is not needed: the reference documents the Python package, and the Python mirror of each algorithm is the readable definition of the
kernel (`autodoc_mock_imports`).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "python"))           # the Python package, even when the wheel is not installed

project = "goldsluice"
author = "goldsluice authors"
copyright = "the goldsluice authors"
language = "en"

extensions = [
    "myst_parser",             # the pages are Markdown
    "sphinx.ext.autodoc",      # the reference is read from the docstrings
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",     # accepts NumPy / Google style sections if a docstring uses them
    "sphinx.ext.intersphinx",  # links into numpy, Python
    "sphinx.ext.viewcode",
    "sphinx_copybutton",       # a copy button on every code block
]

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
exclude_patterns = ["_build", "requirements.txt"]
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3
myst_all_links_external = True                           # the pages link to other sites, not to Sphinx documents

# The docstrings put names in single backticks: show them as code, not as emphasis.
default_role = "code"

autosummary_generate = True
autodoc_default_options = {"members": True, "undoc-members": False, "show-inheritance": True}
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_mock_imports = ["goldsluice._core"]               # the Rust extension: not needed to read the docstrings
napoleon_use_param = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}
intersphinx_timeout = 10

html_theme = "furo"
html_title = "goldsluice"
html_static_path = []
html_theme_options = {
    "source_repository": "https://github.com/villano-lab/goldsluice/",
    "source_branch": "develop",
    "source_directory": "docs/",
}
html_copy_source = False
html_show_sourcelink = False
