# Master Library Code

import socket

def connectMiner(server):
    while True:

        connection, minerIp = server.accept()