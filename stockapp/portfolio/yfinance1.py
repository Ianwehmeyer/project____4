import yfinance as yf
import json
#print( help( yf))
stock = yf.Ticker('MSFT')

name = stock.info['shortName']

print(stock.info)