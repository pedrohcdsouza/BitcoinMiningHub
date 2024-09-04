# Master Core Code

import socket, sys
from masterlib import *

print('The server is starting up ...\n')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: # Defining network and transport protocols (IPV4, TCP)

    try: # Trying to start the server ...
    
            # Defining connection options

            HOST = '127.0.0.1'
            PORT = 31471
            server.bind((HOST,PORT)) # Hearing requests
            server.listen(10)

    except OSError: # Handling exception in case of server startup error

        print('ERROR: The server failed to start ...\nEnding Application ...\n')
        sys.exit()

    except Exception as exp:

        print(exp)

    else:

        print('The server is now online ...\n')

        connectMiners(server)