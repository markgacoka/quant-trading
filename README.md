# quant-trading
This repository is a corpus of quantitative analysis of the crypto markets [via Binance] based on Stephan Jansen's [book](https://www.amazon.com/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715) -- Machine Learning for Algorithmic Trading: Predictive models to extract signals from market and alternative data for systematic trading strategies with Python, 2nd Edition.

### Market Data
**Order book analysis**: Using the [Binance Public Data](https://github.com/binance/binance-public-data/) script by Binance, I was able to download the list of individual trades (buy and sell data) for any asset on the exchange organized by price level for a specified period. I chose the aggregate trades over normal trades as the distinction was irrelevant. If you want to read about the difference, you can get more information [here](https://www.reddit.com/r/BinanceExchange/comments/8sangq/api_what_is_the_difference_between_aggtrades_and/e102l7x/).
The order book is categorized into buy orders, sell orders, price, and size. Analyzing these four attributes for a particular asset informs us about the order imbalances that give insight into an asset's direction in the short term. For example, a large number of buy orders around a specific level might indicate a level of support for the asset. I use the order book to sort the top equities by traded value in my analysis.

The Binance Order Book can also be downloaded [here](https://data.binance.vision/).
