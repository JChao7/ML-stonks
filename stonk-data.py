import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web #grab data from yahoo finance api

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2021,1,1)

df = web.DataReader('TSLA', 'yahoo', start, end) #dataframe, similar to spreadsheet

df['100ma'] = df ['Adj Close'].rolling(window=100, min_periods=0).mean()

print(df.tail())

##visualization

ax1 = plt.subplot2grid((6,1), (0,0, rowspan=5, colspan=1))
ax2 = plt.subplot2grid((6,1), (5,0, rowspan=1, colspan=1, sharex=ax1))

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

df['Adj Close'].plot()
plt.show()
