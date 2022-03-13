# quant-trading
This repository is a corpus of quantitative analysis of the crypto markets [via Binance] based on Stephan Jansen's [book](https://www.amazon.com/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715) -- Machine Learning for Algorithmic Trading: Predictive models to extract signals from market and alternative data for systematic trading strategies with Python, 2nd Edition.

![ML for Algorithmic Trading](https://camo.githubusercontent.com/96a637dcc2abfbec4725cbe0a78233934c8659969ad9c9b9b5d7f0d05059937d/68747470733a2f2f6d6c34742e73332e616d617a6f6e6177732e636f6d2f6173736574732f636f7665725f746f635f67682e706e67)

### 1. Market Data
**Order book analysis**: After slightly modifying and refactoring the [Binance Public Data](https://github.com/binance/binance-public-data/) script, I was able to download the list of daily aggregate trades (buy and sell data) for any asset on the exchange for a specified period. I chose to analyze aggregate trades over normal trades. If you want to read about the difference, you can do so [here](https://www.reddit.com/r/BinanceExchange/comments/8sangq/api_what_is_the_difference_between_aggtrades_and/e102l7x/).

The order book is categorized into buy orders, sell orders, price, and size. Analyzing these four attributes for a particular asset informs us about the order imbalances that give insight into an asset's direction over the short term. For example, a large number of buy orders around a specific level might indicate a level of support for the asset. The [MarketData](MarketData/) folder is divided into the [data collection](MarketData/data_collection/) segment where I download order book data and the [data analysis](MarketData/data_analysis/) segment where I sort the top equities by traded value.

The Binance Order Book can also be downloaded [here](https://data.binance.vision/).
