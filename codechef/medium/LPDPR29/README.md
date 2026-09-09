# LPDPR29

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T15:08:21.416Z  

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

[View on CodeChef](https://www.codechef.com/problems/LPDPR29)