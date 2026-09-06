import pandas as pd

grades = pd.Series([85, 90, 88, 92, 95], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
print(grades['Bob'])
print(grades['David'])