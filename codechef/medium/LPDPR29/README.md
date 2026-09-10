# LPDPR29

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Filling Missing Data in Pandas

During data cleaning - while one option is to remove rows containing missing values - another is to fill missing data with values. Pandas provides several methods to fill missing data. Here are the main approaches:

```
# Fill all missing values with 0
df_filled = df.fillna(0)

# Fill different values for different columns
df_filled = df.fillna({'A': 0, 'B': 99, 'C': 'Unknown'})

# Forward fill - This method propagates the last valid observation forward to next missing value
df_ffilled = df.ffill()

# Backward fill - This method uses the next valid observation to fill the gap.
df_bfilled = df.bfill()

# You can fill missing values with statistical measures like mean, median, or mode.
df['A'].fillna(df['A'].mean(), inplace=True)
df['B'].fillna(df['B'].median(), inplace=True)

```

Important Considerations:

- Data Type: Ensure the fill value is compatible with the column's data type.
- Bias: Be aware that filling missing data can introduce bias into your dataset.
- Reason for Missingness: Consider why the data is missing before choosing a fill method.
- Impact on Analysis: Think about how the filled values might affect your subsequent analysis.
### Task

Perform the following operations on the given DataFrame.

- Replace null values based on given conditions to get the table as per the expected output below
- Forward fill only column B
- Create a function that fills missing values in numeric columns with the mean of the column and in string columns with 'Unknown'.
### Expected output

```
     A     B     C
0  1.0   5.0     a
1  2.0   NaN     b
2  NaN   NaN     c
3  4.0   NaN  None
4  5.0  10.0     e
     A     B        C
0  1.0   5.0        a
1  2.0  99.0        b
2  0.0  99.0        c
3  4.0  99.0  Unknown
4  5.0  10.0        e
     A     B     C
0  1.0   5.0     a
1  2.0   5.0     b
2  NaN   5.0     c
3  4.0   5.0  None
4  5.0  10.0     e
     A     B        C
0  1.0   5.0        a
1  2.0   7.5        b
2  3.0   7.5        c
3  4.0   7.5  Unknown
4  5.0  10.0        e

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T08:50:12.109Z  

```py
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, None, 10],
    'C': ['a', 'b', 'c', None, 'e']
})
                   
print(df)  

# Replace null values based on given conditions
print(df.fillna({'A':0,'B':99,'C':"Unknown"}))


# Forward fill column B
df_forward = df.copy()
df_forward['B'] = df_forward['B'].ffill()
print(df_forward)


# Fills missing values in numeric columns with the mean of the column and in string columns with 'Unknown'.
def fill_missing_values(df):
    df=df.copy()
    for i in df.columns:
        if pd.api.types.is_numeric_dtype(df[i]):
            df[i]=df[i].fillna(df[i].mean())
        else:
            df[i]=df[i].fillna('Unknown')
    return df
res=fill_missing_values(df)
print(res)


```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR29)