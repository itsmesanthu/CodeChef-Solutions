# LPDPR04

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Creating Series

A Pandas Series is a one-dimensional array that can hold data of any type.

Series can be created from various data types including lists, numpy arrays, and dictionaries. Check the sample syntax below

```
# From list
s1 = pd.Series([1, 3, 5, 7, 9])

# From numpy array
s2 = pd.Series(np.array([1, 3, 5, 7, 9]))

# From dictionary
s3 = pd.Series({'a': 1, 'b': 3, 'c': 5})

```

### Task

Create 3 Pandas series and output them to the console

- List of fruits - 'apple', 'banana', 'cherry', 'date'
- NumPy array - [0.5, 0.3, 0.8, 0.6]
- Dictionary consisting of fruits and their corresponding prices - 'apple': 0.5, 'banana': 0.3, 'cherry': 0.8, 'date': 0.6
### Sample 1:
Input
Output

```
 
```

```
0     apple
1    banana
2    cherry
3      date
dtype: object
0    0.5
1    0.3
2    0.8
3    0.6
dtype: float64
apple     0.5
banana    0.3
cherry    0.8
date      0.6
dtype: float64
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T11:44:39.051Z  

```py
import pandas as pd
fruits =['apple', 'banana', 'cherry', 'date']
array = [0.5, 0.3, 0.8, 0.6]
f=pd.Series(fruits)
print(f)
a=pd.Series(array)
print(a)
aa=pd.Series(array,index=fruits)
print(aa)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR04)