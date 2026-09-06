import pandas as pd

monthly_sales = pd.Series([4000, 4500, 5100, 5400, 5800, 6200, 6500, 6300, 5900, 5600, 5200, 4800],
                          index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(monthly_sales['Mar'])
print(monthly_sales['Sep'])
print(monthly_sales[0:3])
yearly_average = monthly_sales.mean()
print(monthly_sales[monthly_sales > yearly_average])