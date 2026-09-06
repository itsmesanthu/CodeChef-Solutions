# LPDPR09

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Customise the index

Let us create a custom index list based on our Python knowledge and incorporate it into our Pandas series.

### Task

Create and print the series representing a gradebook for a class of 5 students.
The code in the IDE already contains the scores for the 5 students as a Pandas series.
Can you think of a way to create the Index list?

The output of the series is given below.

### Sample 1:
Input
Output

```
 
```

```
Student_1    85
Student_2    90
Student_3    88
Student_4    92
Student_5    95
dtype: int64
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T12:15:21.606Z  

```py
import pandas as pd

# update the code below
students = ['Student_1',"Student_2","Student_3","Student_4","Student_5"]

grades = pd.Series([85, 90, 88, 92, 95],index=students )

print(grades)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR09)