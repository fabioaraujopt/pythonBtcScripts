from poloniex import Poloniex
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
polo = Poloniex()
"""
polo_publicTicker = 'https://poloniex.com/public?command=returnTicker'
polo_public24Volume= 'https://poloniex.com/public?command=return24hVolume'
polo_publicOrderBook= 'https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_NXT&depth=10'
polo_publicTradeHistory= 'https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_NXT&start=1410158341&end=1410499372'

bitstamp_key = 'QaPyRIwnk6y0ZQ3sZxgrPA9JaF7BdtWa'
bitstamp_secret = 'JyRUdwtZroVVkj9igVg67h5CBKASqQc9'
bitstamp_user = '790720'

gdax_key = '594b8e741b893a31dcc6a965b8405b7d'
gdax_b64 = '0LlOtQ0eBUvmCtZoF16Fs4f03l0esWj2npm41q7vvmCtKJEY5Kz+zuA1qS/xvYRld/+3l7rMOsotV6dV9P9KCw=='
gdax_passphrase ='coelho_gdax'

trading_bitstamp = bitstamp.client.Trading(username=bitstamp_user, key=bitstamp_key, secret=bitstamp_secret)
trading_gdax = GDAX.AuthenticatedClient(key = gdax_key, b64secret = gdax_b64, passphrase = gdax_passphrase)
public_bitstamp = bitstamp.client.Public()
public_gdax = GDAX.PublicClient()

"
json_obj= urllib2.urlopen(polo_publicTicker)
data = json.load(json_obj)

exchange 1-bitstamp//2-gdax//3-poloniex"""

class candlestick_plot ():
    currency = []
    date = []
    high = []
    low = []
    day_open = []
    day_close =[]
    volume = []
    quoteVolume= []
    weightedAverage = []

"""
300, 5min
900, 15min
1800,30min
7200,2hr
14400,4hr
86400,1d
"""
   
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

