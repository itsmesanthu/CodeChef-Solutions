# LPDPR32

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Identifying data types continued

We can check datatypes for individual columns and specific entries

```
print(df['A'].dtype)
print(type(df['A'][0]))

```

Columns with mixed data types are usually stored as 'object'

```
df['H'] = [1, 'two', 3.0]
print(df['H'].dtype)  # Will be 'object'

```

### Task

You are given a DataFrame.
Create a dictionary with column names as keys and their data types as values.
Output the dictionary to the console.

### Expected output

```
{'A': 'int64', 'B': 'float64', 'C': 'object', 'D': 'bool', 'E': 'datetime64[ns]', 'F': 'float64'}

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T10:33:06.264Z  

```py
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [1.0, 2.0, 3.0],
    'C': ['a', 'b', 'c'],
    'D': [True, False, True],
    'E': pd.date_range('20230101', periods=3),
    'F': [1, 2, None]
})

# Update your code below this line
column_types = df.dtypes.astype(str).to_dict()
print(column_types)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR32)