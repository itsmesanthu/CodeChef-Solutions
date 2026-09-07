# LPDPR11

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Pandas DataFrame

A DataFrame is a 2-dimensional labeled data structure in Pandas. It can be thought of as a table or a spreadsheet-like structure where data is organized in rows and columns.

A common practical application for pandas DataFrames is in analyzing and manipulating structured data, such as sales records, financial data, or scientific observations.

We have populate the syntax for a dataframe creation in the IDE. Run the code to see the output.

### When to Use DataFrames vs Series

Use DataFrames when:

- You have multiple related columns of data (like in our sales example).
- You need to perform operations that involve multiple columns.
- You want to analyze relationships between different variables.
- You're working with structured, tabular data (like CSV files, SQL tables, or Excel sheets).

Use Series when:

- You're working with a single column of data.
- You need a one-dimensional array with labels.
- You're performing operations on a single variable.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T05:11:47.562Z  

```py
import pandas as pd

# Series: Single column of data (e.g., daily temperatures)
temperatures = pd.Series([20, 22, 23, 19, 21], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print("Temperature Series:")
print(temperatures)
print("\nAverage temperature:", temperatures.mean())

# DataFrame: Multiple related columns (e.g., weather data)
weather_data = pd.DataFrame({
    'Temperature': [20, 22, 23, 19, 21],
    'Humidity': [45, 47, 50, 43, 42],
    'WindSpeed': [10, 12, 8, 15, 11]
}, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])

print("\nWeather DataFrame:")
print(weather_data)
print("\nAverage conditions:")
print(weather_data.mean())
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR11)