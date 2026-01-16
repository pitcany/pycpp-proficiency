"""Numerically stable algorithms."""

import numpy as np
from numpy.typing import NDArray


def log_sum_exp(x: NDArray[np.floating]) -> float:
    """
    Compute log(sum(exp(x))) in a numerically stable way.

    Uses the log-sum-exp trick to avoid overflow/underflow.

    Args:
        x: Array of values.

    Returns:
        log(sum(exp(x)))

    Example:
        >>> log_sum_exp(np.array([1000, 1000, 1000]))
        1001.0986...
    """
    x = np.asarray(x)
    x_max = np.max(x)
    if not np.isfinite(x_max):
        return x_max
    return x_max + np.log(np.sum(np.exp(x - x_max)))


def stable_softmax(x: NDArray[np.floating], axis: int = -1) -> NDArray[np.floating]:
    """
    Compute softmax in a numerically stable way.

    Args:
        x: Input array.
        axis: Axis along which to compute softmax.

    Returns:
        Softmax probabilities (same shape as x).

    Example:
        >>> stable_softmax(np.array([1000, 1000, 1000]))
        array([0.333..., 0.333..., 0.333...])
    """
    x = np.asarray(x)
    x_max = np.max(x, axis=axis, keepdims=True)
    exp_x = np.exp(x - x_max)
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)


def kahan_sum(x: NDArray[np.floating]) -> float:
    """
    Sum array elements using Kahan compensated summation.

    Reduces floating-point error accumulation compared to naive summation.

    Args:
        x: Array of values to sum.

    Returns:
        Sum with reduced floating-point error.

    Example:
        >>> kahan_sum(np.array([1e16, 1.0, 1.0, 1.0]))
        10000000000000003.0
    """
    x = np.asarray(x).ravel()
    total = 0.0
    compensation = 0.0

    for xi in x:
        y = xi - compensation
        t = total + y
        compensation = (t - total) - y
        total = t

    return total
