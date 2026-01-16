"""Statistical utilities."""

from typing import Callable
import numpy as np
from numpy.typing import NDArray


class WelfordAccumulator:
    """
    Online computation of mean and variance using Welford's algorithm.

    This algorithm is numerically stable and computes mean and variance
    in a single pass through the data.

    Example:
        >>> acc = WelfordAccumulator()
        >>> for x in [1, 2, 3, 4, 5]:
        ...     acc.update(x)
        >>> acc.mean
        3.0
        >>> acc.variance
        2.5
    """

    def __init__(self) -> None:
        """Initialize accumulator with zero observations."""
        self._n = 0
        self._mean = 0.0
        self._m2 = 0.0

    def update(self, x: float) -> None:
        """
        Add a new observation.

        Args:
            x: New observation value.
        """
        self._n += 1
        delta = x - self._mean
        self._mean += delta / self._n
        delta2 = x - self._mean
        self._m2 += delta * delta2

    @property
    def count(self) -> int:
        """Return number of observations."""
        return self._n

    @property
    def mean(self) -> float:
        """Return current mean."""
        return self._mean

    @property
    def variance(self) -> float:
        """
        Return current sample variance (n-1 denominator).

        Raises:
            ValueError: If fewer than 2 observations.
        """
        if self._n < 2:
            raise ValueError("Need at least 2 observations for variance")
        return self._m2 / (self._n - 1)

    @property
    def std(self) -> float:
        """Return current sample standard deviation."""
        return np.sqrt(self.variance)


def bootstrap_ci(
    data: NDArray[np.floating],
    statistic: Callable[[NDArray[np.floating]], float] = np.mean,
    n_bootstrap: int = 1000,
    confidence: float = 0.95,
    rng: np.random.Generator | None = None,
) -> tuple[float, float]:
    """
    Compute bootstrap confidence interval for a statistic.

    Args:
        data: Sample data.
        statistic: Function that computes the statistic from a sample.
        n_bootstrap: Number of bootstrap samples.
        confidence: Confidence level (0 < confidence < 1).
        rng: Random number generator for reproducibility.

    Returns:
        Tuple of (lower_bound, upper_bound).

    Example:
        >>> rng = np.random.default_rng(42)
        >>> data = rng.standard_normal(100)
        >>> lower, upper = bootstrap_ci(data, np.mean, rng=rng)
    """
    if rng is None:
        rng = np.random.default_rng()

    data = np.asarray(data)
    n = len(data)

    bootstrap_stats = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sample_indices = rng.integers(0, n, size=n)
        bootstrap_sample = data[sample_indices]
        bootstrap_stats[i] = statistic(bootstrap_sample)

    alpha = 1 - confidence
    lower = np.percentile(bootstrap_stats, 100 * alpha / 2)
    upper = np.percentile(bootstrap_stats, 100 * (1 - alpha / 2))

    return float(lower), float(upper)
