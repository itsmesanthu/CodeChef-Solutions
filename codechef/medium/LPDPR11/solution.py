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