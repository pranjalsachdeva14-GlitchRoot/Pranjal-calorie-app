import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("weather_data.csv")

# Convert date column
data['date'] = pd.to_datetime(data['date'])

# Handle missing values
data = data.fillna(data.mean())

# DAILY statistics
daily_mean = data[['temperature', 'rainfall', 'humidity']].mean()

# MONTHLY statistics
monthly = data.resample('M', on='date').mean()

# PLOTS --------------------------------------------------------

# 1. Line chart – Temperature trend
plt.figure(figsize=(10,5))
plt.plot(data['date'], data['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.savefig("temperature_trend.png")
plt.show()

# 2. Bar chart – Monthly Rainfall
plt.figure(figsize=(8,5))
plt.bar(monthly.index.strftime('%Y-%m'), monthly['rainfall'])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid()
plt.savefig("monthly_rainfall.png")
plt.show()

# 3. Scatter plot – Humidity vs Temperature
plt.figure(figsize=(8,5))
plt.scatter(data['temperature'], data['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.grid()
plt.savefig("humidity_vs_temperature.png")
plt.show()

# 4. Combined Subplot
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(data['date'], data['temperature'])
plt.title("Temperature")

plt.subplot(1,2,2)
plt.plot(data['date'], data['humidity'], color='orange')
plt.title("Humidity")

plt.tight_layout()
plt.savefig("combined_plot.png")
plt.show()

# Export cleaned file
data.to_csv("cleaned_weather_data.csv", index=False)
