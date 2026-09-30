# LPDPR48

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Multiple Aggregation using a List

Once data is grouped - we can apply multiple aggregation functions to grouped data using the agg() method. Multiple aggregations allow you to apply several aggregation functions to one or more columns simultaneously. This is particularly useful when you need different summary statistics for different aspects of your data.

The most common method to perform multiple aggregations is using the agg() method with a list of functions:

```
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
})

# Multiple aggregations
result = df.groupby('Category').agg({
    'Value': ['mean', 'min', 'max']
})

```

gives us the output

```
         Value        
          mean min max
Category              
A         30.0  10  50
B         40.0  20  60

```

### Task

Using the student score DataFrame given in the IDE, calculate the minimum, maximum, and average score for each subject.

### Expected output

```
        Score               
          min max       mean
Subject                     
Math       78  90  84.333333
Science    88  95  91.666667

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T15:14:47.450Z  

```py
import pandas as pd

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Score': [85, 90, 78, 92, 88, 95]
})

# Update your code below this line

result = df.groupby('Subject').agg({
    'Score': ['min', 'max', 'mean']
})

print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR48)