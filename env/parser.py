import argparse
from datetime import datetime

desc = """[CRYPTO-ETL] download crypto data tool
@author: github.com/guidoenr - gitlab.com/guidoenr4
"""


def valid_date(date:str):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return date_obj
    except ValueError:
        msg = 'not a valid date: {0!r}'.format(date)
        raise argparse.ArgumentTypeError(msg)
   


def init_parser():
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "-c", 
        "--coin", 
        help="The coin name(e.g. bitcoin - ethereum - cardano)", 
        required=True,
    )
    parser.add_argument(
        "-d",
        "--date",
        type=valid_date,
        required=True, 
        help="The date for the coin data in format yyyy-mm-dd", 
    )
    parser.add_argument(
        "-an",
        "--analysis",
        help="Full analysis for the crypto in year and month",
        action='store_const', const=2
    )
    args = parser.parse_args()
    return args
