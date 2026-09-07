# LPDPR12

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Create DataFrames from dictionary

DataFrames can be created from dictionaries where keys become column names and values become data in those columns.

```
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data_dict)
print(df)

```

### Task

Create a DataFrame from a dictionary that represents weather data for a week, including columns for 'Day', 'Temperature', and 'Condition'.

Output the dataframe to the console.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T05:17:02.133Z  

```py
import pandas as pd

weather_data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature': [72, 75, 70, 68, 74],
    'Condition': ['Sunny', 'Partly Cloudy', 'Rainy', 'Cloudy', 'Sunny']
}

# Update your code below this line
df=pd.DataFrame(weather_data)
print(df)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR12)