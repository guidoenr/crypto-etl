from env import logger, parser
from model import mapper
import datetime
import api, json, os, pandas as pd

COINS_PATH = f'{os.getcwd()}/coins'
args = parser.init_parser()
lg = logger.get_logger()

class Coin:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.data = {}
        

    def download_data(self):
        try:
            data = api.get_data_by_date(self.name, self.date)
            self.data = data
        except:
            lg.critical('maximum requests made')
        
        
    def show_data(self):
        dumped = json.dumps(self.data, indent=3)
        print(dumped)


class CoinAnalyzer():
    def __init__(self, coin, month, year):
        self.coin = coin 
        self.month = month
        self.year = year
        self.max_price = 0
        self.min_price = 0

    def show(self):
        if args.analysis:
            self.find_max_and_min_price()
        else:
            self.coin.show_data()

    def find_max_and_min_price(self):
        date = datetime.date(year=self.year, month=self.month, day=1)
        prices = []
        lg.warning(f'{self.coin.name} in: {self.year}/{self.month}')

        ant = 0
        while(date.month == self.month):
            self.coin.date = date
            self.coin.download_data()
            price = api.get_price(self.coin.data)
            bt = 0
            if price > ant:
                bt = 1
            if price == 0:
                lg.warning(f'No {coin.name} data for {date}')
                break;
            logger.best(f'date:[{date}], price: U$D {price}', bt)
            prices.append(price)
            ant = price
            date += datetime.timedelta(days=1)

        self.min_price = min(prices)
        self.max_price = max(prices)
        if price != 0:
            lg.info(f'MAX_PRICE: {self.max_price} u$d , MIN_PRICE: {self.min_price} u$d')
        else:
            lg.info(f'(for that period): MAX: {self.max_price}, MIN: {self.min_price}')

    def persist(self):
        if args.persist:
            mapper.map_coin(self.coin, self.min, self.max)


if __name__ == '__main__':
    coin = args.coin 
    date = args.date 

    coin = Coin(coin, date)
    coin.download_data()

    analyzer = CoinAnalyzer(coin, date.month, date.year)
    analyzer.show()


