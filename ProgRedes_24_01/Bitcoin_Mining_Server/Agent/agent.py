# Agent Core Code

import socket, struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as agent:

    HOST = '127.0.0.1'
    PORT = 31471

    agent.connect((HOST, PORT))

    yourName = str(input('Digite o seu nome ...'))
    yourName = struct.pack('c10s',b'G', yourName.encode())
    agent.sendall(yourName)

