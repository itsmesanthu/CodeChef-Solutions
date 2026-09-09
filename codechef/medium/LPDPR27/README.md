# LPDPR27

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Identifying Missing Data

In pandas, missing data can be represented in several ways:

- None: This is a Python singleton object used to represent the absence of a value.
- NaN (Not a Number): This is a special floating-point value defined by the IEEE 754 standard.
- NaT (Not a Time): This is used for missing datetime values.

Pandas treats None, NaN, and NaT as missing in most operations. We use isnull() or isna() to check for missing values:

```
df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': ['a', 'b', 'c', None]})

print(df.isnull())  # Boolean mask of missing values
print(df.isnull().sum())  # Count of missing values per column

```

Gives us the output

```
       A      B      C
0  False  False  False
1  False   True  False
2   True   True  False
3  False  False   True
A    1
B    2
C    1
dtype: int64

```

### Task

Create a function that takes a DataFrame as input and returns the percentage of missing values in each column.

### Sample 1:
Input
Output

```
 
```

```
A    25.0
B    50.0
C    25.0
dtype: float64
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T14:55:55.382Z  

```py
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': ['a', 'b', 'c', None]})
                   
# Update your code below this line
print(df.isnull().sum()/len(df)*100)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR27)