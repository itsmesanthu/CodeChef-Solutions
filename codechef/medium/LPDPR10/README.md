# LPDPR10

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice problem

Let us solve a practice problem that combines your knowledge of Pandas series and Python.

### Task

You are given a Pandas series in the IDE. You need to modify the Series based on certain conditions.

Using the gradebook Series:

- Add 10 points all scores and output the series
- Cap the maximum score at 100 and output the series
- Create a new Pandas series - 'grade_summary' - which summarises the count of students in different score ranges.

Check the sample output below for further clarity on the expected solution.

### Sample 1:
Input
Output

```
 
```

```
Alice       75
Bob        102
Charlie     78
David       82
Eva         94
dtype: int64
Alice       75
Bob        100
Charlie     78
David       82
Eva         94
dtype: int64
<60         0
60 - 79     2
80 - 100    3
dtype: int64
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T05:09:50.447Z  

```py
import pandas as pd

grades = pd.Series([65, 92, 68, 72, 84], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])

# Update your code below this line
grades = grades + 10
print(grades)

grades[grades > 100] = 100
print(grades)

bins = [0, 59, 79, 100]
labels = ['<60', '60 - 79', '80 - 100']

categorised_grades = pd.cut(grades, bins=bins, labels=labels)
grade_summary = categorised_grades.value_counts().sort_index()
grade_summary = grade_summary.rename(None)
print(grade_summary)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR10)