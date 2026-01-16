# Day 14: C++ Capstone - Gaussian Mixture Model

**Time Estimate**: 4-6 hours

## Overview

Implement a Gaussian Mixture Model (GMM) fitting library in C++ that demonstrates all Week 2 skills. The GMM should use the Expectation-Maximization (EM) algorithm and be exposed to Python via pybind11.

## Mathematical Background

A GMM models data as a mixture of K Gaussian distributions:
```
p(x) = Σ_k π_k N(x | μ_k, Σ_k)
```

Where:
- π_k: mixing weights (sum to 1)
- μ_k: mean vectors
- Σ_k: covariance matrices

The EM algorithm alternates:
- **E-step**: Compute responsibilities (soft assignments)
- **M-step**: Update parameters given responsibilities

## Specification

### Directory Structure
```
cpp/
├── include/
│   ├── gmm/
│   │   ├── matrix.hpp      # Matrix class with RAII
│   │   ├── gmm.hpp         # GMM class
│   │   └── numerical.hpp   # Stable numerical functions
├── src/
│   ├── matrix.cpp
│   ├── gmm.cpp
│   └── bindings.cpp        # pybind11 bindings
├── tests/
│   ├── test_matrix.cpp
│   ├── test_gmm.cpp
│   └── test_numerical.cpp
└── CMakeLists.txt
```

### Required Components

#### 1. Matrix Class (RAII)
```cpp
class Matrix {
public:
    Matrix(size_t rows, size_t cols);
    Matrix(const Matrix& other);              // Deep copy
    Matrix(Matrix&& other) noexcept;          // Move
    Matrix& operator=(const Matrix& other);
    Matrix& operator=(Matrix&& other) noexcept;
    ~Matrix();

    double& operator()(size_t i, size_t j);
    const double& operator()(size_t i, size_t j) const;

    size_t rows() const;
    size_t cols() const;
    double* data();
    const double* data() const;

private:
    double* data_;
    size_t rows_, cols_;
};
```

#### 2. Numerical Stability Functions
```cpp
namespace numerical {
    // Log-sum-exp for vector
    double log_sum_exp(const double* values, size_t n);

    // Log of multivariate normal density
    double log_mvn_density(
        const double* x,          // Point (d-dimensional)
        const double* mean,       // Mean (d-dimensional)
        const Matrix& cov,        // Covariance (d x d)
        size_t d
    );

    // Stable computation of responsibilities
    void compute_responsibilities(
        const Matrix& log_likelihoods,  // N x K
        Matrix& responsibilities         // N x K, output
    );
}
```

#### 3. GMM Class
```cpp
class GMM {
public:
    GMM(size_t n_components, size_t n_dims, unsigned int seed = 42);

    // Fit GMM to data
    // Returns log-likelihood history
    std::vector<double> fit(
        const Matrix& X,           // N x D data matrix
        int max_iter = 100,
        double tol = 1e-4
    );

    // Predict responsibilities for new data
    Matrix predict_proba(const Matrix& X) const;

    // Access parameters
    const Matrix& means() const;
    const std::vector<Matrix>& covariances() const;
    const std::vector<double>& weights() const;

private:
    size_t n_components_;
    size_t n_dims_;

    Matrix means_;                    // K x D
    std::vector<Matrix> covariances_; // K matrices, each D x D
    std::vector<double> weights_;     // K weights

    std::mt19937 rng_;

    void initialize(const Matrix& X);
    void e_step(const Matrix& X, Matrix& responsibilities);
    void m_step(const Matrix& X, const Matrix& responsibilities);
    double compute_log_likelihood(const Matrix& X);
};
```

#### 4. pybind11 Bindings
```cpp
PYBIND11_MODULE(gmm_cpp, m) {
    py::class_<GMM>(m, "GMM")
        .def(py::init<size_t, size_t, unsigned int>(),
             py::arg("n_components"),
             py::arg("n_dims"),
             py::arg("seed") = 42)
        .def("fit", &GMM::fit_numpy,
             py::arg("X"),
             py::arg("max_iter") = 100,
             py::arg("tol") = 1e-4)
        .def("predict_proba", &GMM::predict_proba_numpy)
        .def_property_readonly("means", &GMM::means_numpy)
        .def_property_readonly("weights", &GMM::weights_numpy);
}
```

