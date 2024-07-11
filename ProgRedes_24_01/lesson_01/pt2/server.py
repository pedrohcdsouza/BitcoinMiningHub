import socket, datetime, time

HOST = ''
PORT = 50000
clientDir = {}
nameDir = {}

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))
print('Server on-line...')

while True:
    data, client = udpSocket.recvfrom(512)
    data = data.decode('utf-8')
    chost, cport = client[0], client[1]
    if data:
        if chost not in nameDir:
            msg = f'Hello! {chost}, please, enter your nome.'
            msg = msg.encode('utf-8')
            udpSocket.sendto(msg, client)
            print(f'The {chost} try talk, but, we until doesnt have your name.')
            data, client = udpSocket.recvfrom(512)
            chost2, cport2 = client[0],client[1]
            if chost2 == chost:
                nameDir[chost] = data
                msg = f'Hello {nameDir[chost]} nice to meet you, type your message.'
                msg = msg.encode('utf-8')
                udpSocket.sendto(msg, client)
        else:
            clientDir[chost2] = (cport2, (data, datetime.datetime.now()))
            msg = f'Hello! {nameDir[chost2]}, I received your message. \n "{data}"\n'
            print(f'I received "{data}" from "{nameDir[chost2]}" at {clientDir[chost2][1][1]}')
            msg = msg.encode('utf-8')
            udpSocket.sendto(msg, client)

udpSocket.close()
