# LPDPR14

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Create DataFrames from List of dictionaries

In the previous problem, we created a DataFrame from a list of lists.

DataFrames can also be created from a list of dictionaries.

```
data_dict_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]
df_from_dict_list = pd.DataFrame(data_dict_list)

```

Note here that the key values are the same.

- Common keys: If all dictionaries have the same keys, the resulting DataFrame will have columns for all these keys.
- Missing keys: If some dictionaries are missing certain keys, pandas will fill those cells with NaN (Not a Number) values.
- Extra Keys: If some dictionaries have extra keys not present in others, pandas will create columns for these keys and fill with NaN where the key is missing.

We have populated these conditions in the IDE - run the code to see the expected output for each case.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T05:21:55.192Z  

```py
import pandas as pd

# Case 1: All keys are common
data = [
    {'name': 'Alice', 'age': 25, 'cIty': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

df = pd.DataFrame(data)
print('Common keys:\n', df)

# Case 2: Missing keys
data1 = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30},  # Missing 'city'
    {'name': 'Charlie', 'city': 'Los Angeles'}  # Missing 'age'
]

df1 = pd.DataFrame(data1)
print('Missing keys:\n', df1)

# Case 3: Extra keys
data2 = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco', 'salary': 75000},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles', 'department': 'Sales'}
]

df2 = pd.DataFrame(data2)
print('Extra keys:\n',df2)

```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR14)