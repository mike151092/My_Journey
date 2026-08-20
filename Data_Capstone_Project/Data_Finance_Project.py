import numpy as np
import pandas as pd
#from pandas_datareader import data, wb,macro
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import yfinance as yf




start = dt.datetime(2006,1,1)
end = dt.datetime(2016,1,1)


BAC = yf.download('BAC',start,end,auto_adjust=False)
C = yf.download('C',start,end,auto_adjust=False)
GS = yf.download('GS',start,end,auto_adjust=False)
JPM = yf.download('JPM',start,end,auto_adjust=False)
MS = yf.download('MS',start,end,auto_adjust=False)
WFC = yf.download('WFC',start,end,auto_adjust=False)

print(BAC.head())
#BAC.columns= BAC.columns.droplevel('Ticker')
#print(BAC.head())
tickers =['BAC','C','GS','JPM','MS','WFC']
bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1)

print(bank_stocks.head())
print(bank_stocks.info())
print(bank_stocks.max())
print(bank_stocks['Close'].max())

#Calculating Returns
returns = pd.DataFrame()


returns= bank_stocks['Close'].pct_change()
print(returns.head())

#sns.pairplot(returns[1:])
#plt.show()


#print(returns.loc['2011-05-06','C'])
print(returns.loc['2009-02-27','C'])

print(returns.idxmin())
#print(returns.idxmax())
print(returns.std())
print(returns.loc['2015-01-01': '2015-12-31'].std())

#sns.displot(returns.loc['2015-01-01': '2015-12-31']['MS'],color='green',bins=50,kde=True)
#sns.displot(returns.loc['2008-01-01':'2008-12-31']['C'],color='red',bins=50,kde=True)



plt.show()