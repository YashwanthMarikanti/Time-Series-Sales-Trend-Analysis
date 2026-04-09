import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('sales_data.csv')

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])

# Sort values
data = data.sort_values('Date')

# Set index
data.set_index('Date', inplace=True)

print(data.head())

# Plot
plt.figure(figsize=(10,5))
plt.plot(data['Sales'])
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Moving average
data['Moving_Avg'] = data['Sales'].rolling(window=3).mean()

plt.figure(figsize=(10,5))
plt.plot(data['Sales'], label='Original')
plt.plot(data['Moving_Avg'], label='Moving Average')
plt.legend()
plt.show()

print(data.describe())
