import requests
from forex_python.converter import CurrencyRates

class Buff:
    
    def __init__(self, header):
        self.header = {
            "Cookie": str(header)
        }
    def getBuffPrice(self, itemname):
        URL = "https://buff.163.com/api/market/goods"
        params = {
            "game" : "rust",
            "page_num" : "1",
            "search" : str(itemname)
        }
        r = requests.get(URL, params=params, headers=self.header).json()
        priceCNY = r["data"]["items"][0]["sell_min_price"]
        priceUSD = float(priceCNY)
        return round(priceUSD, 2)