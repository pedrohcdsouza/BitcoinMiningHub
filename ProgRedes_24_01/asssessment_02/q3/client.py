# @pedrohcdsouza & @matheusluizsoares

import socket

HOST = '192.168.2.245'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))
    
    protocol = int(input(f"Hello! You're connected on: {HOST}:{PORT}. A server-file.\nChoose a option:\n1 = Download file from server\n2 = Upload file from server\n3 = List files from server\n"))
    
    if protocol == 1:
        print('You have chosen to download a file.')
        arcname = str(input('Enter the name of the file.\n'))
        bytesfrom = int(input('Choose from which byte you want to download from\n0 to default\n'))
        server.sendall(f'GET\n{arcname}\n{bytesfrom}'.encode('utf-8'))

    elif protocol == 2:
        print('You have chosen to upload a file.')
        arcname = str(input('Enter the name of the file.\n'))
        bytesfrom = int(input('Choose from which byte you want to download from\n0 to default\n'))
        server.sendall(f'PUT\n{arcname}\n{bytesfrom}'.encode('utf-8'))
    
    elif protocol == 3:
        print('You have chosen to list the files.')
        





    