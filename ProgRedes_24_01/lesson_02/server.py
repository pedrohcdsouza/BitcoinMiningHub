import socket, datetime

HOST = ''
PORT = 50000
clientDir = {}

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))
print('Server on-line...')

while True:
    data, client = udpSocket.recvfrom(512)
    data = data.decode('utf-8')
    chost, cport = client[0], client[1]
    if data:
        if data[0] == 'reader':
            print(f'The host {chost} is downloading a file.')
            with open(data[1], 'r') as reader:
                arc = writer.read()
                udpSocket.sendto(arc, client)

        if data[0] == 'writer':
            print(f'The host {chost} is writing a file.')
            with open(data[2], 'w') as writer:
                writer.write(data[1])

udpSocket.close()
