import socket

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # AF_INET = Ipv4 and SOCK_STREAM = TCP
    print('Server hearing at')
    client.bind((HOST, PORT)) # Defines HOST (any) and PORT
    client.listen(1) # Defines simultaneous connections
    while True: # Loop to listen to new clients
        conn, addr = client.accept() # Accept request
        with conn:
            print('Connected by: ', addr)
            buffer = 512
            data = conn.recv(buffer).decode('utf-8')
            if not data: continue #como fazer para voltar ao começo
            