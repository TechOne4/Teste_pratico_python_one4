from loguru import logger

class LogWrapper:
    def __init__(self, log_file="./Logs/log.log"):
        logger.add(sink=log_file, format="{time} | {level} | {message}")

    def debug(self, message):
        logger.debug(message)

    def info(self, message):
        logger.info(message)

    def warning(self, message):
        logger.warning(message)

    def error(self, message):
        logger.error(message)

    def critical(self, message):
        logger.critical(message)