"""

"""

import os
import argparse
import yamlParser

class Tester:
    def __init__(self) -> None:
        cli_args = self.argsParser()
        self.yamlParser = yamlParser()

    def argsParser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", help="Device Config File containing system devices information", default="c:\\Automation\\device_config.yaml")
        parser.add_argument("--test", help="Test Case name that needs to be executed")
        parser.add_argument("--loops", help="Number of loops to be executed for given test case. Note: Only valid if --test arg is given", default=1, type=int)
        
        args = parser.parse_args()

        self.configFile = args.config
        if args.test:
            tests = args.test.split(",")
            self.testCaseList = tests

