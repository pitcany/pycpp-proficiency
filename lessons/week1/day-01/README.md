# Day 1: Functions, Modules, and Idiomatic Python

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/ff5ab5e0e9e747e5b66b030e825a109d)

> **Note for absolute beginners**: If you have never written Python before, complete [Day 0.5: Python Primer](../../foundations/python-primer/README.md) before starting this lesson.

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Write functions with explicit type hints and docstrings
- [ ] Organize code into importable modules
- [ ] Use context managers (with statements) for resource management
- [ ] Apply list/dict comprehensions and generator expressions idiomatically
- [ ] Understand when to use *args, **kwargs, and default arguments

## Sections

### Function Design

Writing clean, well-documented functions:
- Type hints for parameters and return values
- Docstrings following NumPy or Google style
- Single responsibility principle
- Pure functions vs functions with side effects

### Module Organization

Structuring Python code for reusability:
- `__init__.py` and package structure
- Relative vs absolute imports
- `if __name__ == "__main__":` pattern
- Avoiding circular imports

### Context Managers

Resource management with `with` statements:
- File handling
- Database connections
- Custom context managers with `__enter__` and `__exit__`
- `contextlib.contextmanager` decorator

### Comprehensions and Generators

Pythonic iteration patterns:
- List comprehensions vs map/filter
- Dictionary and set comprehensions
- Generator expressions for memory efficiency
- When to use generators vs lists

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Always use type hints for function signatures
2. Prefer context managers for resource cleanup
3. Use comprehensions for simple transformations
4. Use generators for large data streams

## Next Steps

Proceed to [Day 2: Memory Model, Views, and Copies](../day-02/README.md).
