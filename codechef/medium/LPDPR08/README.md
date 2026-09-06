# LPDPR08

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Slicing series

Series can be indexed and sliced using labels or integer locations.

```
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s[1:4])
print(s['a':'d'])

```

gives us the following output

```
b    20
c    30
d    40
dtype: int64
a    10
b    20
c    30
d    40
dtype: int64

```

- Note: When you use label-based slicing, the behavior includes both the start and the end labels, which is more intuitive when working with labeled data, such as dates or strings.
### Task

You are given a series representing monthly sales data for a year. Output the following to the console

- Access the sales data for March and September
- Get the sales data for the first quarter (first three months)
- Find the months with sales greater than the yearly average
### Sample 1:
Input
Output

```
 
```

```
5100
5900
Jan    4000
Feb    4500
Mar    5100
dtype: int64
May    5800
Jun    6200
Jul    6500
Aug    6300
Sep    5900
Oct    5600
dtype: int64

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T12:13:23.741Z  

```py
import pandas as pd

monthly_sales = pd.Series([4000, 4500, 5100, 5400, 5800, 6200, 6500, 6300, 5900, 5600, 5200, 4800],
                          index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(monthly_sales['Mar'])
print(monthly_sales['Sep'])
print(monthly_sales[0:3])
yearly_average = monthly_sales.mean()
print(monthly_sales[monthly_sales > yearly_average])
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR08)