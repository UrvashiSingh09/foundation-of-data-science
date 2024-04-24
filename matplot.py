# import matplotlib.pyplot as plt

# # Read data from the text file
# with open('test.txt', 'r') as file:
#     data = file.readlines()

# # Extract x and y values
# x = [float(line.split()[0]) for line in data]
# y = [float(line.split()[1]) for line in data]

# # Plot the line
# plt.plot(x, y)

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')

# # Show the plot
# plt.grid(True)
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# # Read the CSV file
# df = pd.read_csv('fdata.csv')

# # Filter data for the specified date range
# start_date = '10-03-16'
# end_date = '10-07-16'
# filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# # Extract relevant data
# dates = filtered_df['Date']
# close_prices = filtered_df['Close']

# # Plot the line chart
# plt.figure(figsize=(10, 6))
# plt.plot(dates, close_prices, marker='o', linestyle='-')
# plt.title('Alphabet Inc. Close Prices (Oct 3 - Oct 7, 2016)')
# plt.xlabel('Date')
# plt.ylabel('Close Price')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()

# # Show the plot
# plt.show()

# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Plot the data
# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sample Plot')

# # Get current axis limits
# xlim = plt.xlim()
# ylim = plt.ylim()
# print("Current X-axis limits:", xlim)
# print("Current Y-axis limits:", ylim)

# # Set new axis values
# plt.xlim(0, 6)
# plt.ylim(0, 12)

# # Show the plot
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define x values
x = np.linspace(0, 10, 100)

# Define y values for each line
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Plot multiple lines with different format styles in one command
plt.plot(x, y1, '-r', label='sin(x)')
plt.plot(x, y2, '--g', label='cos(x)')
plt.plot(x, y3, ':b', label='sin(x)*cos(x)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines with Different Format Styles')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

