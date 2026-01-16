"""General utilities."""

import time
import logging
from contextlib import contextmanager
from typing import Generator

import numpy as np


logger = logging.getLogger(__name__)


@contextmanager
def Timer(name: str = "Block") -> Generator[None, None, None]:
    """
    Context manager for timing code blocks.

    Args:
        name: Name to display in timing output.

    Example:
        >>> with Timer("my operation"):
        ...     time.sleep(0.1)
        Timer [my operation]: 100.xxx ms
    """
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        logger.info(f"Timer [{name}]: {elapsed * 1000:.3f} ms")


def set_reproducible_seed(seed: int = 42) -> np.random.Generator:
    """
    Create a reproducible random number generator.

    This is the preferred way to handle randomness - always use the returned
    generator rather than the global numpy.random functions.

    Args:
        seed: Seed for the random number generator.

    Returns:
        A numpy random Generator instance.

    Example:
        >>> rng = set_reproducible_seed(42)
        >>> rng.random(3)
        array([0.77395605, 0.43887844, 0.85859792])
    """
    return np.random.default_rng(seed)
