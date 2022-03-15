from distutils.log import INFO, WARN
import logging

def api(msg):
    logging.log(INFO, f'[api]: {msg}')


def data(msg):
    logging.log(INFO, f'[data_analyzer]: {msg}')


def mapper(msg):
    logging.log(WARN, f'[mapper]: {msg}')