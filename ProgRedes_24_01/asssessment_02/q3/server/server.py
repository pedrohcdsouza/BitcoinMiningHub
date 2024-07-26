import socket, os

HOST = ''
PORT = 50007
osDir = os.path.abspath(__file__)
osDir = os.path.dirname(osDir)


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
            if not data:
                print('Desconnected by', addr) 
                continue
            header, body = data.split('\r\n\r\n', 1)
            type, rest = header.split('\n', 1)

            if type == 'GET':
                arcname = rest
                arcsize = os.path.getsize(osDir + 'arquivos' + arcname)
                client.sendall(arcsize+'\n').encode('utf-8')
                actsize = 0
                with open(osDir + 'arquivos', 'rb') as archive:
                    while actsize < arcsize:
                        data = archive.read(512)
                        actsize += len(data)
                        client.sendall(data)
                        data = ''