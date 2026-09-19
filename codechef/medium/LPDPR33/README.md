# LPDPR33

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Converting numeric datatypes

The most straightforward method to convert from other datatypes to numeric is using astype().

pd.to_numeric() provides more control over error handling with options for errors:

- 'raise': Raise an exception on invalid data (default)
- 'coerce': Convert invalid data to NaN
- 'ignore': Leave invalid data as is

Multiple columns can be converted using pd.to_numeric() as follows:

```
df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': [1.1, 2.2, 3.3],
    'C': [1, 2, 3]
})

df[['A', 'B', 'C']] = df[['A', 'B', 'C']].apply(pd.to_numeric, errors='coerce')

```

Note: To select multiple columns, you need to use a list of column names

Run the code given in the IDE to see how datatype conversion works.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T10:35:33.249Z  

```py
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': [1.1, 2.2, 3.3],
    'C': [1, 2, 3]
})
print("Datatype before change:\n", df.dtypes)

df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)
df['C'] = df['C'].astype(np.int32)
print("Datatype after change:\n", df.dtypes)

df1 = pd.DataFrame({
    'D': ['1', '2', 'three', '4'],
    'E': ['1.1', '2.2', 'NaN', '4.4']
})

df1['D'] = pd.to_numeric(df1['D'], errors='coerce')
df1['E'] = pd.to_numeric(df1['E'], errors='coerce')

# Notice that three has converted to NaN
print(df1)

```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR33)