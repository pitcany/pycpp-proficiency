"""Tests for statistical utilities."""

import numpy as np
import pytest
from python_lib.stats import WelfordAccumulator, bootstrap_ci


class TestWelfordAccumulator:
    """Tests for Welford's online algorithm."""

    def test_empty_accumulator(self):
        acc = WelfordAccumulator()
        assert acc.count == 0
        assert acc.mean == 0.0

    def test_single_value(self):
        acc = WelfordAccumulator()
        acc.update(5.0)
        assert acc.count == 1
        assert acc.mean == 5.0

    def test_variance_requires_two_values(self):
        acc = WelfordAccumulator()
        acc.update(5.0)
        with pytest.raises(ValueError):
            _ = acc.variance

    def test_known_values(self):
        acc = WelfordAccumulator()
        for i in range(1, 11):
            acc.update(float(i))

        assert acc.count == 10
        assert acc.mean == 5.5

        # Sample variance of 1..10
        expected_var = np.var(np.arange(1, 11), ddof=1)
        assert np.isclose(acc.variance, expected_var)

    def test_numerical_stability(self):
        acc = WelfordAccumulator()
        base = 1e9
        for i in range(1000):
            acc.update(base + (i % 10))

        # Should still get reasonable variance
        assert np.isclose(acc.mean, base + 4.5, atol=0.1)
        assert np.isclose(acc.variance, np.var(range(10), ddof=1), atol=0.1)


class TestBootstrapCI:
    """Tests for bootstrap confidence intervals."""

    def test_returns_tuple(self):
        rng = np.random.default_rng(42)
        data = rng.standard_normal(100)
        result = bootstrap_ci(data, rng=rng)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_lower_less_than_upper(self):
        rng = np.random.default_rng(42)
        data = rng.standard_normal(100)
        lower, upper = bootstrap_ci(data, rng=rng)
        assert lower < upper

    def test_reproducibility(self):
        rng1 = np.random.default_rng(42)
        rng2 = np.random.default_rng(42)
        data = np.array([1, 2, 3, 4, 5])

        result1 = bootstrap_ci(data, rng=rng1)
        result2 = bootstrap_ci(data, rng=rng2)

        assert result1 == result2

    def test_higher_confidence_wider_interval(self):
        rng1 = np.random.default_rng(42)
        rng2 = np.random.default_rng(42)
        data = np.random.default_rng(0).standard_normal(100)

        lower90, upper90 = bootstrap_ci(data, confidence=0.90, rng=rng1)
        lower95, upper95 = bootstrap_ci(data, confidence=0.95, rng=rng2)

        width90 = upper90 - lower90
        width95 = upper95 - lower95
        assert width95 >= width90
