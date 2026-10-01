import pandas as pd

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Score': [85, 90, 78, 92, 88, 95]
})

# Update your code below this line
output = df.groupby('Subject').agg({'Student': 'count', 'Score': ['max', 'min']})
print(output)