#!/usr/bin/env python3
import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [3, 4, 1]
data = pd.read_csv('TeslaMarketCap.csv', sep=',', parse_dates=['Date'], dayfirst=True)
data[data.columns[1]] = data[data.columns[1]].replace('\$','', regex=True).astype(float)

# Get annual growth in market cap
marketCap = data[data.columns[1]]
divideBy = data[data.columns[1]].drop([11], axis=0)
divideBy.index += 1
divideBy = divideBy.append(pd.Series(0))
anlGrowth = (marketCap / divideBy) * 100 # Calculate % growth

plt.plot(data[data.columns[0]], marketCap)
plt.plot(data[data.columns[0]], anlGrowth)
plt.title('Tesla annual market cap and yearly growth in value')
plt.legend(['Market cap at start of each year (billion USD)', 'Annual growth in stock price (percent)'])
plt.show()
