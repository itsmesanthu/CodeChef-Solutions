# LPDPR13

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Create DataFrames from Lists

DataFrames can also be created from lists of lists or list of dictionaries.

DataFrames created from lists:

```
data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
]
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])

```

Note:

- The list of lists: Each inner list represents a row of data.
- The columns parameter: Used to specify column names. If not provided, pandas will use default numeric indices (0, 1, 2,...).

DataFrames created from lists with custom index for each row

```
data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'], index=['ID1', 'ID2', 'ID3'])

```

### Task

We have created a DataFrame from a list of lists representing a small gradebook with columns for 'Student', 'Subject', and 'Grade'.
Update the code in the IDE to rename the rows with the updated index values provided in the Output below.

### Sample 1:
Input
Output

```
 
```

```
     Student  Subject  Grade
ID1    Alice     Math     95
ID2      Bob     Math     87
ID3  Charlie     Math     91
ID4    Alice  Science     92
ID5      Bob  Science     88
ID6  Charlie  Science     94
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T05:19:18.211Z  

```py
import pandas as pd

gradebook_data = [
    ['Alice', 'Math', 95],
    ['Bob', 'Math', 87],
    ['Charlie', 'Math', 91],
    ['Alice', 'Science', 92],
    ['Bob', 'Science', 88],
    ['Charlie', 'Science', 94]
]

# Update your code below
gradebook_df = pd.DataFrame(gradebook_data, columns=['Student', 'Subject', 'Grade'],index=['ID1','ID2','ID3','ID4','ID5','ID6'])
print(gradebook_df)

```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR13)