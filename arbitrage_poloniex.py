from poloniex import Poloniex
polo = Poloniex()

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


json_obj= urllib2.urlopen(polo_publicTicker)
data = json.load(json_obj)

"""exchange 1-bitstamp//2-gdax//3-poloniex"""

class currency:
    last= []
    quoteVolume = []
    high24hr= []
    isFrozen=[]
    highestBid=[] 
    percentChange=[]
    low24hr=[]
    lowestAsk=[]
    baseVolume=[]
    id1=[]
    name= []   #uniformizar moedas

class limits:
    pair = ['btc_eur','btc_usd']
    variation = ['lower','upper']
    value = ['500','200']
    scoin_reference = ['usd','eur']
    buy_sell = ['buy','sell']
    exchange = ['bitstamp','poloniex']
    percentage_balance = [60,75]

class balances:
    btc = 0 
    usd = 0 
    eth = 0
    eur = 0

class candlestick_plot:
    currency = []
    date = []
    high = []
    low = []
    day_open = []
    day_close =[]
    volume = []
    quoteVolume= []
    weightedAverage = []

btc_plot = candlestick_plot    
currency_array = currency ()  #poloniex_array
currency_array_bitstamp = currency ()
limits_array = limits ()  #limits_array_universal
balance_bitstamp = balances () #bitstamp_balances
data1 = polo.returnChartData('USDT_BTC',4,86400)


def test_last_values (data1, btc_plot):
    i=0
    btc_plot.currency = 'USDT_BTC'
    for item in data1:
        btc_plot.date = data1[i]['date']
        btc_plot.high = data1[i]['high']
        btc_plot.low = data1[i]['low']
        btc_plot.day_open = data1[i]['open']
        btc_plot.day_close = data1[i]['close']
        btc_plot.volume = data1[i]['volume']
        btc_plot.quoteVolume = data1[i]['quoteVolume']
        btc_plot.weightedAverage = data1[i]['weightedAverage']
        i=i+1    


    
   
    print(datetime.datetime.fromtimestamp(
        int(data1[i-1]['date'])
    ).strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.fromtimestamp(
        int(data1[0]['date'])
    ).strftime('%Y-%m-%d %H:%M:%S'))
    

def show_open_limits () :
    for i in range(len(limits_array.pair)):
        print(limits_array.pair[i]+ ' '+ limits_array.buy_sell[i]+' '+ str(limits_array.percentage_balance[i])+'%' + ' when '+ limits_array.scoin_reference[i] + ' is ' +limits_array.variation[i]+' than '+limits_array.value[i]+' in '+limits_array.exchange[i])
 
def process_limits (limits_array):
    for i in range (limits_array.pair):
        if limits_array.exchange[i] == 'bitstamp' :
            print ('x')
            if limits_array.variation[i] == 'lower':
                #if limits_array.value[i]>currency_array_
           # if limits_array.variation[i] == 'upper':
           # if limits_array.variation[i] == 'iqual':
               print('x')
            
        else: print ('limits_array ERROR')
                

def list_construction_bitstamp ():
    data_btc_usd = public_bitstamp.ticker('btc','usd')
    data_btc_eur = public_bitstamp.ticker('btc','eur')
     

    currency_array_bitstamp.baseVolume.append(float (data_btc_usd['volume']))
    currency_array_bitstamp.last.append(float (data_btc_usd['last']))
    currency_array_bitstamp.highestBid.append(float (data_btc_usd['bid']))
    currency_array_bitstamp.lowestAsk.append(float (data_btc_usd['ask']))
    currency_array_bitstamp.high24hr.append(float( data_btc_usd['high']))
    currency_array_bitstamp.low24hr.append(float(data_btc_usd['low']))

    currency_array_bitstamp.baseVolume.append(float (data_btc_eur['volume']))
    currency_array_bitstamp.last.append(float (data_btc_eur['last']))
    currency_array_bitstamp.highestBid.append(float( data_btc_eur['bid']))
    currency_array_bitstamp.lowestAsk.append(float( data_btc_eur['ask']))
    currency_array_bitstamp.high24hr.append(float( data_btc_eur['high']))
    currency_array_bitstamp.low24hr.append(float (data_btc_eur['low']))

    time.sleep(5) 


    while True :
        data_btc_usd = public_bitstamp.ticker('btc','usd')
        data_btc_eur = public_bitstamp.ticker('btc','eur')
        data_balance = trading_bitstamp.account_balance('btc','eur')
        
        currency_array_bitstamp.baseVolume[0] = float  (data_btc_usd['volume'])
        currency_array_bitstamp.last[0] =float ( data_btc_usd['last'])
        currency_array_bitstamp.highestBid[0] =float( data_btc_usd['bid'])
        currency_array_bitstamp.lowestAsk[0] =float( data_btc_usd['ask'])
        currency_array_bitstamp.high24hr[0]=float ( data_btc_usd['high'])
        currency_array_bitstamp.low24hr[0]=float( data_btc_usd['low'])

        currency_array_bitstamp.baseVolume[1]=float( data_btc_eur['volume'])
        currency_array_bitstamp.last[1]=float( data_btc_eur['last'])
        currency_array_bitstamp.highestBid[1]=float (data_btc_eur['bid'])
        currency_array_bitstamp.lowestAsk[1]=float (data_btc_eur['ask'])
        currency_array_bitstamp.high24hr[1]=float (data_btc_eur['high'])
        currency_array_bitstamp.low24hr[1]=float (data_btc_eur['low'])

        balance_bitstamp.btc = float( data_balance['btc_balance'])
        balance_bitstamp.eur =float ( data_balance['eur_balance'])
    
        time.sleep (5)
     

