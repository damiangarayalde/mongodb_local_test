from pycoingecko import CoinGeckoAPI


class incutool_CoinGecko:

    currency='usd' # used in coingecko get_price function and in the parsing of its returned values

    def init(self):        
        self.cg = CoinGeckoAPI()


    def getPrice(self, cryptos_id_list ):
       
        return self.cg.get_price( ids=cryptos_id_list, vs_currencies=self.currency)

