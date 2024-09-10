# Master Core Code

import socket, sys, threading
from masterlib import *

print('The server is starting up ...\n')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Defining network and transport protocols (IPV4, TCP)

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
    sys.exit()

else:

    print('The server is now online ...\n')

    transactionsThread = threading.Thread(target=hearTransactions)
    connectAgentsThread = threading.Thread(target=connectAgents, args=(server,))

    transactionsThread.start()
    connectAgentsThread.start()