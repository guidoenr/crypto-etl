from model import *
import api
import json
from datetime import datetime

def map_coin(coin, max_price, min_price):
    dumped = json.dumps(coin.data, indent=3)
    coin_to_persist = {
        'name': coin.name,
        'year': coin.date.year,
        'month': coin.date.month,
        'max_price' : max_price,
        'min_price' : min_price
    }
    coin = CoinDB(*coin_to_persist)

    session.add(coin)
    session.commit()
    
    
