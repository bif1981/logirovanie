import requests as rq
import logging
import bs4

logging.basicConfig(level=logging.INFO)  # Настройка логирования
logger = logging.getLogger('RequestsLogger')
logger.setLevel(logging.DEBUG)


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING

class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


# Настройка обработчика файла с INFO-логами
info_handler = logging.FileHandler('success_responses.log', 'w', 'utf-8')
info_handler.setLevel(logging.INFO)
info_format = logging.Formatter('%(asctime)s - %(message)s')
info_handler.setFormatter(info_format)
logger.addHandler(info_handler)
info_handler.addFilter(InfoFilter())

# Настройка обработчика файла с WARNING-логами
warning_handler = logging.FileHandler('bad_responses.log', 'w', 'utf-8')
warning_handler.setLevel(logging.WARNING)
warning_format = logging.Formatter('%(asctime)s - %(message)s')
warning_handler.setFormatter(warning_format)
logger.addHandler(warning_handler)
warning_handler.addFilter(WarningFilter())

# Настройка файла с ERROR-логами
error_handler = logging.FileHandler('error_responses.log', 'w', 'utf-8')
error_handler.setLevel(logging.ERROR)
error_format = logging.Formatter('%(asctime)s - %(message)s')
error_handler.setFormatter(error_format)
logger.addHandler(error_handler)
error_handler.addFilter(ErrorFilter())

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
    except rq.exceptions.Timeout:
        logger.error(f"ERROR: {site}, TIMEOUT")
    except rq.exceptions.RequestException as e:
        logger.error(f"ERROR: {site}, REQUEST FAILED: {e}")
