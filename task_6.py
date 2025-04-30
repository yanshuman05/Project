import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-02-01', '2022-02-02', '2022-02-03',
             '2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-02', '2023-02-03'],
    'Sales': [100, 120, 110, 130, 140, 125, 150, 160, 155, 170, 180, 175]
}

df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract year and month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Aggregate sales by year and month
sales_trend = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

# Plot sales trend
plt.figure(figsize=(10,6))
for year in sales_trend['Year'].unique():
    year_data = sales_trend[sales_trend['Year'] == year]
    plt.plot(year_data['Month'], year_data['Sales'], label=year)

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Trend Analysis')
plt.legend()
plt.show()


