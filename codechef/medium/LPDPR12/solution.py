import pandas as pd

weather_data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature': [72, 75, 70, 68, 74],
    'Condition': ['Sunny', 'Partly Cloudy', 'Rainy', 'Cloudy', 'Sunny']
}

# Update your code below this line
df=pd.DataFrame(weather_data)
print(df)