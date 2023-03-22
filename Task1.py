import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df_2 = pd.read_csv('island-data-bottle-round-1/prices_round_1_day_-2.csv', delimiter=';')
df_1 = pd.read_csv('island-data-bottle-round-1/prices_round_1_day_-1.csv', delimiter=';')
df0 = pd.read_csv('island-data-bottle-round-1/prices_round_1_day_0.csv', delimiter=';')
df_1['timestamp'] = df_1['timestamp'] + 1000000
df0['timestamp'] = df0['timestamp'] + 2000000
# Filter the DataFrame to only include data for a specific timestamp and product
# timestamp = '100' # Change this to the desired timestamp
product = 'PEARLS' # Change this to the desired product
df = pd.concat([df_2, df_1, df0], ignore_index=True)
df = df[df['product'] == product]


window_size = 2000
df['moving_avg'] = df['bid_price_1'].rolling(window_size).mean()
fig, ax = plt.subplots() 
ax.plot(df['timestamp'], df['bid_price_1'])
# ax.plot(df['timestamp'], df['ask_price_1'])
ax.plot(df['timestamp'], df['moving_avg'])
# plt.plot(df['timestamp'], df['profit_and_loss'])
if product == 'BANANAS':
	ax.set_ylim(4850, 5020)
elif product == 'PEARLS':
	ax.set_ylim(9980, 10020)


plt.show()
