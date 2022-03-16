import requests
import json
from env import logger
from datetime import datetime

logger = logger.get_logger()
COINGECKO_API = 'https://api.coingecko.com/api/v3'

def get_data_by_date(coin:str, date:datetime, *params):
    date_str = date.strftime('%d-%m-%Y')
    url = f'{COINGECKO_API}/coins/{coin}/history?date={date_str}'
    return requests.get(url, *params).json() # dict

def get_market_chart(coin:str):
    url = f'{COINGECKO_API}/coins/{coin}?vs_currency=usd'
    return requests.get(url).json()

def get_price(data):
    try: 
        return float(data['market_data']['current_price']['usd']).__round__(3) if data['market_data'] else 0
    except KeyError:
        return 0
    
   
def prettify_data(data:dict):
    pretty = json.dumps(data, indent=3)
    with open('coins/cache.json', 'w') as f:
        f.write(pretty)
    print(pretty)

def ping_api():
    return requests.get(COINGECKO_API + '/ping').json()


if __name__ == '__main__':
    prettify_data(get_market_chart('bitcoin'))