from env import logger
import datetime
import api, parser
import json, os, pandas as pd

COINS_PATH = f'{os.getcwd()}/coins'
args = parser.init_parser()

class Data:
    def __init__(self, coin_name, date):
        self.coin_name = coin_name
        self.date = date
        self.dic = {}
        

    def download(self):
        self.dic = api.get_data_by_date(self.coin_name, self.date)
        

    def show(self):
        dumped = json.dumps(self.data, indent=3)
        print(dumped)


class DataAnalizer():
    def __init__(self, data, month, year):
        self.data = data 
        self.month = month
        self.year = year

    def find_max_and_min_price(self):
        date = datetime.date(year=self.year, month=self.month, day=1)
        prices = []
        while(date.month == self.month):
            self.data.date = date
            self.data.download()
            price = float(self.data.dic['market_data']['current_price']['usd'])
            prices.append(price.__round__(2))
            logger.data(f'{self.year} / {self.month}')
            logger.data(f'day: {date.day} - price: {price}')
            date += datetime.timedelta(days=1)

        min_price = min(prices)
        max_price = max(prices)
        return min_price, max_price




if __name__ == '__main__':
    date = args.date
    coin = args.coin
    start_date = args.startdate
    end_date = args.enddate

    data = Data(coin, date)
    data.download()

    data_analyzer = DataAnalizer(data, 2, 2021)
    data_analyzer.find_max_and_min_price()


