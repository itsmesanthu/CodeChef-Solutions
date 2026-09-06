# LPDPR05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Understanding Pandas Series Indexing

Series have attributes like index, values, and dtype.

Index and Datatype - this is something that we have seen in lists as well as NumPy arrays

```
s = pd.Series([10, 20, 30, 40, 50])
print(s[2])        # Output - 30
print(s.dtype)     # Output - int64

```

We can also use the custom labels for each element in the Series.

```
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s['c'])      # Output - 3

```

- Purpose: The index provides a label for each element in the Series, allowing you to access elements by these labels instead of just by their position.
- Structure: The index is a separate array-like object that runs parallel to the data in the Series. In this case, it's a list of strings: ['a', 'b', 'c', 'd', 'e'].
- Alignment and Access: Each label in the index corresponds to a value in the Series. So 'a' corresponds to 1, 'b' to 2, and so on.

Here's a visual representation of the Series:

```
Index | Value
------|------
  a   |   1
  b   |   2
  c   |   3
  d   |   4
  e   |   5

```

### Task

We have given you a series of student grades.
Output the scores for Bob and David to the console on separate lines using the index labels.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T11:47:45.422Z  

```py
import pandas as pd

grades = pd.Series([85, 90, 88, 92, 95], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
print(grades['Bob'])
print(grades['David'])
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR05)