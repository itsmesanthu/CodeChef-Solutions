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