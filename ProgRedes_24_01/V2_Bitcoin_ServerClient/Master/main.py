import socket, sys, threading
from mylib import *

print('THE SERVER IS STARTING ...')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    HOST = '127.0.0.1'
    PORT = 31471
    sock.bind((HOST,PORT))
    sock.listen(10)

except:

    print(f'ERROR: THE SERVER WAS NOT STARTED ...\n')
    sys.exit()

print('THE SERVER WAS STARTED ...\n')

threading.Thread(target=connectAgents, args=(sock,)).start()
threading.Thread(target=writeTransactions, args=(sock,)).start()
threading.Thread(target=startBot).start()