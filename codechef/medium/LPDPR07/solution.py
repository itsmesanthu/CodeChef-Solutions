import pandas as pd

temperatures = pd.Series([20, 22, 25, 23, 21, 19, 24], 
                         index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

print(temperatures)
print(temperatures-22)