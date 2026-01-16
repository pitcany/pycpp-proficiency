# Day 7.5: C++ Primer - Exercises

## Exercise 1: Hello, Statistics (10 min)

**Objective**: Verify you can compile and run C++ programs.

**Task**: Write a program that prints:
```
Welcome to Statistical Computing!
Python + C++ = Power
```

**Instructions**:
1. Create a file named `hello_stats.cpp` in the `cpp/` directory
2. Compile it: `g++ -std=c++17 cpp/hello_stats.cpp -o cpp/hello_stats`
3. Run it: `./cpp/hello_stats`

**Hints**:
- Use `#include <iostream>`
- Use `std::cout` twice with `std::endl`
- Remember `int main()` and `return 0;`

**Solution template**:
```cpp
#include <iostream>

int main() {
    // Your code here
    return 0;
}
```

---

## Exercise 2: Mean Calculator (20 min)

**Objective**: Write a function with parameters and return value.

**Starter code** (save as `cpp/mean_calculator.cpp`):
```cpp
#include <iostream>
#include <vector>

double compute_mean(const std::vector<double>& data) {
    // Your code here
    // Hint: Loop through the vector and accumulate the sum
    // Then divide by data.size()
    return 0.0;  // Replace with actual calculation
}

int main() {
    std::vector<double> values = {1.0, 2.0, 3.0, 4.0, 5.0};
    double mean = compute_mean(values);
    std::cout << "Mean: " << mean << std::endl;  // Should print 3
    return 0;
}
```

**Hints**:

**Approach 1: Traditional for loop**
```cpp
double sum = 0.0;
for (int i = 0; i < data.size(); i++) {
    sum += data[i];
}
return sum / data.size();
```

**Approach 2: Range-based for loop** (more modern)
```cpp
double sum = 0.0;
for (double value : data) {
    sum += value;
}
return sum / data.size();
```

**Expected output**:
```
Mean: 3
```

**Compilation**:
```bash
g++ -std=c++17 cpp/mean_calculator.cpp -o cpp/mean_calculator
./cpp/mean_calculator
```

---

## Exercise 3: Variance Calculator (30 min)

**Objective**: Implement a more complex statistical function.

**Task**: Extend Exercise 2 to also compute variance.

**Starter code** (save as `cpp/variance_calculator.cpp`):
```cpp
#include <iostream>
#include <vector>

double compute_mean(const std::vector<double>& data) {
    double sum = 0.0;
    for (double value : data) {
        sum += value;
    }
    return sum / data.size();
}

double compute_variance(const std::vector<double>& data, double mean) {
    // Variance = mean of squared deviations from mean
    // Your code here
    return 0.0;  // Replace with actual calculation
}

int main() {
    std::vector<double> values = {1.0, 2.0, 3.0, 4.0, 5.0};
    double mean = compute_mean(values);
    double variance = compute_variance(values, mean);

    std::cout << "Mean: " << mean << std::endl;
    std::cout << "Variance: " << variance << std::endl;
    return 0;
}
```

**Hints**:
1. Create a variable to accumulate the sum of squared deviations
2. Loop through the data
3. For each value, compute `(value - mean) * (value - mean)`
4. Add this to your accumulator
5. Return the accumulator divided by the number of elements

**Expected output**:
```
Mean: 3
Variance: 2
```

**Challenge**: Can you write a version that doesn't require passing the mean as a parameter? (Compute it inside `compute_variance()`)

---

## Common Mistakes to Avoid

### 1. Forgetting semicolons
```cpp
// Wrong
int x = 5
cout << x << endl

// Correct
int x = 5;
cout << x << endl;
```

### 2. Missing `std::`
```cpp
// Wrong (unless you have `using namespace std;`)
cout << "Hello" << endl;

// Correct
std::cout << "Hello" << std::endl;
```

### 3. Not including necessary headers
```cpp
// Wrong - won't compile
int main() {
    vector<int> v = {1, 2, 3};  // Error: vector not declared
}

// Correct
#include <vector>
int main() {
    std::vector<int> v = {1, 2, 3};
}
```

### 4. Mismatched types
```cpp
// Wrong
int result = 5.7;  // Loses precision (becomes 5)

// Correct
double result = 5.7;
```

### 5. Off-by-one errors in loops
```cpp
// Wrong - goes out of bounds
for (int i = 0; i <= data.size(); i++) {  // Note: <=
    cout << data[i];  // Will crash on last iteration
}

// Correct
for (int i = 0; i < data.size(); i++) {  // Note: <
    cout << data[i];
}
```

---

## Debugging Tips

### 1. Read the first error
Compiler errors cascade. Fix the first error and recompile.

### 2. Check the line number
The compiler tells you exactly where the problem is:
```
mean_calculator.cpp:10:5: error: expected ';' before 'return'
```
This means line 10, column 5.

### 3. Print intermediate values
Use `std::cout` to debug:
```cpp
std::cout << "DEBUG: sum = " << sum << std::endl;
```

### 4. Compile with warnings
```bash
g++ -std=c++17 -Wall -Wextra myprogram.cpp -o myprogram
```
Warnings catch many potential bugs.

---

## Verification Checklist

After completing all exercises, verify:

- [ ] All programs compile without errors or warnings
- [ ] Output matches expected values exactly
- [ ] You understand the purpose of `#include`, `main()`, and `return 0`
- [ ] You can explain the difference between `int` and `double`
- [ ] You know how to create and iterate through a `std::vector`
- [ ] You can read a compiler error and find the relevant line

---

## Next Level Challenges

If you found these exercises too easy, try these:

**Challenge 1**: Add a `compute_std()` function that returns the standard deviation (square root of variance). You'll need:
```cpp
#include <cmath>
// Then use: std::sqrt(variance)
```

**Challenge 2**: Modify the programs to read numbers from the command line:
```cpp
int main(int argc, char* argv[]) {
    // Parse command line arguments
}
```

**Challenge 3**: Create a program that reads numbers from a file and computes statistics:
```cpp
#include <fstream>
// Use std::ifstream to read from a file
```

**Challenge 4**: Compare the performance of different loop styles using:
```cpp
#include <chrono>
// Time your code
```

---

## Compilation Reference

### Basic compilation
```bash
g++ -std=c++17 myprogram.cpp -o myprogram
```

### With warnings
```bash
g++ -std=c++17 -Wall -Wextra myprogram.cpp -o myprogram
```

### With optimization (for performance testing)
```bash
g++ -std=c++17 -O2 myprogram.cpp -o myprogram
```

### With debug symbols (for debugging)
```bash
g++ -std=c++17 -g myprogram.cpp -o myprogram
```

---

## Ready for Day 8?

If you can complete all three exercises and understand the code you wrote, you're ready to proceed to Day 8: References, Pointers, and Ownership.

**If you're struggling**, don't worry! C++ has a steeper learning curve than Python. Consider:
- Working through [LearnCpp.com](http://LearnCpp.com) Chapters 1-6
- Reviewing the concepts.md file multiple times
- Writing more small programs to practice

The key is to be comfortable with basic syntax before diving into Week 2's advanced topics.
