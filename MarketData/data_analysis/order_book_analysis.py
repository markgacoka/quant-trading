# %%
# Order Book Depth
# [AUTHOR'S NOTE] This implementation is flawed. 
# I have not accounted for decimal prices since I have converted 
# prices to int data type. Additionally, the histogram does not 
# account for the quantity of coins bought at a specific price. 
# It just plots a distribution of the density of prices on the 
# buy and sell sides. It is more so for visualization in seaborn.
import requests
import seaborn as sns
import matplotlib.pyplot as plt

futures_api_url = 'https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=100'

response = requests.get(futures_api_url)
response_formatted = response.json()
message_time = response_formatted['E']
transaction_time = response_formatted['T']
bids = response_formatted['bids']
asks = response_formatted['asks']

bid_prices = [int(float(bid[0])) for bid in bids]
bid_quantities = [bid[1] for bid in bids]

ask_prices = [int(float(ask[0])) for ask in asks]
ask_quantities = [ask[1] for ask in asks]


fig, ax = plt.subplots(figsize=(7,5))
cbar_kws = {'linewidth': 1, 'alpha': .5}
sns.histplot(bid_prices, color='#72bcd4', cbar_kws=cbar_kws, element="step",
            ax=ax, label='Buy', kde=False)
sns.histplot(ask_prices, color='red', cbar_kws=cbar_kws, element="step",
            ax=ax, label='Sell', kde=False)

ax.legend(fontsize=10)
ax.set_title('Limit Order Price Distribution')
ax.set_xlabel('Price')
ax.set_ylabel('Quantity')
sns.despine()
fig.tight_layout()
# %%
