# LPDPR31

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Identifying data types

The most straightforward way to check data types in a DataFrame is using the dtypes attribute.

```
print(df.dtypes)

```

For a more comprehensive overview, including non-null counts, we use the following syntax

```
df.info()

```

You can also use `select_dtypes()`

```
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
specific_columns = df.select_dtypes(include=['int64', 'object']).columns

```

- You can select multiple data types at once
- You can use both include and exclude to select certain datatypes

We have populated these examples in the IDE - run the code to check their output.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T16:05:29.120Z  

```py
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [1.0, 2.0, 3.0],
    'C': ['a', 'b', 'c'],
    'D': [True, False, True],
    'E': pd.date_range('20230101', periods=3),
    'F': [1, 2, None]
})

# Output datatypes of all columns
print(df.dtypes)

# Compehensive overview
print(df.info())

# Numeric columns
numeric_columns = df.select_dtypes(include=[np.number]).columns
print("Numeric columns:", numeric_columns)

# String (object) columns
string_columns = df.select_dtypes(include=['object']).columns
print("String columns:", string_columns)

# Boolean columns
bool_columns = df.select_dtypes(include=['bool']).columns
print("Boolean columns:", bool_columns)

# Datetime columns
date_columns = df.select_dtypes(include=['datetime']).columns
print("Datetime columns:", date_columns)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR31)