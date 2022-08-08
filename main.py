import datetime
from time import time, sleep
from incutool_mongodb   import * 
from incutool_coingecko import * 


#------------------------------------------------------------------
# Use this list to define the coins to be pulled and stored
#
# Each tool uses different names, check list at end of this file
#------------------------------------------------------------------
cryptos_id_list_cg = [ 'bitcoin', 'litecoin', 'ethereum' ]
#------------------------------------------------------------------




source_cg = incutool_CoinGecko()

source_cg.init()

mycoll = initdb()

# this executes the API call periodically 
# - it gets cryptos prices from the API, 
# - fills a new document and 
# - uploads it to db

while True:

    sleep(60 - time() % 60)  # this sentence guarantees that the complete loop repeats every minute

    measurement_timestamp = datetime.datetime.utcnow()

    a = source_cg.getPrice( cryptos_id_list_cg )

    crypto_pack = []

    for coin_cg in cryptos_id_list_cg:
       
    
        crypto_obj = {}

        crypto_obj['name']        = coin_cg
        crypto_obj['timestamp']   = measurement_timestamp
        crypto_obj['priceusd_cg'] = a[coin_cg]['usd']
        crypto_pack.append(crypto_obj)

        print(f'''The price for {coin_cg} is {crypto_obj['priceusd_cg']:.2f}''')

    mycoll.insert_many(crypto_pack) 
    exit()






#-----------------------------------------------------------
# cryptos_id_list_cg = [
#     'bitcoin',
#     'litecoin',
#     'ethereum']
# #     ,
#     'ethereum',
#     'tether',
#     'usd-coin',
#     'cardano',
#     'solana',
#     'ripple',
#     'terra-luna',
#     'dogecoin',
#     'polkadot',
#     'shiba-inu'
# ]

#-----------------------------------------------------------
#cryptos_id_list_bi = [
# 'ADAUSDT',
#"BTCUSDT","LTCUSDT",
# 'BNBUSDT',
# 'DOTUSDT',
# 'ETHUSDT',
# 'XRPUSDT',
# 'SOLUSDT',
# 'DOGEUSDT',
# 'CAKEUSDT',
# 'SUSHIUSDT',
# 'MATICUSDT',
# "LUNAUSDT",
# "1INCHUSDT",
# "AAVEUSDT",
# "ADAUSDT",
# "ALGOUSDT",
# "ATOMUSDT",
# "AVAXUSDT",
# "AXSUSDT",
# "BATUSDT",
# "BNBUSDT",
# "BTCUSDT",
# "BTTUSDT",
# "CAKEUSDT",
# "CELOUSDT",
# "CHZUSDT",
# "DASHUSDT",
# "DOGEUSDT",
# "DOTUSDT",
# "ENJUSDT",
# "EOSUSDT",
# "ETCUSDT",
# "ETHUSDT",
# "FILUSDT",
# "FLOWUSDT",
# "FTMUSDT",
# "FTTUSDT",
# "GRTUSDT",
# "HBARUSDT",
# "HNTUSDT",
# "HOTUSDT",
# "ICPUSDT",
# "KSMUSDT",
# "LINKUSDT",
# "LTCUSDT",
# "MANAUSDT",
# "MATICUSDT",
# "IOTAUSDT",
# "MKRUSDT",
# "NEARUSDT",
# "NEOUSDT",
# "ONEUSDT",
# "QNTUSDT",
# "RUNEUSDT",
# "SANDUSDT",
# "SHIBUSDT",
# "SOLUSDT",
# "STXUSDT",
# "THETAUSDT",
# "TRXUSDT",
# "UNIUSDT",
# "VETUSDT",
# "WAVESUSDT",
# "XLMUSDT",
# "XMRUSDT",
# "XRPUSDT",
# "XTZUSDT",
# "ZILUSDT"
#]
#-----------------------------------------------------------
