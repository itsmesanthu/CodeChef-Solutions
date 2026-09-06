# LPDPR03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Pandas vs NumPy

 **Scenario 1** : You're analyzing the daily temperatures of a city for a month. You want to calculate the average temperature and convert all temperatures from Celsius to Fahrenheit.

NumPy is ideal for this task because:

- We're working with a simple numerical array.
- We need to perform element-wise mathematical operations.
- We don't need labeled data or complex data structures.

 **Scenario 2** : You have sales data for different products over a week. You want to calculate the total sales for each product and find the best-selling product.

Pandas is better for this task because:

- We're working with structured data (products and their daily sales).
- We need to perform analysis on labeled data.
- We want to easily access and manipulate data by column names or indices.

You can check out the code implementation in the IDE for both the scenarios above. Over the course of the next few topics, we will learn how to implement Pandas.

If you want to go ahead and learn / revise NumPy - you can check out our learning path on NumPy here

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T11:37:52.090Z  

```py
import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, 7, 9])

# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


print("Series:", s)
print("\nDataFrame:", df)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR03)