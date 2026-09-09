# LPDPR28

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Dropping missing data

Pandas provides several methods to drop missing data, primarily through the dropna() function.
Remember, dropna() treats both None and NaN as missing values.

Here are the main approaches:

```
# Drop rows with any missing values
df_clean = df.dropna()

# Drop rows only if all values are missing
df_clean = df.dropna(how='all')

# Drop rows with less than 2 non-null values
df_clean = df.dropna(thresh=2)

# Drop rows where column 'A' has missing values
df_clean = df.dropna(subset=['A'])

# Drop rows where either 'A' or 'B' is missing
df_clean = df.dropna(subset=['A', 'B'], how='any')

```

Note:

- The dropna(thresh=n) method in pandas drops rows that have fewer than n non-null values
- df_clean = df.dropna(subset=['A', 'B']) will drop rows where either 'A' OR 'B' (or both) have missing values.
- df_clean = df.dropna(subset=['A', 'B'], how='all') drops rows only if ALL specified columns are null.
- Remember, dropna(subset=[...]) focuses on specific columns, ignoring the status of other columns not mentioned in the subset.
### Task

You are given a DataFrame. Perform the following operations. Check the expected output below

- Drop rows where column A has missing values
- Drop rows with less than 2 non-null values
- Drop rows where both Column A and Column B has missing values
### Expected output

```
     A     B     C
0  1.0   5.0     a
1  2.0   NaN     b
2  NaN   NaN     c
3  4.0   NaN  None
4  5.0  10.0     e
     A     B     C
0  1.0   5.0     a
1  2.0   NaN     b
3  4.0   NaN  None
4  5.0  10.0     e
     A     B  C
0  1.0   5.0  a
1  2.0   NaN  b
4  5.0  10.0  e
     A     B     C
0  1.0   5.0     a
1  2.0   NaN     b
3  4.0   NaN  None
4  5.0  10.0     e

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T15:08:11.816Z  

```py
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, None, 10],
    'C': ['a', 'b', 'c', None, 'e']
})
                   
print(df)  

# Drop rows where column A has missing values
print(df.dropna(subset=['A']))

# Drop rows with less than 2 non-null values
print(df.dropna(thresh=2))

# Drop rows where both Column A and Column B has missing values

print(df.dropna(subset=['A','B'], how='all'))

```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR28)