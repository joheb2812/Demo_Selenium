import inspect
import logging

class LogGen:
    @staticmethod
    def loggen(loglevel=logging.INFO):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename="../Logs/automation.log")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
        formatter1 = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")

        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)

        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger