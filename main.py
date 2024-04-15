import requests as rq
import logging
import bs4

logging.basicConfig(level=logging.INFO)  # Настройка логирования
logger = logging.getLogger('RequestsLogger')
logger.setLevel(logging.DEBUG)



info_handler = logging.FileHandler('success_responses.log')     # Настройка обработчиков для разных уровней сообщений
info_handler.setLevel(logging.INFO)
info_format = logging.Formatter('%(asctime)s - %(message)s')
info_handler.setFormatter(info_format)
logger.addHandler(info_handler)

warning_handler = logging.FileHandler('bad_responses.log')
warning_handler.setLevel(logging.WARNING)
warning_format = logging.Formatter('%(asctime)s - %(message)s')
warning_handler.setFormatter(warning_format)
logger.addHandler(warning_handler)

error_handler = logging.FileHandler('blocked_responses.log')
error_handler.setLevel(logging.ERROR)
error_format = logging.Formatter('%(asctime)s - %(message)s')
error_handler.setFormatter(error_format)
logger.addHandler(error_handler)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru', 'https://twitter.com']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger.info(f"INFO: '{site}', response - 200")
        else:
            logger.warning(f"WARNING: '{site}', response - {response.status_code}")
    except rq.exceptions.ConnectTimeout:
        logger.error(f"ERROR: {site}, NO CONNECTION")
