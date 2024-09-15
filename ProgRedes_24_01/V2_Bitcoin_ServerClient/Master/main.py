import socket, sys, threading

print('THE SERVER IS STARTING ...')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    HOST = '127.0.0.1'
    PORT = 31471
    server.bind((HOST,PORT))
    server.listen(10)

except:

    print(f'ERROR: THE SERVER WAS NOT STARTED ...\n')
    sys.exit()

print('THE SERVER WAS STARTED ...\n')



