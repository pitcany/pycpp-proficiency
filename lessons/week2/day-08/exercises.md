# Day 8: References, Pointers, and Ownership - Exercises

## Foundational Exercises

### Exercise 8.1: Stack vs Heap

**Objective**: Identify stack vs heap allocation and fix memory issues.

```cpp
// Which are stack, which are heap?
void analyze() {
    int a = 10;                    // ?
    int* b = new int(20);          // ?
    std::vector<int> v = {1,2,3};  // ?
    int* c = &a;                   // ?
    int arr[5];                    // ?
    int* d = new int[10];          // ?

    // TODO: Which need cleanup? Add appropriate deletes.
}
```

---

### Exercise 8.2: Fix the Dangling Reference

**Objective**: Identify and fix dangling reference bugs.

```cpp
#include <string>
#include <vector>

// Bug 1: Dangling reference
const std::string& get_greeting() {
    std::string greeting = "Hello, World!";
    return greeting;  // Bug: returning reference to local
}

// Bug 2: Reference to temporary
const int& max_element(const std::vector<int>& v) {
    if (v.empty()) {
        int zero = 0;
        return zero;  // Bug: returning reference to local
    }
    return *std::max_element(v.begin(), v.end());
}

// Bug 3: Iterator invalidation
void process(std::vector<int>& v) {
    for (auto& x : v) {
        if (x % 2 == 0) {
            v.push_back(x * 2);  // Bug: modifying container during iteration
        }
    }
}

// TODO: Fix all three functions
```

---

### Exercise 8.3: Use AddressSanitizer

**Objective**: Use AddressSanitizer to detect memory bugs.

Compile and run with:
```bash
g++ -fsanitize=address -g exercise.cpp -o exercise
./exercise
```

```cpp
#include <iostream>

int main() {
    // Bug 1: Heap buffer overflow
    int* arr = new int[10];
    arr[10] = 42;  // Out of bounds!

    // Bug 2: Use after free
    int* p = new int(42);
    delete p;
    std::cout << *p << std::endl;  // Use after free!

    // Bug 3: Memory leak
    int* leak = new int[1000];
    // Never deleted

    return 0;
}

// TODO: Run with AddressSanitizer and fix all bugs
```

---

## Proficiency Exercises

### Exercise 8.4: Implement a Dynamic Array

**Objective**: Implement a simple dynamic array with proper memory management.

```cpp
class DynamicArray {
private:
    int* data_;
    size_t size_;
    size_t capacity_;

public:
    DynamicArray() : data_(nullptr), size_(0), capacity_(0) {}

    ~DynamicArray() {
        // TODO: Free memory
    }

    void push_back(int value) {
        // TODO: Resize if needed, then add value
    }

    int& operator[](size_t index) {
        // TODO: Return reference to element
    }

    size_t size() const { return size_; }

private:
    void resize(size_t new_capacity) {
        // TODO: Allocate new array, copy data, free old
    }
};
```

---

### Exercise 8.5: Parameter Passing

**Objective**: Choose the correct parameter passing method.

```cpp
// For each function, choose the best parameter type:
// - int          (by value)
// - int&         (by reference)
// - const int&   (by const reference)
// - int*         (by pointer)
// - const int*   (by const pointer)

// 1. Increment a counter
void increment(??? counter);

// 2. Compute sum of vector elements
int sum(??? vec);

// 3. Swap two integers
void swap(??? a, ??? b);

// 4. Find element in array (may return null)
??? find(const int* arr, size_t n, int target);

// 5. Print a matrix (2D vector)
void print_matrix(??? matrix);
```

---

## Mastery Exercises

### Exercise 8.6: Object Lifetime Analysis

**Objective**: Trace object lifetimes in complex scenarios.

```cpp
#include <iostream>
#include <string>

class Tracker {
    std::string name_;
public:
    Tracker(const std::string& name) : name_(name) {
        std::cout << "Construct: " << name_ << std::endl;
    }
    ~Tracker() {
        std::cout << "Destruct: " << name_ << std::endl;
    }
    Tracker(const Tracker& other) : name_(other.name_ + "_copy") {
        std::cout << "Copy: " << name_ << std::endl;
    }
};

Tracker create_tracker() {
    Tracker t("local");
    return t;
}

int main() {
    std::cout << "=== Start ===" << std::endl;
    {
        Tracker a("a");
        Tracker b = create_tracker();
        Tracker* c = new Tracker("c");
        {
            Tracker d("d");
        }
        delete c;
    }
    std::cout << "=== End ===" << std::endl;
    return 0;
}

// TODO: Predict the output order before running
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Stack/heap understanding | Confused | Basic understanding | Deep understanding |
| Memory bug detection | Many bugs remain | Few bugs | All bugs fixed |
| AddressSanitizer usage | Cannot use | Basic usage | Proficient |
| Parameter passing | Wrong choices | Mostly correct | All optimal |
