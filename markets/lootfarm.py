import requests
from forex_python.converter import CurrencyRates

    
def getLootFarmPrice(itemname):
    r = requests.get('https://loot.farm/fullpriceRUST.json').json()
    price = 0
    for item in r:
        if item['name'] == itemname:
            price = item['price']

    if len(str(price)) == 2:
        price = "0." + str(price)
    elif len(str(price)) == 1:
        price = "0.0" + str(price)
    else:
        price = str(price)[:-2] + '.' + str(price)[-2:]
    
    return price
    