#!/usr/bin/env python3
import pandas as pd
from matplotlib import pyplot as plt
import pandas_datareader.data as web
import datetime as dt
import numpy as np

df = pd.read_csv('trading_portfolio.csv', sep=',').astype({'Index': float, 'Total value': float})
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
print(df)

plt.plot(df.Date, df.Index, "-o")
plt.tick_params(axis='x', rotation=70)
plt.ylabel('Index')
plt.title(f'Personal trading portfolio')
plt.tight_layout()
plt.show()
