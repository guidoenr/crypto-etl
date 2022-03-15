import requests
import json
from datetime import datetime

COINGECKO_API = 'https://api.coingecko.com/api/v3'

def get_data_by_date(coin:str, date:datetime, *params):
    date_str = date.strftime('%d-%m-%Y')
    url = f'{COINGECKO_API}/coins/{coin}/history?date={date_str}'
    return requests.get(url, *params).json() # dict

def get_price(data):
    return float(data['market_data']['current_price']['usd']).__round__(3)

def prettify_data(data:dict):
    pretty = json.dumps(data, indent=3)
    with open('coins/cache.json', 'w') as f:
        f.write(pretty)
    print(pretty)

def ping_api():
    return requests.get(COINGECKO_API + '/ping')
