import requests

def getSwapPrice(itemname):
    params = {
        "appId": 252490
        #"app_id": 730, CS
        #"app_id": 252490, Rust
        # "market_hash_name": str(itemname)
    }
    r = requests.get("https://market-api.swap.gg/v1/pricing/lowest", params = params).json()
    price = r['result'].get(itemname)['price']
        
    return price