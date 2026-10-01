# LPDPR49

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Multiple Aggregation using Dictionary

We can also perform multiple aggregations using a dictionary. Sample syntax as follows:

```
df.groupby('column').agg({'col1': 'mean', 'col2': ['sum', 'max']})

```

### Task

Let us take the previous sample data.

Perform multiple aggregations using a dictionary to get the following output

```
        Student Score    
          count   max min
Subject                  
Math          3    90  78
Science       3    95  88

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T16:15:21.283Z  

```py
import pandas as pd

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Score': [85, 90, 78, 92, 88, 95]
})

# Update your code below this line
output = df.groupby('Subject').agg({'Student': 'count', 'Score': ['max', 'min']})
print(output)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR49)