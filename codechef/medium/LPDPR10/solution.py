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