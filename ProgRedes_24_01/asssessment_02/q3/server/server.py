import socket

HOST = ''
PORT = 50007

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: # AF_INET = Ipv4 and SOCK_STREAM = TCP
        print('Server hearing at')
        server.bind((HOST, PORT)) # Defines HOST (any) and PORT
        server.listen(1) # Defines simultaneous connections
        conn, addr = server.accept() # Accept request
        with conn:
            print('Connected by: ', addr)
            while True:
                data = conn.recv(512) # Buffer 512
                if not data: break
                
                



 
            
            