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