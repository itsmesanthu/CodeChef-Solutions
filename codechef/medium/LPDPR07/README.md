# LPDPR07

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice problem

You are given a Series of daily temperatures for a week.

### Task

Calculate and print the following

- The temperature increase if each day was 2 degrees warmer
- The weekly average temperature
- The difference between each day's temperature and the weekly average

Check the expected output below for further clarity.

### Sample 1:
Input
Output

```
 
```

```
Mon    22
Tue    24
Wed    27
Thu    25
Fri    23
Sat    21
Sun    26
dtype: int64
22.0
Mon   -2.0
Tue    0.0
Wed    3.0
Thu    1.0
Fri   -1.0
Sat   -3.0
Sun    2.0
dtype: float64
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T12:06:50.763Z  

```py
import pandas as pd

temperatures = pd.Series([20, 22, 25, 23, 21, 19, 24], 
                         index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

print(temperatures)
print(temperatures-22)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR07)