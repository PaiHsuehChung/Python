from logger_handler import logger_handler

logger = logger_handler('main')

try:
    logger.debug('This is deubg')
    logger.info('Info message')
except Exception:
    logger.error('divde error', exc_info=True)