#pedrohcdsouza archive

import socket, datetime, time
from mylib import *

HOST = ''
PORT = 50000
clientDir = {}

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))
print('Server on-line...')

while True:
    data, client = udpSocket.recvfrom(64)
    data = data.decode('utf-8')
    chost, cport = client[0], client[1]

    if mylib.validadeHost(chost) == False:
        msg = f'Hello {chost}! Your first name are not in our database, please send it to us.'
        msg = msg.encode('utf-8')
        udpSocket.sendto(msg, client)
    else:
        name = mylib.validadeHost(chost)
        msg = f'Hello {name}! This is a server-files. Choose a option:\n1-Upload files\n2-Download files\n3-List files\n'
        msg = msg.encode('utf-8')
        udpSocket.sendto(msg, client)

        data, client = udpSocket.recvfrom(64)
        data = data.decode('utf-8')

        if data == 1:
            uploadFiles()
        elif data == 2:
            downloadFiles()
        elif data == 3:
            listFiles()
        else:
            msg = f'Option invalid!'
            msg.encode('utf-8')
            udpSocket.sendto(msg, client)
            break
msg = f'Connection finished...'
msg = msg.encode('utf-8')
udpSocket.sendto(msg, client)