"""

"""

import os
import argparse
import yamlParser
import logger

class Tester:
    def __init__(self) -> None:
        self.args = self.argsParser()
        self.logger = self.getLogger(name="tester")
        self.devYamlParser = yamlParser.devYamlParser(self.configFile, self.logger)
        self.runYamlParser = yamlParser.runCfgParser(self.runConfig, self.logger)
        self.logger.info("Main Tester Started!!!")

        self.devYamlParser.get_devices()

    def argsParser(self):
        """
            Argument parser for the main tester file.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", help="Device Config File containing system devices information", default="C:\\Users\\Falish\\Desktop\\python_pr\\Framework\\funky_git\\device_config.yml")
        parser.add_argument("--test", help="Test Case name that needs to be executed")
        parser.add_argument("--loops", help="Number of loops to be executed for given test case. Note: Only valid if --test arg is given", default=1, type=int)
        parser.add_argument("--log", help="change the logging path. Note: Default path is in c:\\automation\\funkyLogs", default="C:\\Automation\\FunkyLogs")
        parser.add_argument("--runConfig", help="can be used to define which tests to be run, will be ignored if --test is provided", default="c:\\Automation\\run_config.yml")
        
        args = parser.parse_args()

        self.configFile = args.config
        self.logPath = args.log
        if args.test:
            tests = args.test.split(",")
            self.testCaseList = tests
            self.logger.inf(f"Test cases Provided by user: {[self.testCaseList]}")
        else:
            self.runConfig = args.runConfig

    def getLogger(self, name, level="INFO"):
        """
            Create new or return the existing logger.
            @args:
                name: name of the logger
            @return: logger object
        """
        self.fLogger = logger.FunkyLogger(self.logPath)
        flog = self.fLogger.create_logger(name)
        self.fLogger.add_file_handler(logger=flog, logPath=self.logPath, logName=self.fLogger.name)
        self.fLogger.set_level(logger=flog, level=level)
        return flog

if __name__ == "__main__":
    tester = Tester()
