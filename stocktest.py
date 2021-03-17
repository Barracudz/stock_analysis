#!/usr/bin/env python3
import pandas as pd
from matplotlib import pyplot as plt
import pandas_datareader.data as web
import datetime as dt
import numpy as np

def getStockData():
    stocks = []
    stock = 'dummy'
    # Let user give min 1 stock and max 5
    while stock != '' or len(stocks) == 0:
        if len(stocks) == 5:
            break
        print('\nEnter a stock ticker or leave blank and press enter to stop.')
        print('You have to enter at least one stock and max 5')
        stock = input('Enter stock ticker: ')
        if stock != '':
            stocks.append(stock)

    print(f'\nCompanies chosen: {stocks}')

    start = input('\nEnter start date (YYYY-MM-DD) - leave blank and press enter for first date: ')
    end = input('\nEnter end date (YYYY-MM-DD) - leave blank and press enter for last date: ')

    currentDate = dt.datetime.today()
    earliestDate = '1900-01-01' # If user wants earliest date

    dfs = [] # Get data from Yahoo and create dataframe
    for s in stocks:
        dfs.append(web.DataReader(s, 'yahoo', start if start != '' else earliestDate, end if end != '' else currentDate))

    marketCapDf = web.get_quote_yahoo(stocks)['sharesOutstanding'] # Get amount of shares

    # Put shares in list
    shares = []
    for i in range(len(stocks)):
        shares.append(marketCapDf.iloc[i])

    # Calculate historical market cap and put dfs in list
    historicalCaps = []
    for i in range(len(stocks)):
        historicalCaps.append(dfs[i]['Close'] * shares[i])

    # Create 2 subplots with shared x-axis
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    stocksStr = '' # Create string with tickers
    for s in stocks:
        if s == stocks[len(stocks)-1]:
            stocksStr += s
        else:
            stocksStr += s + ', '

    # Plot chart for historical market cap
    for i in range(len(stocks)):
        ax1.plot(historicalCaps[i])

    ax1.set(ylabel='Market cap in USD')
    ax1.set_title(f'Historical market caps for: {stocksStr}')
    ax1.legend(stocks)

    # Plot chart for historical stock price
    for i in range(len(stocks)):
        ax2.plot(dfs[i]['Close'])

    ax2.set(ylabel='Stock price in USD')
    ax2.set_title(f'Historical stock prices for: {stocksStr}')
    ax2.legend(stocks)

    # Plot chart for percentage growth in stock price
    for i in range(len(stocks)):
        startingPrice = dfs[i].iloc[0][0] # Get startingPrice
        print(f'\nStock: {stocks[i]}')
        print(f'Starting price: {startingPrice}')
        ax3.plot(((dfs[i]['Close'] / startingPrice) - 1) * 100)

    ax3.set(ylabel='Percentage growth')
    ax3.set_title(f'Percentage growth in stock prices of: {stocksStr}')
    ax3.tick_params(axis='x', rotation=70)
    ax3.legend(stocks)

    plt.tight_layout()
    plt.show()

getStockData()
