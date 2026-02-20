import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from datetime   import date, datetime, time, timezone       # bring sub modules

def get_stock_data(ticker, start, end):
    data = yf.download(tickers = [ticker], start=start, end=end)
    data.columns = data.columns.droplevel(1)
    data.insert(0, "Ticker", ticker)
    return data
"""
ticker = 'DIS'
start = datetime (2020, 1, 1)
end = datetime.today()

d = get_stock_data(ticker, start, end)
d.head()

print("Hello world")

d = d.reset_index().pivot(index="Date", columns="Ticker", values="Close")
d.head()

"""
start = datetime (2020, 1, 1)
end = datetime.today()

SPY = get_stock_data("SPY", start, end)
IYW = get_stock_data("IYW", start, end)
VT = get_stock_data("VT", start, end)
DBA = get_stock_data("DBA", start, end)
TLT = get_stock_data("TLT", start, end)
PDBC = get_stock_data("PDBC", start, end)
IAU = get_stock_data("IAU", start, end)

SPY.info()



SPY = SPY.reset_index().pivot(index="Date", columns="Ticker", values="Close")
IYW = IYW.reset_index().pivot(index="Date", columns="Ticker", values="Close")
VT = VT.reset_index().pivot(index="Date", columns="Ticker", values="Close")
DBA = DBA.reset_index().pivot(index="Date", columns="Ticker", values="Close")
TLT = TLT.reset_index().pivot(index="Date", columns="Ticker", values="Close")
PDBC = PDBC.reset_index().pivot(index="Date", columns="Ticker", values="Close")
IAU = IAU.reset_index().pivot(index="Date", columns="Ticker", values="Close")

stock = pd.concat([SPY, IYW, VT, DBA, TLT, PDBC, IAU], axis=1, join="outer")
stock.head()

plt.style.use('ggplot')
stock.plot(figsize = (20, 10))
plt.show()

# slicing
covid = stock['2020-2-1': '2020-7-31']

plt.style.use('ggplot')
stock.plot(figsize = (20, 10))
plt.show()

# finding factors

x = covid.index
s_y = covid[['SPY']]
i_y = covid[['IAU']]
d_y = covid[['DBA']]
t_y = covid[['TLT']]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].plot(x, s_y)
axs[1].plot(x, i_y)
axs[2].plot(x, t_y)

fig.suptitle('Covid 19')

# re obtain data as we had dropped it before
PDBC_2 = get_stock_data('PDBC', start, end)
x = PDBC_2.index
y = PDBC_2["Volume"]
plt.figure(figsize= (15, 3))
plt.bar(x, y)
plt.show()

spy_daily_pc = (stock['SPY']/stock['SPY'].shift(1) - 1)*100
plt.hist(spy_daily_pc, bins= 50)
plt.show()


stock_dayily_pc = (stock-stock.shift(1))/stock.shift(1)*100
stock_d_cr = stock_dayily_pc.cumsum()
stock_d_cr.plot(figsize= (20, 10))
plt.show()

df_corr = stock_dayily_pc.corr()
df_corr

plt.imshow(df_corr, cmap='hot', interpolation = 'none')
plt.colorbar()
plt.xticks(range(len(df_corr)), df_cor.columns)
plt.yticks(range(len(df_corr)), df_cor.columns)

plt.gcf().set_size_inches(10, 10)
plt.show()