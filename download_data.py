from env import logger
import datetime
import api, parser
import json, os, pandas as pd

COINS_PATH = f'{os.getcwd()}/coins'
args = parser.init_parser()
logger = logger.get_logger()

class Coin:
    def __init__(self, coin_name, date):
        self.coin_name = coin_name
        self.date = date
        self.data = {}
        

    def download_data(self):
        try:
            data = api.get_data_by_date(self.coin_name, self.date)
            self.data = data
        except:
            logger.critical('maximum requests made')
        
        
    def show(self):
        dumped = json.dumps(self.data, indent=3)
        print(dumped)


class CoinAnalyzer():
    def __init__(self, coin, month, year):
        self.coin = coin 
        self.month = month
        self.year = year

    def find_max_and_min_price(self):
        date = datetime.date(year=self.year, month=self.month, day=1)
        prices = []
        logger.warning(f'{self.coin.coin_name} in: {self.year}/{self.month}')

        while(date.month == self.month):
            self.coin.date = date
            self.coin.download_data()
            price = api.get_price(self.coin.data)
            if price == 0:
                logger.warning(f'No {coin.coin_name} data for {date}')
            prices.append(price)
            date += datetime.timedelta(days=1)

        min_price = min(prices)
        max_price = max(prices)
        logger.info(f'MAX_PRICE: {max_price} u$d , MIN_PRICE: {min_price} u$d')
        return min_price, max_price



if __name__ == '__main__':
    date = args.date
    coin = args.coin
    start_date = args.startdate
    end_date = args.enddate

    coin = Coin(coin, date)
    coin.download_data()

    coin_analyzer = CoinAnalyzer(coin, date.month, date.year)
    coin_analyzer.find_max_and_min_price()


