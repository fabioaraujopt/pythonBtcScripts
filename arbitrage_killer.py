
import urllib2
import json
import GDAX
import bitstamp.client
import time
import threading
from threading import Thread


public_gdax = GDAX.PublicClient()
public_bitstamp = bitstamp.client.Public()

#iniciate_globals
class pairs ():
    eur_btck =0
    eth_eurk =0
    eth_btck =0
    eur_btcg =0
    eth_btcg =0
    eur_btcb =0
class fees ():
    #kraken_fees_5/2017
    kraken_eur_btc_fee = 0.26
    kraken_btc_withdraw_fee = 0.0025
    kraken_eth_eur_fee = 0.26
    #gdax_fees_5/2017
    gdax_btc_eur_fee = 0.25
    gdax_btc_eth_fee = 0.3 
    gdax_eur_withdraw_fee = 0.15
    #bitstamp_fees_5/2017
    bitstamp_eur_btc_fee = 0.25
    #cex.io_fees_5/2017
    cex_io_eur_btc_fee = 0.20
    cex_io_eur_withdraw_fee = 10
    #bank_fee_5/2017
    bankfee = 0.52

pair = pairs()
fee = fees()

#data_upload_threaded
def data_get (pair) :
    value_invested=1300
    while True:   
            #kraken EUR_BTC
            json_obj= urllib2.urlopen('https://api.kraken.com/0/public/Ticker?pair=XBTEUR')
            pair.eur_btck = json.load(json_obj)
            pair.eur_btck = float( pair.eur_btck['result']['XXBTZEUR']['c'][0])
            #kraken ETH_EUR
            json_obj= urllib2.urlopen('https://api.kraken.com/0/public/Ticker?pair=ETHEUR')
            pair.eth_eurk = json.load(json_obj)
            pair.eth_eurk=float( pair.eth_eurk['result']['XETHZEUR']['c'][0] )
            #kraken ETH_BTC
            json_obj= urllib2.urlopen('https://api.kraken.com/0/public/Ticker?pair=ETHXBT')
            pair.eth_btck = json.load(json_obj)
            pair.eth_btck= float(pair.eth_btck['result']['XETHXXBT']['c'][0])
            #gdax EUR_BTC
            pair.eur_btcg = public_gdax.getProductTicker(product="BTC-EUR")
            pair.eur_btcg=float( pair.eur_btcg['price'])
            #gdax ETH_BTC
            pair.eth_btcg = public_gdax.getProductTicker(product="ETH-BTC")
            pair.eth_btcg= float(pair.eth_btcg['price'])
            #bitstamp EUR_BTC
            pair.eur_btcb = public_bitstamp.ticker('btc','eur')
            pair.eur_btcb = float (pair.eur_btcb['last'])   
            #cex.io 
            #calculation
            btc_1b= (value_invested / pair.eur_btcb) * (1-fee.bitstamp_eur_btc_fee*0.01) - 0
            eur_2gb = (btc_1b * pair.eur_btcg)*(1 -(fee.gdax_btc_eur_fee*0.01)) - fee.gdax_eur_withdraw_fee - fee.bankfee
            btc_1k = (value_invested / pair.eur_btck)* (1- fee.kraken_eur_btc_fee*0.01) - fee.kraken_btc_withdraw_fee
            eur_2gk = (btc_1k * pair.eur_btcg) * (1 -(fee.gdax_btc_eur_fee*0.01)) - fee.gdax_eur_withdraw_fee - fee.bankfee
            eth_1b = (value_invested / pair.eth_eurk) * (1- fee.kraken_eth_eur_fee*0.01) - fee.kraken_btc_withdraw_fee
            eur_eth_2gk = ((eth_1b * pair.eth_btcg) * (1- fee.gdax_btc_eth_fee*0.01)) * pair.eur_btcg * (1 -(fee.gdax_btc_eur_fee*0.01))
            #prints
            print('arbitrage_1', round((((eur_2gk/value_invested)-1)*100),4),round((((eur_2gb/value_invested)-1)*100),4), round((((eur_eth_2gk/value_invested)-1)*100),4) )
            #kraken_eur-btc / btc-eur_gdax
            if round((((eur_2gk/value_invested)-1)*100),4) > 1.5 :
                print 'arb_op kraken_EB,gdax_BE ','ini ', value_invested , 'ret ', eur_2gk , 'perc ', round((((eur_2gk/value_invested)-1)*100),4)
                print 'buy ', pair.eur_btck, 'sell ', pair.eur_btcg, '(', btc_1b, ')'
            #bitstamp_eur-btc / btc-eur_bitstamp
            if round((((eur_2gb/value_invested)-1)*100),4) >1.5 :
                print 'arb_op bitstampEB,gdax_BE ','ini ', value_invested , 'ret ', eur_2gb , 'perc ', round((((eur_2gb/value_invested)-1)*100),4)
                print 'buy ', pair.eur_btcb, 'sell ', pair.eur_btcg, '(', btc_1k, ')'
            #kraken_eur-eth/eth-btc /btc-eur_gdax
            if round((((eur_eth_2gk/value_invested)-1)*100),4) > 1.5 :
                print 'arb_op kraken_EE,gdax_EE ','ini ', value_invested , 'ret ', eur_eth_2gk , 'perc ', round((((eur_eth_2gk/value_invested)-1)*100),4)
                print 'buy ', pair.eth_btck, 'sell ', pair.eth_btcg , '/', pair.eur_btcg, '(', eth_1b,'/',eth_1b * pair.eth_btcg,'/',(eth_1b * pair.eth_btcg) * (1- fee.gdax_btc_eth_fee*0.01) * pair.eur_btcg, ')'
            #kraken_eur-btc/btc-eurCEX.io  
            time.sleep(4)
"""
buy_array = []
tipo_array = []
   
def save_last(tipo,buyvalue,add) :
    if add == 'add':
        if tipo == 1 | tipo == 2 | tipo==3 :
            tipo_array.append(tipo)
            tipo_array.append(buyvalue)
    elif add == 'remove':
         x = input("enter_remover_number ") - 1
         if range(tipo_array) > x :
             del buy_array[x]
             del tipo_array[x]
             
         else :print 'list_transaction_error'
    else : print 'invalid_values'

def wait_profit_counter () :
    i= 0 
    for i in range (buy_array):
        if tipo_array [i] == 1:
            print 'buyed btc kraken ',buy_array [i], 'sell now gdax ', 
            
        if tipo_array [i] == 2:
        if tipo_array [i] == 3:
         
"""        
                                                                         
                                                           
Thread(target = data_get(pair)).start()




