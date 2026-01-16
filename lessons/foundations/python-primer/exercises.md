# Day 0.5: Python Primer - Exercises

## Exercise 1: Hello, Statistics (10 min)

**Objective**: Verify you can run Python scripts and produce output.

**Task**: Write a Python script that prints:
```
Welcome to Statistical Computing!
Python + Statistics = Insight
```

**Instructions**:
1. Create a file named `hello_stats.py`
2. Save it in the `python/` directory
3. Run it with `python python/hello_stats.py`

**Solution approaches**:
- Use two `print()` statements
- Or use a multi-line string with triple quotes: `print("""line1\nline2""")`

---

## Exercise 2: Mean Calculator (20 min)

**Objective**: Write a function with parameters and return value.

**Starter code** (save as `python/mean_calculator.py`):
```python
def compute_mean(data):
    """Return the mean of a list of numbers."""
    # Your code here
    pass  # Remove this placeholder

# Test your function
values = [1.0, 2.0, 3.0, 4.0, 5.0]
mean = compute_mean(values)
print(f"Mean: {mean}")  # Should print 3.0
```

**Hints**:
- Use `sum(data)` to get the sum
- Use `len(data)` to get the count
- Return `sum(data) / len(data)`

**Expected output**:
```
Mean: 3.0
```

---

## Exercise 3: Variance Calculator (30 min)

**Objective**: Implement a more complex statistical function using loops.

**Task**: Extend Exercise 2 to compute variance.

**Starter code** (save as `python/variance_calculator.py`):
```python
def compute_mean(data):
    """Return the mean of a list of numbers."""
    return sum(data) / len(data)

def compute_variance(data):
    """Return the variance of a list of numbers.

    Variance = mean of squared deviations from mean
    """
    # Your code here
    pass

# Test your function
values = [1.0, 2.0, 3.0, 4.0, 5.0]
variance = compute_variance(values)
print(f"Variance: {variance}")  # Should print 2.0
```

**Hints**:
1. First compute the mean (reuse your `compute_mean` function or recalculate)
2. Compute squared deviations using a list comprehension:
   ```python
   squared_deviations = [(x - mean)**2 for x in data]
   ```
3. Return the mean of squared deviations

**Expected output**:
```
Variance: 2.0
```

**Challenge**: Can you do it in a single line using a list comprehension?

---

## Exercise 4: Working with Dictionaries (20 min)

**Objective**: Create and return structured data using dictionaries.

**Task**: Create a function that returns a statistical summary as a dictionary.

**Starter code** (save as `python/summary_stats.py`):
```python
def compute_mean(data):
    """Return the mean of a list of numbers."""
    return sum(data) / len(data)

def compute_variance(data):
    """Return the variance of a list of numbers."""
    mean = compute_mean(data)
    squared_deviations = [(x - mean)**2 for x in data]
    return sum(squared_deviations) / len(data)

def summarize(data):
    """Return a dictionary with mean, variance, and count.

    Args:
        data: List of numbers

    Returns:
        Dictionary with keys 'mean', 'variance', and 'n'
    """
    # Your code here
    pass

# Test your function
values = [1.0, 2.0, 3.0, 4.0, 5.0]
summary = summarize(values)
print(summary)
# Should print: {'mean': 3.0, 'variance': 2.0, 'n': 5}
```

**Hints**:
- Create an empty dictionary: `result = {}`
- Or create it with initial values:
  ```python
  return {
      'mean': compute_mean(data),
      'variance': compute_variance(data),
      'n': len(data)
  }
  ```

**Expected output**:
```python
{'mean': 3.0, 'variance': 2.0, 'n': 5}
```

---

## Common Mistakes to Avoid

### 1. Indentation errors
```python
# Wrong
def foo():
print("Hello")  # IndentationError

# Correct
def foo():
    print("Hello")
```

### 2. Using 1-based indexing
```python
data = [10, 20, 30]
print(data[1])  # Prints 20, not 10!
# Remember: Python is 0-indexed
print(data[0])  # Prints 10
```

### 3. Forgetting the colon
```python
# Wrong
if x > 0
    print("positive")

# Correct
if x > 0:
    print("positive")
```

### 4. Modifying lists while iterating
```python
# Dangerous
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)  # Can skip elements!

# Better - create new list
numbers = [n for n in numbers if n % 2 != 0]
```

---

## Verification

Once you've completed all exercises, verify:

1. All scripts run without errors
2. Output matches expected values
3. You understand what each line does
4. You can modify the code and predict the changes

**If you're stuck for more than 30 minutes on any exercise**, review the concepts section or consult the additional resources in the README.

---

## Next Level

If you found these exercises too easy, you're likely ready for Day 1. Consider these challenge problems:

**Challenge 1**: Add a `compute_std()` function that returns the standard deviation (square root of variance). You'll need to import the math module:
```python
import math
```

**Challenge 2**: Modify `summarize()` to also include minimum, maximum, and median values.

**Challenge 3**: Create a function that reads numbers from a file (one per line) and returns their summary statistics.