"""print data['BTC_BBR']['id']"""  #POLONIEX
def list_construction(data,currency_array) :
    json_obj= urllib2.urlopen(polo_publicTicker)
    data = json.load(json_obj)
    end_list=0
    for item in data:
         currency_array.last.append(float  (data[item]['last']))
         currency_array.quoteVolume.append(float  (data[item]['quoteVolume']))
         currency_array.high24hr.append(float  (data[item]['high24hr']))
         currency_array.isFrozen.append(float  (data[item]['isFrozen']))
         currency_array.highestBid.append(float  (data[item]['highestBid']))
         currency_array.percentChange.append(float  (data[item]['percentChange']))
         currency_array.low24hr.append(float  (data[item]['low24hr']))
         currency_array.lowestAsk.append(float  (data[item]['lowestAsk']))
         currency_array.baseVolume.append(float  (data[item]['baseVolume']))
         currency_array.id1.append(data[item]['id'])
         currency_array.name.append(item)
         end_list= end_list+1
    return end_list

def list_update(data,currency_array) :
    i=0
    json_obj= urllib2.urlopen(polo_publicTicker)
    data = json.load(json_obj)
    for item in data:
         currency_array.last[i]=(float  (data[item]['last']))
         currency_array.quoteVolume[i]=(float  (data[item]['quoteVolume']))
         currency_array.high24hr[i]=(float  (data[item]['high24hr']))
         currency_array.isFrozen[i]=(float  (data[item]['isFrozen']))
         currency_array.highestBid[i]=(float  (data[item]['highestBid']))
         currency_array.percentChange[i]=(float  (data[item]['percentChange']))
         currency_array.low24hr[i]=(float  (data[item]['low24hr']))
         currency_array.lowestAsk[i]=(float  (data[item]['lowestAsk']))
         currency_array.baseVolume[i]=(float  (data[item]['baseVolume']))
         currency_array.id1[i]=(data[item]['id'])
         currency_array.name[i]=(item)
         i=i+1
    return

#def bitstamp_limit_check () :
    
#List get_id 
def get_id (currency_array, name_search, end_list):
    i=0
    for name in currency_array.name:
        if name_search == currency_array.name[i]:
            break
        i=i+1
    if i==end_list :
        return 'Currency_not_existing' #non exist error
    return i

#get_parameter('last',currency_array,'BTC_EUR')
def get_parameter(parameter_type, currency_array, name_search) :
      i=get_id(currency_array,name_search,end_list)
      if(i==-1):
         return 'name_error'
      if parameter_type == 'last':
          return currency_array.last[i]
      elif parameter_type == 'quoteVolume':
          return currency_array.quoteVolume[i]
      elif parameter_type == 'high24hr':
          return currency_array.high24hr[i]
      elif parameter_type == 'isFrozen':
          return currency_array.isFrozen[i]
      elif parameter_type == 'highestBid':
        return currency_array.highestBid[i] 
      elif parameter_type == 'percentChange':
          return currency_array.percentChange[i] 
      elif parameter_type == 'low24hr':
            return currency_array.low24hr[i] 
      elif parameter_type == 'lowestAsk':
           return currency_array.lowestAsk[i] 
      elif parameter_type == 'baseVolume':
           return currency_array.baseVolume[i] 
      elif parameter_type == 'id1':
          return currency_array.id1[i]
      elif parameter_type == 'name':
            return currency_array.name[i]
      else :
         return 'parameter_error'

#print_all_poloniex_currencies
def print_currency (currency_array) :
    i=0
    for name in currency_array.name:
        print (currency_array.name[i],currency_array.last[i])
        i=i+1
        
