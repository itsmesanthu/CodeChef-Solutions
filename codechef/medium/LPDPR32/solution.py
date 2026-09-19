import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [1.0, 2.0, 3.0],
    'C': ['a', 'b', 'c'],
    'D': [True, False, True],
    'E': pd.date_range('20230101', periods=3),
    'F': [1, 2, None]
})

# Update your code below this line
column_types = df.dtypes.astype(str).to_dict()
print(column_types)