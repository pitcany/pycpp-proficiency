#include <gtest/gtest.h>
#include <cmath>
#include <limits>
#include "numerical.hpp"

TEST(LogSumExp, BasicCase) {
    std::vector<double> x = {1.0, 2.0, 3.0};
    double result = numerical::log_sum_exp(x);
    double expected = std::log(std::exp(1) + std::exp(2) + std::exp(3));
    EXPECT_NEAR(result, expected, 1e-10);
}

TEST(LogSumExp, LargeValues) {
    std::vector<double> x = {1000, 1000, 1000};
    double result = numerical::log_sum_exp(x);
    double expected = 1000 + std::log(3);
    EXPECT_NEAR(result, expected, 1e-10);
}

TEST(LogSumExp, SmallValues) {
    std::vector<double> x = {-1000, -1000, -1000};
    double result = numerical::log_sum_exp(x);
    double expected = -1000 + std::log(3);
    EXPECT_NEAR(result, expected, 1e-10);
}

TEST(LogSumExp, EmptyVector) {
    std::vector<double> x;
    double result = numerical::log_sum_exp(x);
    EXPECT_EQ(result, -std::numeric_limits<double>::infinity());
}

TEST(KahanSum, ReducesError) {
    std::vector<double> x;
    x.push_back(1e16);
    for (int i = 0; i < 10000; ++i) {
        x.push_back(1.0);
    }
    double kahan = numerical::kahan_sum(x);
    double expected = 1e16 + 10000;
    EXPECT_NEAR(kahan, expected, 1e6);  // Within 0.0001% of 1e16
}

TEST(ApproxEqual, BasicCases) {
    EXPECT_TRUE(numerical::approx_equal(1.0, 1.0));
    EXPECT_TRUE(numerical::approx_equal(1.0, 1.0 + 1e-10));
    EXPECT_FALSE(numerical::approx_equal(1.0, 2.0));
}

TEST(ApproxEqual, NaN) {
    double nan = std::numeric_limits<double>::quiet_NaN();
    EXPECT_FALSE(numerical::approx_equal(nan, nan));
    EXPECT_FALSE(numerical::approx_equal(1.0, nan));
}

TEST(ApproxEqual, Infinity) {
    double inf = std::numeric_limits<double>::infinity();
    EXPECT_TRUE(numerical::approx_equal(inf, inf));
    EXPECT_TRUE(numerical::approx_equal(-inf, -inf));
    EXPECT_FALSE(numerical::approx_equal(inf, -inf));
}
