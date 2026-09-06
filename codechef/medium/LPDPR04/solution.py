import pandas as pd
fruits =['apple', 'banana', 'cherry', 'date']
array = [0.5, 0.3, 0.8, 0.6]
f=pd.Series(fruits)
print(f)
a=pd.Series(array)
print(a)
aa=pd.Series(array,index=fruits)
print(aa)