"""Thread for update poloniex currency array"""
def update_currency_array():
  while True:
    list_update(data,currency_array)
    time.sleep (2)




"""
//////set_limit////////////////
    Exchange- 'gdax'/'bitstamp'
    buy_sell- 'buy'/'sell'
    value- 1560
    currency- 'btc_usd', 'btc_eur'
    buy_type- 'imediate'/'fill'
    number- 'all', 50, 40, values in %
///////////////////////////////"""
                    #buy,percentage_balance,pair,variation,value,scoin_reference
                    
def bitstamp_limit (buy_sell,percentage_balance,pair,variation,value, scoin_reference):
   if(variation != 'upper') and (variation != 'lower') and (variation != 'iqual'):
        print ('variation_error')
        return 0
   elif pair == 'btc_eur' :
       if buy_sell == 'buy':
           if (variation == 'lower') and (currency_array_bitstamp.last <value):
               print ('variation_and_value_error')
               return 0
           if (variation== 'upper') and (currency_array_bitstamp.last > value):
               print ('variation_and_value_error')
               return 0
           if (balance_bitstamp.eur > 0 & balance_bitstamp.eur > balance_bitstamp.eur*percentage_balance/100 & percentage_balance >= 0) :
                if scoin_reference == 'usd' | scoin_reference =='eur':
                       limits_array.pair.append('btc_eur')
                       limits_array.percentage_balance(percentage_balance)
                       limits_array.variation(variation)
                       limits_array.value(value)
                       limits_array.scoin_reference(scoin_reference)
                       limits_array.buy_sell('buy')
                       limits_array.buy_sell('bitstamp')
                       #currency_array_bitstamp.last #value 
                       print ('buy_limit_donne')
                else:
                    print('scoin_reference_error')
                    return 0 
           else :
               print('percentage_error')
               return 0
       if buy_sell == 'sell':
           if (variation == 'lower') and (currency_array_bitstamp.last <value):
               print ('variation_and_value_error')
               return 0
           if (variation== 'upper') and (currency_array_bitstamp.last > value):
               print ('variation_and_value_error')
               return 0
           if (balance_bitstamp.btc > 0 & balance_bitstamp.btc > balance_bitstamp.btc*percentage_balance/100 & percentage_balance >= 0):
                if scoin_reference == 'usd' | scoin_reference =='eur':
                       limits_array.pair.append('btc_eur')
                       limits_array.percentage_balance(percentage_balance)
                       limits_array.variation(variation)
                       limits_array.value(value)
                       limits_array.scoin_reference(scoin_reference)
                       limits_array.buy_sell('sell')
                       limits_array.buy_sell('bitstamp')
                       print ('sell_limit_donne')
                else:
                    print('scoin_reference_error')
                    return 0 
           else :
               print('percentage_error')
               return 0
           
       else:
           print('buy_sell_error')
           return 0
   else:
       print ('coin_dont_exists')
   
           


#def limits_array_thread ():
    
    
 
    
#end_list = list_construction(data,currency_array)  #first_list_construction_poloniex
#poloniex_thread = threading.Thread(target = update_currency_array) #update_list_polo
#bitstamp_thread = threading.Thread(target = list_construction_bitstamp)
#bitstamp_thread.start()
#poloniex_thread.start()

#test_last_values (data1,btc_plot)
def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))



#time.strptime("30 Nov 00", "%d %b %y")




"""
def Time(datestr):
    return time.mktime(time.strptime(datestr))"""

"""def UTCstr2epoch(datestr, fmat="%Y-%m-%d %H:%M:%S"):
    """
  #  - takes UTC date string
  #  - returns epoch
"""
    return timegm strptime(datestr, fmat)
    def limit_GDAX (password,tipo,valor,mercado):
    api_key = 'qualquer coisa'
    secret_key = 'qualquer coisa'"""


"""///////////BITSTAMP COMMANDS\\\\\\\\\\\
inicialization- trading_bitstamp.account_balance()['fee']
                        quotes btc_balance
                               usd_balance
                                .user_transactions()
                                






   //////////GDAX COMMANDS\\\\\\\\\\\
public_gdax.getProducts
            getProductOrderBook
            getProductTicker
            getProductTrades
            getProductHistoricRates
            getProduct24HrStates
            getCurrencies
            getTime

trading_gdax.getAccounts
            .getAccount
            .getAccountHistory
            .getAccountHolds
            buyParams {
                    'price' : '100.00'
                    'size'  : '0,01'
                    'product_id' : 'BTC-USD'
                }
            .buy(buyParams)
            .sell
            
"""
