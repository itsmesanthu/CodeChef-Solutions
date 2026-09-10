import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, None, 10],
    'C': ['a', 'b', 'c', None, 'e']
})
                   
print(df)  

# Replace null values based on given conditions
print(df.fillna({'A':0,'B':99,'C':"Unknown"}))


# Forward fill column B
df_forward = df.copy()
df_forward['B'] = df_forward['B'].ffill()
print(df_forward)


# Fills missing values in numeric columns with the mean of the column and in string columns with 'Unknown'.
def fill_missing_values(df):
    df=df.copy()
    for i in df.columns:
        if pd.api.types.is_numeric_dtype(df[i]):
            df[i]=df[i].fillna(df[i].mean())
        else:
            df[i]=df[i].fillna('Unknown')
    return df
res=fill_missing_values(df)
print(res)

