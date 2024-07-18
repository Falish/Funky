"""
    Configuration FIle Parser

    @Author: Falish Dureja 
    @Created at: 18-07-2024

"""

import os
import yaml

class yamlParser:
    def __init__(self, config_file) -> None:
        """

        Args:
            config_file: YAML File location containing info
        """
        if os.path.exists(config_file):
            pass
        else:
            assert(f"{config_file} does not exist, Please check the file.")

    def get_devices(self, device_type=None):
        """
            
        """
