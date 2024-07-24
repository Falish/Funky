"""
    SSH Connection
"""

import os, time, re
import paramiko

from pprint import pprint as pp

class SSHClient:
    def __init__(self, hostname, username, password, port=22, friendly_name=None) -> None:
        if not friendly_name:
            self.name = hostname
        else:
            self.name = friendly_name

        # Connecting to SSH Client
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client.connect(hostname=hostname, username=username, password=password, port=port)

        # Creating a session
        self.session = self.client.invoke_shell()

    def exec_command(self, command, timeout=200):
        """
            Execute commands and return the output
        """
        try:
            command = command + "\n"
            def recv_rdy():
                stdout = stderr = ""
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                while(True):
                    time.sleep(0.1)
                    if self.session.recv_ready():
                        stdout += self.session.recv(1024).decode("utf8")
                    else:
                        break
                    if self.session.recv_stderr_ready():
                        stderr += self.session.recv_stderr(1024).decode("utf8")
                stdout = "".join(ansi_escape.sub('', stdout).split("\r")[2:-1])
                stderr = "".join(ansi_escape.sub('', stderr).split("\r")[2:-1])
                return stdout, stderr
            recv_rdy()
            self.session.send(command)
            stdout, stderr = recv_rdy()
        except paramiko.SSHException as e:
            print(f"Error While Executing command on {self.name} : {e}")
        return stdout, stderr

    def exec_command_async(self, command, timeout=200):
        """
            Execute comamnd using screen module 
        """

if __name__ == "__main__":
    ssh = SSHClient("192.168.226.128", "falish", "pass", 22, "SUT")
    pp(ssh.exec_command("python3 --version")[0])