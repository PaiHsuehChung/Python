import logging
import sys
import datetime

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s - line : %(lineno)d', datefmt='%Y-%m-%d %H:%M:%S')

today = datetime.datetime.now()
stf_date = today.strftime("%Y_%m_%d")

def logger_handler(name):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('{}.log'.format(stf_date), 'a', 'utf-8')
    file_handler.setLevel(level=logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(level=logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
