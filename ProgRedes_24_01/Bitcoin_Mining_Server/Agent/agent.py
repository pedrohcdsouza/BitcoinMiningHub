# Agent Core Code

import socket, struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as agent:

    HOST = '127.0.0.1'
    PORT = 31471

    agent.connect((HOST, PORT))

    yourName = str(input('Digite o seu nome ...\n'))
    yourName = struct.pack('c10s',b'G', yourName.encode())
    agent.sendall(yourName)

    protocol = agent.recv(1)

    if protocol == b'W':
        print('The server has no transactions ...')
    
    if protocol == b'T':
        print('Starting a new transaction ...')
        response = agent.recv(13)
        while len(response) != 13:
            response += agent.recv(1)
        
        numTrans, numClient, winSize, bitsZero, tranSize = struct.unpack('!HHIBI', response)

        trans = agent.recv(tranSize)
        while len(trans) != tranSize:
            trans += agent.recv(tranSize)
        
        
    
    


