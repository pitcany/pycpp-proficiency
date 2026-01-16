# Day 11: STL Containers, Algorithms, and Iterators - Exercises

## Foundational Exercises

### Exercise 11.1: Erase-Remove Idiom

**Objective**: Use the erase-remove idiom correctly.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

// Remove all even numbers from vector
// Bug: This doesn't work correctly
void remove_evens_wrong(std::vector<int>& v) {
    for (auto it = v.begin(); it != v.end(); ++it) {
        if (*it % 2 == 0) {
            v.erase(it);  // Bug: iterator invalidated!
        }
    }
}

// TODO: Fix using erase-remove idiom
void remove_evens_correct(std::vector<int>& v) {
    // Hint: std::remove_if + erase
}

// TODO: Modern C++20 version
void remove_evens_modern(std::vector<int>& v) {
    // Hint: std::erase_if
}

int main() {
    std::vector<int> v1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    remove_evens_correct(v1);
    // Should be: 1, 3, 5, 7, 9

    for (int x : v1) std::cout << x << " ";
    std::cout << std::endl;

    return 0;
}
```

---

### Exercise 11.2: Transform and Accumulate

**Objective**: Use STL algorithms to replace loops.

```cpp
#include <algorithm>
#include <numeric>
#include <vector>
#include <iostream>
#include <cmath>

// Task 1: Compute sum of squares
// Loop version:
double sum_of_squares_loop(const std::vector<double>& v) {
    double sum = 0;
    for (size_t i = 0; i < v.size(); ++i) {
        sum += v[i] * v[i];
    }
    return sum;
}

// TODO: Algorithm version using transform + accumulate (or inner_product)
double sum_of_squares_algo(const std::vector<double>& v) {
}

// Task 2: Normalize vector to unit length
// Loop version:
void normalize_loop(std::vector<double>& v) {
    double norm = std::sqrt(sum_of_squares_loop(v));
    for (size_t i = 0; i < v.size(); ++i) {
        v[i] /= norm;
    }
}

// TODO: Algorithm version
void normalize_algo(std::vector<double>& v) {
}

// Task 3: Count elements in range [low, high]
// TODO: Use std::count_if
int count_in_range(const std::vector<int>& v, int low, int high) {
}
```

---

### Exercise 11.3: Custom Comparator with Lambda

**Objective**: Sort with custom comparison criteria.

```cpp
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

struct Person {
    std::string name;
    int age;
    double salary;
};

int main() {
    std::vector<Person> people = {
        {"Alice", 30, 50000},
        {"Bob", 25, 60000},
        {"Charlie", 35, 45000},
        {"Diana", 28, 55000}
    };

    // TODO: Sort by age (ascending)
    std::sort(people.begin(), people.end(), /* lambda */);

    // TODO: Sort by salary (descending)
    std::sort(people.begin(), people.end(), /* lambda */);

    // TODO: Sort by name length, then alphabetically
    std::sort(people.begin(), people.end(), /* lambda */);

    // TODO: Stable sort by age (preserve relative order)
    std::stable_sort(people.begin(), people.end(), /* lambda */);

    // TODO: Partial sort - get top 2 by salary
    std::partial_sort(people.begin(), people.begin() + 2, people.end(),
        /* lambda */);

    return 0;
}
```

---

## Proficiency Exercises

### Exercise 11.4: Container Selection

**Objective**: Choose the right container for each scenario.

```cpp
// For each scenario, choose the best container and explain why.
// Options: vector, deque, list, set, map, unordered_set, unordered_map

// Scenario 1: Store student grades, frequent random access by index
// Container: ???
// Reason: ???

// Scenario 2: Priority queue with frequent min extraction
// Container: ???
// Reason: ???

// Scenario 3: Cache with O(1) lookup by string key
// Container: ???
// Reason: ???

// Scenario 4: Maintain sorted unique elements with O(log n) insert
// Container: ???
// Reason: ???

// Scenario 5: Queue for BFS, add to back, remove from front
// Container: ???
// Reason: ???

// Scenario 6: Frequent insertion/removal in the middle
// Container: ???
// Reason: ???
```

---

### Exercise 11.5: Iterator Invalidation

**Objective**: Identify iterator invalidation bugs.

```cpp
#include <vector>
#include <map>
#include <list>
#include <iostream>

// Bug 1: Vector invalidation
void bug1() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    auto it = v.begin();
    v.push_back(6);  // May reallocate!
    *it = 10;        // Bug: it may be invalid
}

// Bug 2: Map invalidation during iteration
void bug2() {
    std::map<int, std::string> m = {{1, "a"}, {2, "b"}, {3, "c"}};
    for (auto it = m.begin(); it != m.end(); ++it) {
        if (it->first % 2 == 0) {
            m.erase(it);  // Bug: it is invalidated
        }
    }
}

// TODO: Fix both bugs
void fixed1() {
}

void fixed2() {
}
```

---

### Exercise 11.6: Algorithm Composition

**Objective**: Combine algorithms for complex operations.

```cpp
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>

struct Transaction {
    std::string category;
    double amount;
    bool is_expense;
};

std::vector<Transaction> transactions = {
    {"food", 50.0, true},
    {"salary", 3000.0, false},
    {"transport", 30.0, true},
    {"food", 75.0, true},
    {"utilities", 100.0, true},
    {"bonus", 500.0, false}
};

// TODO: Using only STL algorithms (no raw loops):

// 1. Total expenses
double total_expenses() {
}

// 2. Total income
double total_income() {
}

// 3. Largest expense category
std::string largest_expense_category() {
}

// 4. Are there any expenses over $100?
bool has_large_expense() {
}

// 5. Sort transactions by amount (descending)
void sort_by_amount(std::vector<Transaction>& txns) {
}
```

---

## Mastery Exercises

### Exercise 11.7: Custom Container Adapter

**Objective**: Implement a frequency counter using STL.

```cpp
#include <unordered_map>
#include <vector>
#include <algorithm>

template<typename T>
class FrequencyCounter {
private:
    std::unordered_map<T, int> counts_;

public:
    void add(const T& item) {
        // TODO: Increment count
    }

    int count(const T& item) const {
        // TODO: Return count (0 if not found)
    }

    T most_common() const {
        // TODO: Return item with highest count
    }

    std::vector<std::pair<T, int>> top_n(size_t n) const {
        // TODO: Return n most common items with counts
    }

    void merge(const FrequencyCounter& other) {
        // TODO: Combine counts from other
    }
};
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Erase-remove | Wrong | Correct but verbose | Idiomatic |
| Algorithm usage | Uses loops | Partial usage | Full algorithm usage |
| Container choice | Wrong container | Acceptable | Optimal |
| Iterator safety | Bugs present | Mostly safe | Fully safe |
