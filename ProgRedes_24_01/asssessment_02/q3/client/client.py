# @pedrohcdsouza & @matheusluizsoares

import socket, os

HOST = '10.25.3.164'
PORT = 50007
osDir = os.path.abspath(__file__)
osDir = os.path.dirname(osDir)

<<<<<<< HEAD

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))
    while True:
        opt = str(input('Escreva o nome do arquivo: '))
        len_arcname = str(len(opt))
        server.sendall(bytes('PUT\n'+len_arcname+'\r\n\r\n')).encode('utf-8')
        data = server.recv(512).decode('utf-8')
        arcsize, rest = data.split('\n',1)
        with open(osDir + 'download' + opt, 'wb') as archive:
            actsize = len(rest)
            archive.write(rest)
            while actsize < arcsize:
                data = server.recv(512).decode('utf-8')
                archive.write(data)
                actsize += 512
            print('Arquivo gerado.')


    
=======
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))
    server.sendall(b'PUT 10 teste1.txt\r\n\r\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        
>>>>>>> a7d1391ef8771effce59fd0419b573c90136b8e1



    