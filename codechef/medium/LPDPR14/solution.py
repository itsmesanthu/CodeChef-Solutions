import pandas as pd

# Case 1: All keys are common
data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

df = pd.DataFrame(data)
print('Common keys:\n', df)

# Case 2: Missing keys
data1 = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30},  # Missing 'city'
    {'name': 'Charlie', 'city': 'Los Angeles'}  # Missing 'age'
]

df1 = pd.DataFrame(data1)
print('Missing keys:\n', df1)

# Case 3: Extra keys
data2 = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco', 'salary': 75000},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles', 'department': 'Sales'}
]

df2 = pd.DataFrame(data2)
print('Extra keys:\n',df2)
