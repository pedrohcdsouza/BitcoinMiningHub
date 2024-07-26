import socket

hostname = socket.gethostname()


HOST = ''
PORT = 50007
SERVERIP = socket.gethostbyname(hostname)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # AF_INET = Ipv4 and SOCK_STREAM = TCP
    print(f'Server hearing at {SERVERIP}:{PORT}')
    client.bind((HOST, PORT)) # Defines HOST (any) and PORT
    client.listen(1) # Defines simultaneous connections
    while True: # Loop to listen to new clients
        conn, addr = client.accept() # Accept request
        with conn:
            print('Connected by: ', addr)

            header = conn.recv(512).decode('utf-8')

            if not header: continue

            protocol = header.split('\n')[0]

            if protocol == 'GET':
                protocol, arcname, bytesfrom = header.split('\n')
                client.sendall('OK'.encode('utf-8'))
                while True:
                    with open()

            elif protocol == 'PUT':
                protocol, arcname, bytesfrom = header.split('\n')
            
            elif protocol == 'LIST':
                print('ok')

            