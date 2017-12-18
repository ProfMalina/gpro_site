import urllib.request
import gzip
import shutil
from db import Database
import configparser
import logging, logging.config, logging.handlers
import time
import json

LINK = 'http://gpro.net/ru/GetMarketFile.asp?market=drivers&type=json'
GZ_NAME = 'DriversMarket.json.gz'
FILE_NAME = 'DriversMarket.json'

logging.config.fileConfig('/root/gpro_site/log_main.conf')
logging.getLogger('main')


def downloader():
    """
    Скачивает архив пилотов
    """
    urllib.request.urlretrieve(LINK, GZ_NAME)


def unpacker():
    """
    Разархивирует архив gz
    """
    with gzip.open(GZ_NAME, 'rb') as f_in, open(FILE_NAME, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    try:
        start = time.clock()  # засекаем время
        downloader()  # качаем файл
        unpacker()  # распаковываем
        config = configparser.ConfigParser()  # парсим конфиг
        config.read('/root/gpro_site/config')  # читаем
        db = Database(config['Database']['Path'])  # коннектимся к бд
        drv = db.get_drivers(FILE_NAME)  # готовим пилотов для бд
        for i in drv:  # отправляем пилотов в бд
            d = json.load(open(FILE_NAME))
            i.date = d['Last updated']
            if not db.find_driver(i.id_driver):
                logging.debug("New driver: {}".format(i))
                db.add_driver(i)
            else:
                logging.debug("Update driver: {}".format(i))
                db.update_driver(i)
        elapsed = time.clock() - start
        logging.info(elapsed)
    except Exception as e:
        logging.exception(e)
