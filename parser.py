import argparse

def formater(date:str):
    spl = date.split('-')
    return f'{spl[2]}-{spl[1]}-{spl[0]}'


def init_parser():
    parser = argparse.ArgumentParser(description='Mutt-data download crypto info tool')
    parser.add_argument(
        "-s", 
        "--startdate", 
        help="startdate in format ISO8601(e.g. 2019-10-30)", 
        type=formater,
        required=False,
    )
    parser.add_argument(
        "-e", 
        "--enddate", 
        help="endate in format ISO8601(e.g. 2019-10-5)", 
        type=formater,
        required=False,
    )
    parser.add_argument(
        "-c", 
        "--coin", 
        help="the coin name(e.g. bitcoin - ethereum - cardano)", 
        required=True,
    )
    parser.add_argument(
        "-d", 
        "--date", 
        help="the date for the coin data", 
    )
    parser.add_argument(
        "-persist", 
        help="persist the data",
        action='store_const', const=42
    )
    args = parser.parse_args()
    return args