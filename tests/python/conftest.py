"""Shared pytest fixtures."""

import numpy as np
import pytest


@pytest.fixture
def rng():
    """Reproducible random number generator."""
    return np.random.default_rng(42)


@pytest.fixture
def normal_sample(rng):
    """Standard normal sample for testing."""
    return rng.standard_normal(1000)


@pytest.fixture
def small_sample():
    """Small sample for edge case testing."""
    return np.array([1.0, 2.0, 3.0])
