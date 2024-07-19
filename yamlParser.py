"""
    Configuration FIle Parser

    @Author: Falish Dureja 
    @Created at: 18-07-2024

"""

import os
import yaml
from pdb import set_trace as bkp

class yamlParser:
    def __init__(self, config_file, logger) -> None:
        """

        Args:
            config_file: YAML File location containing info
        """
        self.logger = logger
        if os.path.exists(config_file):
            self.logger.info(f"Parsing the config file {config_file}")
            with open(config_file, 'r') as file:
                self.cfg = yaml.safe_load(file)
        else:
            assert(f"{config_file} does not exist, Please check the file.")


class devYamlParser(yamlParser):
    def __init__(self, config_file, logger) -> None:
        super().__init__(config_file, logger)

    def get_devices(self, device_type=None):
        """
            
        """
        self.logger.info(self.cfg)
        for i in self.cfg["DEVICES"]:
            self.logger.info(i)

class runCfgParser(yamlParser):
    def __init__(self, config_file, logger) -> None:
        super().__init__(config_file, logger)

    def get_test_case_list(self):
        self.logger.info(self.cfg)