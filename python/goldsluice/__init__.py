"""goldsluice: fast pulse-reduction kernels in Rust, with a Python mirror of every algorithm (see `README.md`)."""
from .algorithms import ALGORITHMS, run
from .profile import compare

__version__ = "0.1.2"
__all__ = ["ALGORITHMS", "run", "compare"]
