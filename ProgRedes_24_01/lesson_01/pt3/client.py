# @pedrohcdsouza archive

import socket

HOST = '10.25.3.164'
PORT = 50000

server = (HOST, PORT)

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    option = int(input('What do you want? \n1: Write a file to the server.\n2: Download a file from the server.\n 3: Show server files.'))
    if option == 1:
        arcName = str(input('Write the name of file with extesion: '))
        with open(arcName, 'r') as reader:
            arc = reader.read()
            response = ['writer', arc, arcName]
            udpSocket.sendto(response, server)
    if option == 2:
        arcName = str(input('Write the name of file with extesion: '))
        response = ['reader', arcName]
        udpSocket.sendto(response, arcName)
        data, server = udpSocket.recvfrom(512)
        with open(arcName, 'w') as writer:
            writer.write(data)
    else:
        print('Choose a valid option!')


            
udpSocket.close()