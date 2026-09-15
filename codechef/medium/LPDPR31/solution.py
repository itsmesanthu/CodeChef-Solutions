import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [1.0, 2.0, 3.0],
    'C': ['a', 'b', 'c'],
    'D': [True, False, True],
    'E': pd.date_range('20230101', periods=3),
    'F': [1, 2, None]
})

# Output datatypes of all columns
print(df.dtypes)

# Compehensive overview
print(df.info())

# Numeric columns
numeric_columns = df.select_dtypes(include=[np.number]).columns
print("Numeric columns:", numeric_columns)

# String (object) columns
string_columns = df.select_dtypes(include=['object']).columns
print("String columns:", string_columns)

# Boolean columns
bool_columns = df.select_dtypes(include=['bool']).columns
print("Boolean columns:", bool_columns)

# Datetime columns
date_columns = df.select_dtypes(include=['datetime']).columns
print("Datetime columns:", date_columns)