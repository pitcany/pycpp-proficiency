# Python Core Concepts for Absolute Beginners

This guide covers the fundamental Python concepts you need before starting Week 1.

## 1. Variables and Types

Python uses **dynamic typing**—you don't declare types explicitly:

```python
x = 42              # Integer
y = 3.14            # Float (floating-point number)
name = "Alice"      # String
is_valid = True     # Boolean (note: capital T)
```

**Contrast with R:**
```r
x <- 42           # R uses <- for assignment
y <- 3.14
name <- "Alice"
is_valid <- TRUE  # R uses all caps
```

**Contrast with MATLAB:**
```matlab
x = 42;           % MATLAB uses semicolons (optional)
y = 3.14;
name = 'Alice';   % Single quotes for strings
```

**Key insight:** Variables are **references** to objects, not containers. More on this in Week 1, Day 2.

---

## 2. Printing Output

```python
age = 30
print("Age:", age)
print(f"Age: {age}")  # f-string (formatted string literal)
```

Output:
```
Age: 30
Age: 30
```

**f-strings** (formatted string literals) are the modern way to format output in Python.

---

## 3. Functions

```python
def square(x):
    """Return the square of x."""
    return x * x

result = square(5)
print(f"Result: {result}")  # Result: 25
```

**Key points:**
- Use `def` to define functions
- Indentation matters (4 spaces is standard)
- Docstrings (triple-quoted strings) document functions
- No type declarations required (but Week 1 will introduce type hints)

**Contrast with R:**
```r
square <- function(x) {
  x * x
}
```

**Contrast with MATLAB:**
```matlab
function result = square(x)
    result = x * x;
end
```

---

## 4. Control Flow

### If statements

```python
x = 10
if x > 5:
    print("x is large")
elif x > 0:
    print("x is positive")
else:
    print("x is non-positive")
```

**Note:** Python uses `elif` (not `else if`) and **indentation** (not braces or `end`).

### For loops

```python
# Loop through a range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Key insight:** Python's `for` loops iterate over sequences, not indices (unlike C/C++).

### While loops

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 5. Lists

Lists are Python's primary sequence type (like R vectors or MATLAB arrays, but more flexible):

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])   # 1 (zero-indexed!)
print(numbers[-1])  # 5 (negative indices count from end)

# Add element
numbers.append(6)

# Slice
print(numbers[1:3])  # [2, 3] (start:stop, excludes stop)

# Length
print(len(numbers))  # 6
```

**Critical:** Python uses **0-based indexing** (unlike R and MATLAB, which start at 1).

### List Comprehensions (Preview)

A compact way to create lists:

```python
# Traditional loop
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension (more Pythonic)
squares = [i ** 2 for i in range(5)]
# Result: [0, 1, 4, 9, 16]
```

You'll learn more about comprehensions in Week 1, Day 1.

---

## 6. Dictionaries

Dictionaries store key-value pairs (like named lists in R):

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "Seattle"
}

print(person["name"])    # Alice
person["age"] = 31       # Update value
person["email"] = "alice@example.com"  # Add new key-value pair

# Check if key exists
if "email" in person:
    print(person["email"])

# Loop through keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 7. Importing Modules

Python code is organized into modules:

```python
import math
print(math.sqrt(16))  # 4.0

# Import specific function
from math import sqrt
print(sqrt(16))  # 4.0

# Import with alias
import numpy as np
x = np.array([1, 2, 3])
```

**Week 1 will focus on NumPy and Pandas**, the core libraries for statistical computing.

---

## 8. Indentation is Syntax

Unlike most languages, Python uses indentation to define code blocks:

```python
# Correct
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

# Wrong - IndentationError
def greet(name):
if name:  # Missing indentation!
    print(f"Hello, {name}!")
```

**Standard:** Use 4 spaces for each indentation level (not tabs).

---

## Python vs. R vs. MATLAB Quick Reference

| Concept | Python | R | MATLAB |
|---------|--------|---|---------|
| Assignment | `x = 5` | `x <- 5` | `x = 5;` |
| Indexing | `arr[0]` (0-based) | `arr[1]` (1-based) | `arr(1)` (1-based) |
| Range | `range(5)` → 0,1,2,3,4 | `1:5` → 1,2,3,4,5 | `1:5` → 1,2,3,4,5 |
| Function | `def f(x):` | `f <- function(x)` | `function y = f(x)` |
| Comment | `# comment` | `# comment` | `% comment` |
| Print | `print(x)` | `print(x)` or `cat(x)` | `disp(x)` |
| String | `"hello"` or `'hello'` | `"hello"` or `'hello'` | `'hello'` (single only) |
| Boolean | `True`, `False` | `TRUE`, `FALSE` | `true`, `false` |
| Logical AND | `and` or `&` | `&&` or `&` | `&&` or `&` |
| Logical OR | `or` or `\|` | `\|\|` or `\|` | `\|\|` or `\|` |

---

## Common Gotchas for R/MATLAB Users

### 1. Zero-based indexing
```python
data = [10, 20, 30]
data[0]  # 10 in Python, would be data[1] in R/MATLAB
```

### 2. Range excludes endpoint
```python
range(5)      # 0, 1, 2, 3, 4 (5 is excluded)
# Compare to R: 1:5 gives 1, 2, 3, 4, 5
```

### 3. Integer division
```python
5 / 2    # 2.5 (float division)
5 // 2   # 2 (integer division)
```

### 4. Indentation matters
Python doesn't use `end` or braces—whitespace defines blocks.

### 5. Mutable vs immutable
```python
# Lists are mutable
lst = [1, 2, 3]
lst[0] = 99  # Works

# Strings are immutable
s = "hello"
s[0] = 'H'   # Error!
```

---

## Tips for Success

1. **Use an IDE or editor with Python support**: VS Code, PyCharm, or Jupyter notebooks
2. **Enable linting**: Tools like `pylint` or `flake8` catch common mistakes
3. **Read error messages carefully**: Python error messages include line numbers and helpful descriptions
4. **Use the interactive interpreter**: Type `python` in terminal to test snippets
5. **Practice incrementally**: Run your code frequently to catch errors early

---

## What's Next

Once you're comfortable with these concepts, proceed to the exercises. After completing the exercises, you'll be ready for Week 1, where you'll learn:

- Type hints and modern Python practices
- NumPy for vectorized operations
- Pandas for data manipulation
- How Python's memory model affects performance
- Writing efficient, production-quality code

Remember: Day 0.5 is about basic syntax. Week 1 teaches you Python **for statistical computing**.
