from poloniex import Poloniex
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import csv


class candlestick_plot ():
    avg_gdax = []
    avg_bitstamp = []
    avg_kraken = []
    avg_cex = []

class spread_plot ():
    gdax_bitstamp = []
    gdax_kraken = []
    gdax_cex = []
    bitstamp_cex =[]
    bitstamp_kraken =[]
    kraken_cex =[]

    
    

Candlestick = candlestick_plot ()
Spread = spread_plot ()

with open("coinbase_june.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
     #row time/avg/max/min
    print readCSV
    for row in readCSV :
        try: 
            Candlestick.avg_gdax.append(float(row[1]))
        except:
            continue

with open("bitstamp_june.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    error = 0
     #row time/avg/max/min
    print readCSV
    for row in readCSV :
        try:
            Candlestick.avg_bitstamp.append(float(row[1]))
        except:
            continue
   
with open("cex_june.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
     #row time/avg/max/min
    for row in readCSV :
        try:
            Candlestick.avg_cex.append(float(row[1]))
        except:
            continue

with open("kraken_june.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
     #row time/avg/max/min
    for row in readCSV :
        try:
            Candlestick.avg_kraken.append(float(row[1]))
        except:
            continue


def spread_graphs():
    i=0
    for values in Candlestick.avg_gdax:
        try:
            Spread.gdax_kraken.append(abs(1-(Candlestick.avg_gdax[i]/Candlestick.avg_kraken[i])))
        except:
            continue
        i=i+1
    i=0
    for values in Candlestick.avg_gdax:
        try:
            Spread.gdax_bitstamp.append(abs(1-(Candlestick.avg_gdax[i]/Candlestick.avg_bitstamp[i])))
        except:
            continue
        i=i+1
    i=0
    for values in Candlestick.avg_gdax:
        try:
            Spread.gdax_cex.append(abs(1-(Candlestick.avg_gdax[i]/Candlestick.avg_cex[i])))
        except:
            continue 
        i=i+1
    i=0
    for values in Candlestick.avg_bitstamp:
        try:
            Spread.bitstamp_cex.append(abs(1-(Candlestick.avg_bitstamp[i]/Candlestick.avg_cex[i])))
        except:
            continue
        i=i+1
    i=0
    for values in Candlestick.avg_bitstamp:
        try:
            Spread.bitstamp_kraken.append(abs(1-(Candlestick.avg_bitstamp[i]/Candlestick.avg_kraken[i])))
        except:
            continue
        i=i+1
    i=0
    for values in Candlestick.avg_kraken:
        try:
            Spread.kraken_cex.append(abs(1-(Candlestick.avg_kraken[i]/Candlestick.avg_cex[i])))
        except:
            continue
        i=i+1
spread_graphs()
plt.plot(Spread.gdax_kraken)
plt.show()




"""


300, 5min
900, 15min
1800,30min
7200,2hr
14400,4hr
86400,1d


   
data1 = polo.returnChartData('BTC_ETH',90,14400)
btc_plot = candlestick_plot()

def test_last_values ():
    i=0
    btc_plot.currency = 'USDT_BTC'
    for item in data1:
        btc_plot.date.append(float(item['date']))
        btc_plot.high.append (float(item['high']))
        btc_plot.low.append(float(item['low']))
        btc_plot.day_open.append(float(item['open']))
        btc_plot.day_close.append(float(item['close']))
        btc_plot.volume.append(float(item['volume']))
        btc_plot.quoteVolume.append(float(item['quoteVolume']))
        btc_plot.weightedAverage.append(float(item['weightedAverage']))
        i=i+1
        
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

test_last_values ()
x=0
y= len(btc_plot.date)
ohlc = []
while x < y:
        append_me = btc_plot.date[x],btc_plot.day_open[x],btc_plot.high[x],btc_plot.low[x], btc_plot.day_close[x], btc_plot.volume[x]
        ohlc.append(append_me)
        x+=1


candlestick_ohlc(ax1, ohlc)
plt.show()

"""
