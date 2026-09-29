# LPDPR47

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### GroupBy Multiple Columns

Grouping by multiple columns allows you to create more specific subgroups within your data. For example, you might want to group sales data by both product category and region, or analyze student performance by both grade level and subject.

We have populated an example in the IDE which gives us the average performance score by department and job level. Run the code to see how grouping by multiple columns works

### Task

Update the code in the IDE to perform the following operation

- Calculate the total salary for each Job Level-Department combination.
### Expected output

```
Job_Level  Department 
Junior     Engineering    6548566
           HR             8357975
           Marketing      8332198
           Sales          7594099
Manager    Engineering    7292836
           HR             7101794
           Marketing      7041657
           Sales          8540204
Senior     Engineering    8782303
           HR             7082253
           Marketing      7698620
           Sales          7090670
Name: Salary, dtype: int64

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T16:05:34.407Z  

```py
import pandas as pd
import numpy as np

# Create sample employee data
np.random.seed(0)
departments = ['Sales', 'Marketing', 'Engineering', 'HR']
job_levels = ['Junior', 'Senior', 'Manager']
employees = 1000

data = {
    'Employee_ID': range(1, employees + 1),
    'Department': np.random.choice(departments, employees),
    'Job_Level': np.random.choice(job_levels, employees),
    'Years_of_Experience': np.random.randint(1, 20, employees),
    'Performance_Score': np.random.uniform(60, 100, employees),
    'Salary': np.random.randint(30000, 150000, employees)
}

df = pd.DataFrame(data)

# Basic grouping by multiple columns
avg_performance = df.groupby(['Department', 'Job_Level'])['Performance_Score'].mean()
print(avg_performance)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR47)