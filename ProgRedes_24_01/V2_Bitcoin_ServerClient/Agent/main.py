import socket,sys
from mylib import *

print('THE APPLICATION IS STARTING ...')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    
    HOST = '127.0.0.1'
    PORT = 31471
    sock.connect((HOST,PORT))

except:

    print('ERROR: THE APPLICATION WAS NOT STARTED ...\n')
    sys.exit()

print('THE APPLICATION WAS STARTED ...\n')

name = str(input('Write a username: '))

startApplication(sock, name)

threading.Thread(target=checkWork, args=(sock,)).start()