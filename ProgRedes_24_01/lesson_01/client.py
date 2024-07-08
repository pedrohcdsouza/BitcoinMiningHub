# @pedrohcdsouza archive

import socket

HOST = '10.25.3.164'
PORT = 50000

server = (HOST, PORT)

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))
while True:
    msg = input(f'Message to {HOST}: \n')
    msg = msg.encode('utf-8')
    udpSocket.sendto(msg, server)
    data, server = udpSocket.recvfrom(512)
    if data:
        data = data.decode('utf-8')
        print(data)
udpSocket.close()