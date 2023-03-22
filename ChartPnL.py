import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df= pd.read_csv('log.csv', delimiter=';')
# Filter the DataFrame to only include data for a specific timestamp and product
# timestamp = '100' # Change this to the desired timestamp
product = 'PEARLS' # Change this to the desired product


# window_size = 10000
# df['moving_avg'] = df['ask_price_1'].rolling(window_size).mean()
df['cumulative_sum'] = df['profit_and_loss'].cumsum()
plt.plot(df['timestamp'], df['profit_and_loss'])


plt.show()
