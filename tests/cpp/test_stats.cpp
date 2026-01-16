#include <gtest/gtest.h>
#include <cmath>
#include <stdexcept>
#include "stats.hpp"

TEST(WelfordAccumulator, EmptyAccumulator) {
    stats::WelfordAccumulator acc;
    EXPECT_EQ(acc.count(), 0);
    EXPECT_EQ(acc.mean(), 0.0);
}

TEST(WelfordAccumulator, SingleValue) {
    stats::WelfordAccumulator acc;
    acc.update(5.0);
    EXPECT_EQ(acc.count(), 1);
    EXPECT_DOUBLE_EQ(acc.mean(), 5.0);
}

TEST(WelfordAccumulator, VarianceRequiresTwoValues) {
    stats::WelfordAccumulator acc;
    acc.update(5.0);
    EXPECT_THROW(acc.variance(), std::runtime_error);
}

TEST(WelfordAccumulator, KnownValues) {
    stats::WelfordAccumulator acc;
    for (int i = 1; i <= 10; ++i) {
        acc.update(static_cast<double>(i));
    }
    EXPECT_EQ(acc.count(), 10);
    EXPECT_DOUBLE_EQ(acc.mean(), 5.5);

    // Sample variance of 1..10 is 9.166666...
    double expected_var = 0;
    for (int i = 1; i <= 10; ++i) {
        expected_var += (i - 5.5) * (i - 5.5);
    }
    expected_var /= 9;  // n-1 denominator

    EXPECT_NEAR(acc.variance(), expected_var, 1e-10);
}

TEST(WelfordAccumulator, NumericalStability) {
    stats::WelfordAccumulator acc;

    // Large values with small differences
    double base = 1e9;
    for (int i = 0; i < 1000; ++i) {
        acc.update(base + (i % 10));
    }

    // Mean should be approximately base + 4.5
    EXPECT_NEAR(acc.mean(), base + 4.5, 0.1);

    // Variance should be approximately 8.25 (variance of 0..9)
    EXPECT_NEAR(acc.variance(), 8.25, 0.1);
}

TEST(WelfordAccumulator, Reset) {
    stats::WelfordAccumulator acc;
    acc.update(1.0);
    acc.update(2.0);
    acc.reset();

    EXPECT_EQ(acc.count(), 0);
    EXPECT_EQ(acc.mean(), 0.0);
}
