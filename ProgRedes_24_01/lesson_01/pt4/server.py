#pedrohcdsouza archive

import socket, datetime, mylib, sleep

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
    
    if data:
        if mylib.validadeHost(chost):
            msg = f'Hello {chost}! Your first name are not in our database, please send it to us.'
            msg = msg.encode('utf-8')
            udpSocket.sendto(msg, client)
            sleep(10)
            data, now_client = udpSocket.recvfrom(64)
            if now_client == client:
                mylib.createHost(data, chost)
                msg = f'Hello {data}, pleasure. This is a file_server, what did you want?\n1 = Upload archive, 2 = Download archive, 3 = Archive list'
                msg = msg.encode('utf-8')
                udpSocket.sendto(msg, client)
            else:
                continue


