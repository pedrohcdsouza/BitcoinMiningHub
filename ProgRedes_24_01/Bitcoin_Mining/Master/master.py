# Master Core Code

import socket, sys

print('Starting up the server ...\n')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: # Defining network and transport protocols (IPV4, TCP)

    try: 

        while True:

            server_ip, port = '10.25.3.165', 31471 # Defining connection options
            server.bind((server_ip,port)) # Hearing requests
            server.listen(10)

    except OSError: # Handling exception in case of server startup error
        print('ERROR: Server startup failure ...\nEnding Application ...\n')
        sys.exit()

    except Exception as exp:
        print(exp)
