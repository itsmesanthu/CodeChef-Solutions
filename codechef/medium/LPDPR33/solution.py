import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': [1.1, 2.2, 3.3],
    'C': [1, 2, 3]
})
print("Datatype before change:\n", df.dtypes)

df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)
df['C'] = df['C'].astype(np.int32)
print("Datatype after change:\n", df.dtypes)

df1 = pd.DataFrame({
    'D': ['1', '2', 'three', '4'],
    'E': ['1.1', '2.2', 'NaN', '4.4']
})

df1['D'] = pd.to_numeric(df1['D'], errors='coerce')
df1['E'] = pd.to_numeric(df1['E'], errors='coerce')

# Notice that three has converted to NaN
print(df1)