### Requirements Checklist

- [ ] Matrix class implements Rule of Five (copy, move, destructor)
- [ ] All memory managed with RAII (no raw new/delete in GMM)
- [ ] Log-sum-exp used throughout for numerical stability
- [ ] STL containers and algorithms used appropriately
- [ ] Row-major cache-friendly data layout
- [ ] E-step and M-step can be profiled separately
- [ ] pybind11 bindings compile and work
- [ ] NumPy arrays accepted without copying (where possible)
- [ ] Unit tests for Matrix operations
- [ ] Unit tests for numerical functions
- [ ] Integration tests comparing to sklearn
- [ ] Performance: <1s for N=10000, D=20, K=5

### Testing

```python
# test_gmm.py
import numpy as np
from sklearn.mixture import GaussianMixture
import gmm_cpp

def test_matches_sklearn():
    np.random.seed(42)
    X = np.vstack([
        np.random.randn(1000, 2) + [0, 0],
        np.random.randn(1000, 2) + [5, 5],
        np.random.randn(1000, 2) + [0, 5]
    ])

    # Fit sklearn
    sklearn_gmm = GaussianMixture(n_components=3, random_state=42)
    sklearn_gmm.fit(X)
    sklearn_proba = sklearn_gmm.predict_proba(X)

    # Fit C++
    cpp_gmm = gmm_cpp.GMM(3, 2, seed=42)
    cpp_gmm.fit(X)
    cpp_proba = cpp_gmm.predict_proba(X)

    # Should match within tolerance
    # (Note: exact match unlikely due to initialization differences)
    assert cpp_proba.shape == sklearn_proba.shape


def test_performance():
    import time
    np.random.seed(42)
    X = np.random.randn(10000, 20)

    gmm = gmm_cpp.GMM(5, 20, seed=42)
    start = time.time()
    gmm.fit(X, max_iter=50)
    elapsed = time.time() - start

    assert elapsed < 1.0, f"Too slow: {elapsed:.2f}s"
```

### Rubric

| Dimension | 0 | 1 | 2 |
|-----------|---|---|---|
| **Data Structures** | No RAII | Partial RAII | Complete Rule of Five |
| **EM Algorithm** | Wrong | Correct but unstable | Numerically stable |
| **Testing** | No tests | Basic tests | Comprehensive |
| **Performance** | >5s | 1-5s | <1s |
| **Python Binding** | Doesn't compile | Works | Zero-copy where possible |
| **sklearn Match** | >20% difference | <20% difference | <5% difference |
| **Documentation** | None | Comments only | Full API docs |

### Tips

1. Start with Matrix class and tests
2. Implement log-sum-exp before GMM
3. Test E-step and M-step separately
4. Use diagonal covariances first (simpler)
5. Profile before optimizing
6. Use AddressSanitizer during development

---

## Warmup Exercises

Before the capstone, complete these exercises:

### Exercise 14.1: pybind11 Hello World

```cpp
// hello.cpp
#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(hello, m) {
    m.doc() = "A simple example module";
    m.def("add", &add, "Add two integers");
}
```

Build and test:
```bash
# CMakeLists.txt
find_package(pybind11 REQUIRED)
pybind11_add_module(hello hello.cpp)

# Build
cmake -B build
cmake --build build

# Test
python -c "import hello; print(hello.add(1, 2))"
```

### Exercise 14.2: NumPy Array Binding

```cpp
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

// Compute sum of array elements
double array_sum(py::array_t<double> arr) {
    // TODO: Implement
}

// Multiply array by scalar in-place
void scale_inplace(py::array_t<double> arr, double factor) {
    // TODO: Implement (modify arr directly)
}

PYBIND11_MODULE(numpy_example, m) {
    m.def("array_sum", &array_sum);
    m.def("scale_inplace", &scale_inplace);
}
```
