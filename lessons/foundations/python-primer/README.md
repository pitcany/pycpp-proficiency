# 🐍 Day 0.5: Python Primer for Absolute Beginners

**Language**: Python
**Time Estimate**: 3-4 hours
**Notion Source**: [Link](https://www.notion.so/6416c20b3d3341539697ca0edbfb11ec)

## Purpose

This optional half-day module bridges Day 0 (Setup) and Week 1 (Python) for learners with **zero prior Python experience**. If you've never written Python before, complete this section before starting Day 1.

### Who should do this:

- You have never written or run a Python program
- You don't know what `def` or `import` means
- You're coming from pure statistics/math background with no programming experience
- You know R or MATLAB but have never touched Python

### Who can skip this:

- You've taken an intro Python course or tutorial
- You can write basic Python programs (variables, loops, functions)
- You're comfortable reading simple Python code
- You know another programming language well and just need Python-specific details (start with Day 1)

## Learning Objectives

By the end of Day 0.5, you will be able to:

- [ ] Run Python code interactively and from scripts
- [ ] Declare variables and understand Python's dynamic typing
- [ ] Write functions that take parameters and return values
- [ ] Use basic control flow (if/else, for loops, while loops)
- [ ] Work with lists and dictionaries
- [ ] Import and use modules
- [ ] Read Python error messages without panic

## Setup Verification

Before starting, verify your Python environment is working:

### Step 1: Check Python version

Open a terminal and run:
```bash
python --version
```

You should see Python 3.9 or higher. If not, revisit Day 0 setup instructions.

### Step 2: Run Python interactively

Type `python` in your terminal to start the interactive interpreter:
```python
>>> print("Hello from Python!")
Hello from Python!
>>> 2 + 2
4
>>> exit()
```

### Step 3: Run a Python script

Create a file named `hello.py`:
```python
print("Hello from a Python script!")
```

Run it:
```bash
python hello.py
```

If you see the output, your environment is ready.

## Core Concepts

See [python/concepts.md](python/concepts.md) for detailed explanations of:
- Variables and types
- Functions
- Control flow (if/elif/else, loops)
- Lists and dictionaries
- Importing modules
- Indentation as syntax

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Self-Assessment Checklist

Before proceeding to Day 1, verify you can:

- [ ] Run Python code both interactively and from scripts
- [ ] Declare variables and understand that types are inferred
- [ ] Write a function with parameters and a return value
- [ ] Use `if/elif/else` statements with proper indentation
- [ ] Write `for` loops that iterate over lists
- [ ] Create and access lists using 0-based indexing
- [ ] Create and access dictionaries using keys
- [ ] Import modules with `import` and `from ... import`
- [ ] Use f-strings to format output
- [ ] Read Python error messages and identify line numbers

**If you can complete this checklist, you're ready for Day 1.**

## Key Takeaways

1. Python uses dynamic typing - types are inferred, not declared
2. Indentation is part of the syntax (use 4 spaces)
3. Python is 0-indexed (unlike R and MATLAB which start at 1)
4. F-strings are the modern way to format output
5. Functions are defined with `def` and must be indented

## Additional Resources

If you need more help:
- [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney (Chapter 2-3)
- [Python for Everybody](https://www.py4e.com/) (Chapters 1-6)
- [Real Python tutorials](https://realpython.com/) (Start Here section)

## What You're NOT Learning Here

This primer covers only the bare minimum. You will NOT learn:

- NumPy arrays and vectorization → **Week 1, Days 2-3**
- Pandas dataframes → **Week 1, Day 4**
- Object-oriented programming (classes)
- List comprehensions and generators (briefly touched)
- File I/O and data loading
- Error handling (try/except)
- Advanced data structures

These topics are covered in Week 1, where you'll learn Python *for statistical computing specifically*. Day 0.5 just ensures you can read and write basic Python syntax.

## Estimated Time

- **Reading concepts:** 1.5 hours
- **Setup verification:** 20 min
- **Exercises:** 1-1.5 hours
- **Self-assessment:** 30 min
- **Total:** 3-4 hours

**If you spend more than 6 hours on Day 0.5**, you may benefit from a more comprehensive Python introduction before tackling this statistics-focused curriculum.

## Next Steps

Once you've completed the self-assessment checklist, proceed to [Week 1: Python (Days 1-7)](../../week1/day-01/README.md), starting with Day 1: Functions, Modules, and Idiomatic Python.
