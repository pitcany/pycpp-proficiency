# Day 4: Pandas Pitfalls and Alternatives

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/6789a15b62cd43308c455bff90dd58c5)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Avoid chained indexing and SettingWithCopyWarning
- [ ] Use `.loc`, `.iloc`, and `.query()` correctly
- [ ] Recognize when Pandas is slow
- [ ] Apply Polars or DuckDB for large datasets
- [ ] Write transformation pipelines using method chaining

## Sections

### Indexing Done Right

Correct Pandas indexing patterns:
```python
# BAD: Chained indexing
df[df['a'] > 0]['b'] = 5  # SettingWithCopyWarning!

# GOOD: Single .loc call
df.loc[df['a'] > 0, 'b'] = 5
```

Key methods:
- `.loc[]`: Label-based indexing
- `.iloc[]`: Integer-based indexing
- `.at[]`, `.iat[]`: Scalar access (fast)
- `.query()`: SQL-like filtering

### Performance Pitfalls

Common Pandas antipatterns:
1. Iterating with `iterrows()` (use vectorized operations)
2. Growing DataFrames row by row (preallocate or concat once)
3. String operations on object dtype (use StringDtype)
4. Unnecessary copies from chained operations

### Method Chaining

Clean, readable transformations:
```python
result = (
    df
    .query("age > 18")
    .assign(age_group=lambda x: pd.cut(x['age'], bins=[18, 30, 50, 100]))
    .groupby('age_group')
    .agg({'income': 'mean'})
    .reset_index()
)
```

### Alternatives to Pandas (Polars, DuckDB)

When to consider alternatives:
- Large datasets (> 1GB)
- Need for lazy evaluation
- SQL-like operations

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Always use `.loc` or `.iloc`, never chained indexing
2. Avoid `iterrows()` - use vectorized operations
3. Method chaining makes pipelines readable
4. Consider Polars/DuckDB for large data

## Next Steps

Proceed to [Day 5: Testable, Reusable Code](../day-05/README.md).
