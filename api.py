# @author: Guido Enrique
# @github: /guidoenr
# @gitlab: /guidoenr
# https://github.com/man-c/pycoingecko TODO

import requests
import logger
import json

COINGECKO_API = 'https://api.coingecko.com/api/v3'

def get_data(subdomain:str, *params): # params could be optional
    url = f'{COINGECKO_API}{subdomain}'
    return requests.get(url, *params).json() # dict

# def prettify_data(data:dict):
#     pretty = json.dumps(data, indent=3)
#     with open('cache.json', 'w') as f:
#         f.write(pretty)
#     print(pretty)

