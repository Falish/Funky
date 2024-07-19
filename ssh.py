"""
    SSH Connection
"""

import os
import paramiko

class SSHClient:
    def __init__(self, ip, username, password, port=22) -> None:
        pass

    def exec_command(self, command, timeout=200):
        """
            Execute commands and return the output
        """

    def exec_command_async(self, command, timeout=200):
        """
            Execute comamdn using screen module 
        """