import yfinance as yf
import json

tick = yf.Ticker('sda.ax')
dump = tick.info
print(dump)