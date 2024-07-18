# @pedrohcdsouza archive

import socket
from clientlib import *

HOST = '192.168.2.245'
PORT = 1010
server = (HOST, PORT)
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:

    msg = input(f'Message to {HOST}: \n').encode('utf-8')
    udpSocket.sendto(msg, server)
    data, server = udpSocket.recvfrom(512)
    if data == '000_UPLOAD':
        sendfile()
    elif data == '001_DOWNLOAD':
        recfile()
    elif data == '002_LIST':
        listfile()
    else:
        print(data.decode('utf-8'))
udpSocket.close()