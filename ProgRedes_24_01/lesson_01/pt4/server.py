#pedrohcdsouza archive

import socket, datetime, mylib, time
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
            time.sleep(10)
            data, now_client = udpSocket.recvfrom(64)
            if now_client == client:
                data = data.decode('utf-8')
                mylib.createHost(data, chost)
                msg = f'Hello {data}, pleasure. This is a file_server, what did you want?\n1 = Upload archive \n2 = Download archive \n3 = Archive list'
                msg = msg.encode('utf-8')
                udpSocket.sendto(msg, client)
                time.sleep(10)
                data, now_client = udpSocket.recvfrom(64)
                if now_client == client:
                    data = data.encode('utf-8')
                    if data == 1:
                        msg = f'Please, choose your file and send to us.'
                        msg = msg.decode('utf-8')
                        udpSocket.sendto(msg, client)
                        time.sleep(10)
                        packet = 0
                        while True:
                            data, client = udpSocket.recvfrom(512)
                    

            else:
                continue


