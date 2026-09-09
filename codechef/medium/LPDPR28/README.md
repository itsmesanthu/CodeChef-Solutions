# LPDPR28

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T14:55:59.408Z  

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

[View on CodeChef](https://www.codechef.com/problems/LPDPR28)