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
        clientDir[chost] = (cport, (data, datetime.datetime.now()))
        msg = f'Hello! {chost}, I received your message. \n "{data}"\n'
        print(f'I received "{data}" from "{client}" at {clientDir[chost][1][1]}')
        msg = msg.encode('utf-8')
        udpSocket.sendto(msg, client)

udpSocket.close()
