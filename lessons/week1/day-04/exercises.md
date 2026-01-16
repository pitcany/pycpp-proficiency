# Day 4: Pandas Pitfalls and Alternatives - Exercises

## Foundational Exercises

### Exercise 4.1: Fix the Chained Indexing

**Objective**: Identify and fix SettingWithCopyWarning issues.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A'],
    'value': [10, 20, 30, 40, 50],
    'flag': [True, False, True, False, True]
})

# Bug 1: This triggers SettingWithCopyWarning
df[df['category'] == 'A']['value'] = 100

# Bug 2: This also triggers the warning
subset = df[df['flag']]
subset['new_col'] = subset['value'] * 2

# TODO: Fix both bugs using .loc
```

---

### Exercise 4.2: Optimize the Loop

**Objective**: Replace iterrows with vectorized operations.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'x': np.random.randn(10000),
    'y': np.random.randn(10000)
})

# Slow version using iterrows
def compute_distances_slow(df):
    distances = []
    for idx, row in df.iterrows():
        dist = np.sqrt(row['x']**2 + row['y']**2)
        distances.append(dist)
    return pd.Series(distances)

# TODO: Implement fast vectorized version
def compute_distances_fast(df):
    pass

# Benchmark both
import time

start = time.time()
slow_result = compute_distances_slow(df)
print(f"Slow: {time.time() - start:.3f}s")

start = time.time()
fast_result = compute_distances_fast(df)
print(f"Fast: {time.time() - start:.3f}s")
```

---

## Proficiency Exercises

### Exercise 4.3: Convert to Polars

**Objective**: Rewrite a Pandas pipeline in Polars.

```python
import pandas as pd
import numpy as np

# Sample data
np.random.seed(42)
df_pandas = pd.DataFrame({
    'user_id': np.random.randint(1, 100, 10000),
    'amount': np.random.uniform(10, 1000, 10000),
    'category': np.random.choice(['food', 'transport', 'entertainment'], 10000),
    'date': pd.date_range('2024-01-01', periods=10000, freq='h')
})

# Pandas pipeline
result_pandas = (
    df_pandas
    .query("amount > 100")
    .assign(month=lambda x: x['date'].dt.month)
    .groupby(['user_id', 'category', 'month'])
    .agg(
        total_amount=('amount', 'sum'),
        transaction_count=('amount', 'count')
    )
    .reset_index()
    .query("transaction_count >= 3")
    .sort_values('total_amount', ascending=False)
)

# TODO: Convert to Polars
import polars as pl

df_polars = pl.from_pandas(df_pandas)

# result_polars = (
#     df_polars
#     ...
# )
```

---

### Exercise 4.4: Method Chaining Pipeline

**Objective**: Refactor imperative code into a clean method chain.

```python
import pandas as pd
import numpy as np

# Imperative style (messy)
def process_data_imperative(df):
    df = df.copy()
    df = df[df['value'] > 0]
    df['log_value'] = np.log(df['value'])
    df['normalized'] = (df['log_value'] - df['log_value'].mean()) / df['log_value'].std()
    grouped = df.groupby('category')
    result = grouped['normalized'].mean()
    result = result.reset_index()
    result.columns = ['category', 'avg_normalized']
    result = result.sort_values('avg_normalized', ascending=False)
    return result

# TODO: Rewrite as a single method chain
def process_data_chained(df):
    return (
        df
        # ... your chain here
    )
```

---

## Mastery Exercises

### Exercise 4.5: DuckDB for Large Data

**Objective**: Use DuckDB for SQL-like operations on large data.

```python
import duckdb
import pandas as pd
import numpy as np

# Create large dataset
n = 1_000_000
df = pd.DataFrame({
    'id': range(n),
    'category': np.random.choice(['A', 'B', 'C', 'D'], n),
    'value': np.random.randn(n),
    'timestamp': pd.date_range('2020-01-01', periods=n, freq='s')
})

# TODO: Use DuckDB to:
# 1. Filter rows where value > 1
# 2. Group by category and hour
# 3. Compute mean and count per group
# 4. Find top 10 groups by count

# result = duckdb.query("""
#     ...
# """).df()
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| No chained indexing | Uses chained indexing | Partial fix | All .loc/.iloc |
| Vectorization | Uses iterrows | Partial vectorization | Fully vectorized |
| Method chaining | Imperative style | Partial chains | Clean pipelines |
| Alternative libraries | Not attempted | Basic usage | Proficient usage |
