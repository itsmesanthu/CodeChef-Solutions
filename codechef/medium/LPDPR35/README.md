# LPDPR35

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Date and Time Conversion in Pandas

The primary function for converting to datetime is pd.to_datetime()

```
# Converting a series of strings
df = pd.DataFrame({'date': ['2023-07-15', '2023-07-16', '2023-07-17']})
df['date'] = pd.to_datetime(df['date'])

```

Pandas can automatically parse many date formats, but you can specify the format for ambiguous cases

```
# American format (month/day/year)
date = pd.to_datetime('7/15/2023', format='%m/%d/%Y')

# Custom format
date = pd.to_datetime('15-Jul-2023', format='%d-%b-%Y')

```

To handle invalid dates / datatype - you can use coerce in the following manner

```
dates = ['2023-07-15', 'Invalid Date', '2023-07-17']
pd.to_datetime(dates, errors='coerce')  # 'Invalid Date' becomes NaT (Not a Time)

```

You can also handle time-zones in the following manner

```
date = pd.to_datetime('2023-07-15 12:00:00')
date_tz = date.tz_localize('UTC').tz_convert('US/Eastern')

```

### Task

You are given a DataFrame - your task is to process this data using pandas and perform the following operations. Output the updated DataFrame after each operation.

- Convert the 'order_date' column to datetime format. Handle any invalid dates in the 'order_date' column by replacing them with NaT (Not a Time).
- Create a new column 'formatted_date' that displays the date in the format: "DD-Mon-YYYY" (e.g., "15-Mar-2023").
### Expected outpu

```
   order_id    order_date  total_amount
0         1    2023-03-15        100.50
1         2    2023-04-01        200.75
2         3  invalid_date        150.25
3         4    2023-03-20        300.00
4         5    2023-04-05         75.80
   order_id order_date  total_amount
0         1 2023-03-15        100.50
1         2 2023-04-01        200.75
2         3        NaT        150.25
3         4 2023-03-20        300.00
4         5 2023-04-05         75.80
   order_id order_date  total_amount formatted_date
0         1 2023-03-15        100.50    15-Mar-2023
1         2 2023-04-01        200.75    01-Apr-2023
2         3        NaT        150.25            NaN
3         4 2023-03-20        300.00    20-Mar-2023
4         5 2023-04-05         75.80    05-Apr-2023

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T13:19:43.393Z  

```py
import pandas as pd

sample_data = {
    'order_id': [1, 2, 3, 4, 5],
    'order_date': ['2023-03-15', '2023-04-01', 'invalid_date', '2023-03-20', '2023-04-05'],
    'total_amount': [100.50, 200.75, 150.25, 300.00, 75.80]
}
df = pd.DataFrame(sample_data)
print(df)
df['order_date']=pd.to_datetime(df['order_date'],errors='coerce')
print(df)
df['formatted_date'] = df['order_date'].dt.strftime('%d-%b-%Y')
print(df)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPDPR35)