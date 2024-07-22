# @pedrohcdsouza & @matheusluizsoares

import socket

HOST = '10.25.3.164'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))
    server.sendall(b'PUT 10 teste1.txt\r\n\r\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        



    