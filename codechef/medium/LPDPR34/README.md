# LPDPR34

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Converting numeric datatypes

Categorical data in pandas is used for

- Memory efficiency, especially for strings with repeated values
- Improved performance for certain operations
- Meaningful representation of non-numeric data with a specific set of possible values

The memory efficiency of categorical data in pandas stems from its internal representation. Categorical data in pandas is represented internally using two main components:

- Categories Array: A unique array of all possible category values.
- Codes Array: An integer array where each integer is an index pointing to a value in the categories array.

Let's consider a column with 1 million rows, containing only the values 'Apple', 'Banana', and 'Cherry'.

- Without Categorical: Each string is stored separately. Memory usage ≈ (5 + 6 + 6) bytes * 1,000,000 ≈ 17 MB (Assuming each character takes 1 byte and accounting for Python's string overhead)
- With Categorical: Categories Array: ['Apple', 'Banana', 'Cherry'] ≈ 17 bytes Codes Array: 1,000,000 integers (1 byte each if using uint8) ≈ 1 MB Total: ≈ 1 MB

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T13:00:34.645Z  

```py
import pandas as pd
import numpy as np

# Generating the data
n = 1_000_000
data = np.random.choice(['Apple', 'Banana', 'Cherry'], size=n)

# Without Categorical
df = pd.DataFrame({'Fruit': data})
print("Memory usage without Categorical:")
print(df.memory_usage(deep=True))

# With Categorical
df['Fruit'] = df['Fruit'].astype('category')
print("\nMemory usage with Categorical:")
print(df.memory_usage(deep=True))

```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR34)