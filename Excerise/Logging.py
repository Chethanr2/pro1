import logging

logging.basicConfig(filename='Logging_file', level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("This is my debug test message")
logging.info("This is my Info test message")
logging.error("This is my error test message")
logging.critical("This is my critical test message")
logging.warning("This is my warning test message")

