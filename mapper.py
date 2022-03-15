from model import *
import api
import model
import json
from datetime import datetime

def map_coin(data:dict, date:str):
    dumped = json.dumps(data, indent=3)
    date_obj = datetime.strptime(date, '%d-%m-%Y')
    coin_d1 = {
        'coin_id': data['symbol'],
        'price_usd': data['market_data']['current_price']['usd'],
        'date': date,
        'json' : dumped
    }
    coin_d2 = {
        'coin_id': data['symbol'],
        'year': date_obj.year,
        'month': date_obj.month,
        'max_price' : 1,
        'min_price' : 2
    }

    coin = Coin(**coin_d1)
    coindata = CoinData(**coin_d2)

    session.add(coin)
    session.add(coindata)
    session.commit()
    
    
