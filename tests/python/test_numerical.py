"""Tests for numerical utilities."""

import numpy as np
import pytest
from python_lib.numerical import log_sum_exp, stable_softmax, kahan_sum


class TestLogSumExp:
    """Tests for log_sum_exp function."""

    def test_basic_case(self):
        x = np.array([1.0, 2.0, 3.0])
        result = log_sum_exp(x)
        expected = np.log(np.exp(1) + np.exp(2) + np.exp(3))
        assert np.isclose(result, expected)

    def test_large_values_no_overflow(self):
        x = np.array([1000, 1000, 1000])
        result = log_sum_exp(x)
        expected = 1000 + np.log(3)
        assert np.isclose(result, expected)

    def test_small_values_no_underflow(self):
        x = np.array([-1000, -1000, -1000])
        result = log_sum_exp(x)
        expected = -1000 + np.log(3)
        assert np.isclose(result, expected)

    def test_single_value(self):
        x = np.array([5.0])
        result = log_sum_exp(x)
        assert np.isclose(result, 5.0)

    def test_handles_infinity(self):
        x = np.array([np.inf, 1.0, 2.0])
        result = log_sum_exp(x)
        assert result == np.inf


class TestStableSoftmax:
    """Tests for stable_softmax function."""

    def test_sums_to_one(self):
        x = np.array([1.0, 2.0, 3.0])
        result = stable_softmax(x)
        assert np.isclose(result.sum(), 1.0)

    def test_large_values(self):
        x = np.array([1000, 1000, 1000])
        result = stable_softmax(x)
        assert np.allclose(result, [1/3, 1/3, 1/3])

    def test_2d_axis(self):
        x = np.array([[1, 2, 3], [1, 2, 1000]])
        result = stable_softmax(x, axis=1)
        assert np.allclose(result.sum(axis=1), [1.0, 1.0])
        # Second row should be dominated by 1000
        assert result[1, 2] > 0.99


class TestKahanSum:
    """Tests for Kahan summation."""

    def test_reduces_error(self):
        x = np.array([1e16] + [1.0] * 10000)
        result = kahan_sum(x)
        expected = 1e16 + 10000
        # Kahan should get closer to expected than naive sum
        naive = np.sum(x)
        assert abs(result - expected) <= abs(naive - expected)

    def test_small_values(self):
        x = np.array([0.1] * 10)
        result = kahan_sum(x)
        assert np.isclose(result, 1.0)
