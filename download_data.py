from datetime import datetime
import api, mapper, logger, parser
import json, os, pandas as pd


COINS_PATH = f'{os.getcwd()}/coins'
args = parser.init_parser()

class CoinSaver():
    def __init__(self, coin:str, dates:list):
        self.coin = coin
        self.dates = dates
        self.URI = '/coins/{coin_id}/history?date={date}'
        self.coin_dir = f'{COINS_PATH}/{coin}'

    def check_dir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
    
    def create_sub_dir(self, start_date, end_date):
        dir_name = f'{self.coin_dir}/{start_date}_to_{end_date}/'
        return dir_name

    def save_data(self):
        self.check_dir(self.coin_dir)
        savepath = f'{self.coin_dir}'
        dates = self.dates
        dates_between = [dates[0]] if len(self.dates) > 1 else [datetime.now().strftime("%d-%m-%Y")]
        if len(self.dates) > 1:
            savepath = self.create_sub_dir(dates[0], dates[1])
            dates_between = pd.date_range(start=self.dates[0], end=self.dates[1], freq='D').strftime("%d-%m-%Y").to_list()
        self.check_dir(savepath)
        for date in dates_between:
            url = self.URI.format(coin_id=self.coin, date=date)
            data = api.get_data(url)
            self.persist_coin(data, date)
            with open(f'{savepath}/{date}.json', 'w') as f:
                f.write(json.dumps(data, indent=3))

    def persist_coin(self, data, date):
        if (args.persist):
            mapper.map_coin(data, date)


if __name__ == '__main__':
    saver = ...
    if args.date:
        saver = CoinSaver(args.coin, [args.date])
    else:
        saver = CoinSaver(args.coin, [])
    if args.startdate and args.enddate:
        saver = CoinSaver(args.coin, [args.startdate, args.enddate])

    saver.save_data()
    
    


