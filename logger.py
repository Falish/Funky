"""


    @Author: Falish
    @Created on: 18-07-2024
"""

import sys
import logging

log_level_map = {
    "INFO": logging.INFO,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
    "DEBUG": logging.DEBUG
}

class FunkyLogger:
    def __init__(self, logPath) -> None:
        self._logName = "MAIN"
        self._logger = self.create_logger(name=self._logName)
        sHandler = logging.StreamHandler(sys.stdout)
        self._logger.addHandler(sHandler)
        sHandler.setFormatter(self.formatter)
        self._logger.info("Logger Created SuccessFully!!")
    
    def create_logger(self, name):
        logger = logging.getLogger(name)
        self.name = name
        logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        return logger

    def get_logger(self, name=None):
        if not name or name == self._logName: 
            name = self._logName
            return self.logger
        else:
            return self.create_logger(name)
    
    def add_file_handler(self, logger, logPath, logName):
        fHandler = logging.FileHandler(f"{logPath}\\{logName}.log", mode='w')
        fHandler.setFormatter(self.formatter)
        logger.addHandler(fHandler)

    def set_level(self, logger, level):
        logger.setLevel(log_level_map.get(level, logging.INFO))
        