# Master Library Code

import socket, struct

def connectMiners(server): # Function to connect miners

    while True:

        try: 

            connection, IP = server.accept() # Connecting the miner

        except Exception as Exp:
            continue

        response = connection.recv(11)
        while len(response) != 11:
            response += connection.recv(1)
            
        response = struct.unpack('c10s', response)

        print(response)
        