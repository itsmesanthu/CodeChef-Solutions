# LPDPR46

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### GroupBy Operation

The GroupBy operation in Pandas is a powerful tool that allows you to split your data into separate groups based on some criteria, apply a function to each group independently, and then combine the results. This operation is inspired by the SQL GROUP BY clause and is fundamental to data aggregation and analysis.

Key Components of GroupBy

- Split: The data is divided into groups based on one or more keys.
- Apply: A function is applied to each group independently.
- Combine: The results are combined into a new data structure.

Common GroupBy Methods

- group.mean(): Calculate mean of each group
- group.sum(): Calculate sum of each group
- group.size(): Count the number of items in each group
- group.count(): Count non-NA/null values in each group
- group.min(), group.max(): Find minimum and maximum values in each group
- group.agg(): Apply multiple aggregation functions at once

We have populate a practical example in the IDE to show how GroupBy works. Go ahead and review the code.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T16:46:40.732Z  

```py
import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value1': [10, 20, 30, 40, 50, 60],
    'Value2': [100, 200, 300, 400, 500, 600]
})

# Basic groupby and aggregation
print("Mean of Value1 for each Category:")
print(df.groupby('Category')['Value1'].mean())

print("Max of Value2 for each Category:")
print(df.groupby('Category')['Value2'].max())

print("Sum of Value1 for each Category:")
print(df.groupby('Category')['Value1'].sum())


```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR46)