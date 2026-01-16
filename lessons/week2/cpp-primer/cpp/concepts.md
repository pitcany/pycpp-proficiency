# C++ Core Concepts for Absolute Beginners

This guide covers the fundamental C++ concepts you need before starting Week 2.

## 1. Program Structure

Every C++ program starts with `main()`:

```cpp
#include <iostream>  // Include standard library headers

int main() {
    // Your code here
    return 0;  // 0 means success
}
```

**Key points:**
- `#include` brings in library functionality (like Python's `import`)
- `main()` is the entry point (Python doesn't require this)
- `return 0;` signals successful completion
- Every statement ends with `;` (Python doesn't require this)
- Curly braces `{}` define blocks (Python uses indentation)

---

## 2. Variables and Types

C++ requires explicit type declarations:

```cpp
int x = 42;              // Integer
double y = 3.14;         // Floating-point
bool is_valid = true;    // Boolean
std::string name = "Alice";  // String (needs #include <string>)
```

**Contrast with Python:**
```python
x = 42          # Python infers type
y = 3.14
is_valid = True
name = "Alice"
```

**Why explicit types?** C++ needs to know how much memory to allocate. This enables faster execution but requires more upfront specification.

### Common Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer | `42`, `-7` |
| `double` | Floating-point | `3.14`, `-0.5` |
| `float` | Single-precision float | `3.14f` |
| `bool` | Boolean | `true`, `false` |
| `char` | Single character | `'A'`, `'z'` |
| `std::string` | Text string | `"hello"` |

---

## 3. Output

```cpp
#include <iostream>

int main() {
    int age = 30;
    std::cout << "Age: " << age << std::endl;
    return 0;
}
```

- `std::cout` is like Python's `print()`
- `<<` sends data to the output stream (think of it as "put into")
- `std::endl` is a newline (like `\n` in Python)

**Multiple values:**
```cpp
std::cout << "Name: " << name << ", Age: " << age << std::endl;
```

---

## 4. Functions

```cpp
#include <iostream>

// Function declaration (tells compiler it exists)
double square(double x);

int main() {
    double result = square(5.0);
    std::cout << "Result: " << result << std::endl;
    return 0;
}

// Function definition (actual implementation)
double square(double x) {
    return x * x;
}
```

**Key differences from Python:**
- Must specify return type (`double`) and parameter types
- Function must be declared before use (or defined before `main()`)
- No `def` keyword

**Alternative: Define before use**
```cpp
#include <iostream>

// Define function before main()
double square(double x) {
    return x * x;
}

int main() {
    double result = square(5.0);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
```

---

## 5. Control Flow

### If statements

```cpp
int x = 10;
if (x > 5) {
    std::cout << "x is large" << std::endl;
} else if (x > 0) {
    std::cout << "x is positive" << std::endl;
} else {
    std::cout << "x is non-positive" << std::endl;
}
```

**Key points:**
- Condition must be in parentheses: `if (condition)`
- Use curly braces for blocks (even single lines are good practice)
- Use `else if`, not `elif`

### For loops

```cpp
// Loop from 0 to 4
for (int i = 0; i < 5; i++) {
    std::cout << i << std::endl;
}
```

**Structure:** `for (initialization; condition; increment)`

Python equivalent: `for i in range(5):`

**Range-based for loop** (C++11 and later):
```cpp
std::vector<int> numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    std::cout << num << std::endl;
}
```

Python equivalent: `for num in numbers:`

### While loops

```cpp
int count = 0;
while (count < 3) {
    std::cout << count << std::endl;
    count++;
}
```

**Note:** `count++` is shorthand for `count = count + 1`

---

## 6. Arrays and Vectors

### C-style array (avoid for now)

```cpp
int arr[5] = {1, 2, 3, 4, 5};  // Fixed size
```

**Problems:**
- Fixed size at compile time
- No built-in size() method
- Easy to make mistakes

### Vector (use this instead)

```cpp
#include <vector>

std::vector<int> vec = {1, 2, 3, 4, 5};  // Dynamic size
vec.push_back(6);  // Add element
std::cout << vec[0] << std::endl;  // Access element
std::cout << vec.size() << std::endl;  // Get size
```

**Vectors are like Python lists but type-specific:**
```python
# Python
vec = [1, 2, 3, 4, 5]
vec.append(6)
print(vec[0])
print(len(vec))
```

**Common vector operations:**
```cpp
vec.push_back(7);     // Add to end
vec.pop_back();       // Remove from end
vec.clear();          // Remove all elements
vec.empty();          // Check if empty
vec.size();           // Number of elements
```

---

## 7. Understanding `std::`

`std::` is a **namespace** that prevents naming conflicts:

```cpp
std::cout << "Hello" << std::endl;  // Explicit namespace
```

**What's a namespace?** It groups related names together. The standard library uses the `std` namespace.

### Using directive (use with caution)

```cpp
using namespace std;  // Now you can skip std::
cout << "Hello" << endl;
```

**Warning:** `using namespace std;` is convenient but can cause naming conflicts in larger projects. Week 2 will teach you when it's safe.

**Better approach for beginners:**
```cpp
using std::cout;
using std::endl;
using std::vector;

cout << "Hello" << endl;  // Now just these need no std::
```

---

## 8. Const Correctness

The `const` keyword means "cannot be modified":

```cpp
const int MAX_SIZE = 100;  // Constant variable
MAX_SIZE = 200;  // Error!

// Const reference (efficient for large data)
double compute_mean(const std::vector<double>& data) {
    // data cannot be modified inside this function
    // & means reference (no copy), const means read-only
}
```

**Why use const references for parameters?**
- Avoids copying large data structures
- Guarantees the function won't modify the input
- More on this in Day 8

---

## 9. Type Conversion

```cpp
int x = 5;
double y = x;  // Implicit conversion (safe)

double a = 5.7;
int b = a;  // Implicit conversion (loses precision! b becomes 5)

// Explicit conversion (cast)
int c = static_cast<int>(a);  // Makes intention clear
```

---

## 10. Common Operators

### Arithmetic
```cpp
+   // Addition
-   // Subtraction
*   // Multiplication
/   // Division
%   // Modulo (remainder)
++  // Increment
--  // Decrement
```

### Comparison
```cpp
==  // Equal to
!=  // Not equal to
>   // Greater than
<   // Less than
>=  // Greater than or equal
<=  // Less than or equal
```

### Logical
```cpp
&&  // AND
||  // OR
!   // NOT
```

---

## 11. Input (Preview)

```cpp
#include <iostream>

int main() {
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;  // Read from keyboard
    std::cout << "You are " << age << " years old." << std::endl;
    return 0;
}
```

**Note:** `std::cin` is for input, `std::cout` is for output. Think of `>>` as "read from" and `<<` as "write to".

---

## Python vs. C++ Quick Reference

| Concept | Python | C++ |
|---------|--------|-----|
| Variable | `x = 5` | `int x = 5;` |
| Function | `def f(x):` | `double f(double x) { }` |
| Print | `print("Hi")` | `std::cout << "Hi" << std::endl;` |
| If statement | `if x > 5:` | `if (x > 5) { }` |
| For loop | `for i in range(5):` | `for (int i = 0; i < 5; i++) { }` |
| List/Vector | `lst = [1, 2, 3]` | `std::vector<int> vec = {1, 2, 3};` |
| Boolean | `True`, `False` | `true`, `false` |
| AND/OR | `and`, `or` | `&&`, `\|\|` |
| Not equal | `!=` | `!=` |
| String | `"hello"` or `'hello'` | `"hello"` (double quotes) |
| Comment | `# comment` | `// comment` or `/* comment */` |

---

## Common Gotchas for Python Developers

### 1. Semicolons are required
```cpp
int x = 5;  // Don't forget the semicolon!
```

### 2. Types are explicit
```cpp
double mean = compute_mean(data);  // Must declare type
```

### 3. Compilation is separate from execution
```bash
g++ program.cpp -o program  # Compile
./program                   # Run
```

### 4. Division behaves differently
```cpp
5 / 2       // 2 (integer division)
5.0 / 2     // 2.5 (floating-point division)
5 / 2.0     // 2.5
```

### 5. No automatic type coercion in some cases
```cpp
std::vector<double> vec = {1, 2, 3};  // OK: ints convert to double
std::vector<int> vec2 = {1.5, 2.5};   // OK: but loses precision
```

---

## Memory and Performance (Preview)

**Why is C++ faster than Python?**

1. **Compiled code:** Translated to machine code once, not interpreted every time
2. **Static typing:** Compiler knows exact memory layout
3. **No overhead:** Direct memory access without Python's object wrapper
4. **Manual control:** You decide when to allocate/deallocate (more in Day 8)

**Example:**
```cpp
// C++: Allocates exact memory needed for 1000 doubles
std::vector<double> data(1000);

# Python: Each number is a full Python object with overhead
data = [0.0] * 1000
```

---

## Include Guards and Headers (Preview)

You might see this pattern in header files:

```cpp
// myheader.h
#ifndef MYHEADER_H
#define MYHEADER_H

// Function declarations here

#endif
```

**Purpose:** Prevents multiple inclusion. You'll learn more about this in Week 2.

---

## Tips for Success

1. **Compile frequently**: Catch errors early
2. **Read compiler errors from top to bottom**: Fix the first error first
3. **Use meaningful variable names**: `mean` not `m`
4. **Enable warnings**: `g++ -Wall -Wextra`
5. **Keep functions small**: One task per function
6. **Use `std::vector` instead of arrays**: Safer and easier

---

## What's Next

Once you're comfortable with these concepts, proceed to the exercises. After completing the exercises, you'll be ready for Week 2, where you'll learn:

- Memory management (pointers, references, ownership)
- Object-oriented programming (classes, inheritance)
- Generic programming (templates)
- Standard library algorithms
- Performance optimization

Remember: Day 7.5 is about basic syntax. Week 2 teaches you C++ **for high-performance statistical computing**.
