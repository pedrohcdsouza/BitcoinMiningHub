import socket
import os

osDir = os.path.abspath(__file__)
osDir = os.path.dirname(osDir)

HOST = ''  # Accepting whatever HOST
PORT = 1981

# CONFIGURING SERVER

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #AF_INET = IVP4 / SOCK_STREAM = TCP
    print(f'Server listening at PORT: {PORT}') 
    server.bind((HOST, PORT)) # HOST and PORT to hearing
    server.listen(1) # Maximum request at a time

# WHILE for new request

    while True:

        conn, addr = server.accept()
        with conn:
            try:
                print('Connected by: ', addr)
                conn.settimeout(30)
                
                # Defining request

                request = conn.recv(512).decode('utf-8') # Hearing the raw request
                header = request.split('\r\n\r\n')[0] # Separating header
                protocol = header.split('\n')[0] # Separating protocol

# PROTOCOL GET

                if protocol == 'GET':

                    _, arcname, bytesfrom = header.split('\n') # Separating header data
                    bytesfrom = int(bytesfrom)

                    try:

                        arcpath = os.path.join(osDir,'arquivos',arcname)
                        arcpath = os.path.realpath(arcpath) # Ensuring that file intrusions by \..
                        arcsize = os.path.getsize(arcpath)

                        with open(arcpath, 'rb') as archive:
                            archive.seek(bytesfrom) # Defines from which byte will be sent
                            conn.sendall(f'OK\n{arcsize}\r\n\r\n'.encode('utf-8')) # Notifying that the data will be sent and the file size

                            # WHILE for read data up to file size

                            actsize = bytesfrom
                            while actsize < arcsize:
                                data = archive.read(512)
                                conn.sendall(data)
                                actsize += 512
                            
                        print(f'GET Operation {arcname} by\n{addr}')

                    # Handling exception and informing the client application        

                    except IsADirectoryError:
                        conn.sendall(f'ERROR\nIS_A_DIRECTORY\r\n\r\n'.encode('utf-8'))
                        continue
                    except FileNotFoundError:
                        conn.sendall(f'ERROR\nFILE_NOT_FOUND\r\n\r\n'.encode('utf-8'))
                        continue
                    except Exception as UnknownError:
                        conn.sendall(f'ERROR\nUNKNOWN\r\n\r\n'.encode('utf-8'))
                        continue

# PROTOCOL LIST

                elif protocol == 'LIST':

                    try:
                        listpath = os.path.join(osDir, 'arquivos')
                        listarc = os.listdir(listpath) # Defining the files present on the server

                        # LOOP for transform list into a string to be sent correctly

                        strlist = ''

                        for i in listarc:
                            strlist += f'{i}\n'
                        conn.sendall(strlist.encode('utf-8'))
                        conn.sendall('\r\n\r\n'.encode('utf-8'))

                        print(f'LIST Operation by\n{addr}')

                    # It is not necessary to handle specific exceptions as it is unlikely here.

                    except Exception as UnknownError:
                        conn.sendall(f'ERROR\nUNKNOWN'.encode('utf-8'))
                        continue

            except socket.timeout:
                print(f'Timeout from {addr}')
                continue
            
            except Exception as UnknownError:
                continue

        