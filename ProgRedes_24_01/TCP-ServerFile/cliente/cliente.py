import socket
import os, sys

osDir = os.path.abspath(__file__)
osDir = os.path.dirname(osDir)

HOST = '10.25.2.78'  # Defining the IP SERVER
PORT = 1981 # Defining PORT 

# WHILE for new request

while True:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #AF_INET = IVP4 / SOCK_STREAM = TCP
        server.connect((HOST, PORT)) # HOST and PORT to connect
        # server.timeout(10) # Defining 10s timeout
        
        protocol = int(input(f"Hello! You're connected on: {HOST}:{PORT}. SERVER-FILE\n1 = Download archive\n2 = List archive\n"))

        if protocol == 1:

            print('CHOOSE the file to download: ')
            arcname = str(input('Enter the name of the file: '))

            downloadDir = os.path.join(osDir, 'download')
            downloadDir = os.listdir(downloadDir)

            if arcname in downloadDir:
                print('Your desired file already exists ...')
                continue

            bytesfrom = int(input('Choose from which byte you want to download from (0 to start from the beginning):\n')) # Defines from which byte the file will be written
            server.sendall(f'GET\n{arcname}\n{bytesfrom}\r\n\r\n'.encode('utf-8')) # Sending request header

            response = server.recv(512)
            while b'\r\n\r\n' not in response:
                response = server.recv(512)

            p = response.find(b'\r\n\r\n') # Catching the final position of the header

            # Separating the header from the rest of the data

            header = response[:p].decode('utf-8')
            header = header.split('\n') # Breaking the header
            rest = response[p+4:]

            if header[0] == 'OK':

                print('STARTING DOWNLOAD ...')
                arcsize = int(header[1]) # Size of the file
                filepath = os.path.join(osDir, 'download', arcname)
                filepath = os.path.realpath(filepath) # Ensuring that file intrusions by \..

                try:

                    with open(filepath, 'wb') as archive:
                        archive.seek(bytesfrom) # Defines from which byte will be writed
                        actsize = 0 # Actually size

                        # WHILE for write data

                        while actsize < arcsize:

                            archive.write(rest) # Writing the rest data if has it

                            # Writing the real data

                            data = server.recv(512)
                            archive.write(data)

                            actsize += 512

                    print('DOWNLOAD FINISHED ...')
                
                # Handling exception and and treating it  

                except PermissionError:
                    print('\nYou doesnt have permission to write this file. Please, try again ...\n')
                    continue
                except FileNotFoundError:
                    print('\nYour desired file coudnt be created. Please, try again ...\n')
                    continue
                except Exception as UnknownError:
                    print('\nA unknown error was detected. Please, try again ...\n')
                    continue

                else:
                    again = str(input('Do you want to continue? (Y/N): ')).lower() # Asking if the user want to continue requesting
                    if again == 'y':
                        continue
                    sys.exit(0)

            elif header[0] == 'ERROR': # Verify if response is a ERROR one
                
                # Explains the detected error

                if header[1] == 'IS_A_DIRECTORY':
                    print('\nYou desired file its a directory. Please, try again ...\n')
                    continue
                elif header[1] == 'FILE_NOT_FOUND':
                    print('\nYou desired file doensnt exists. Please, try again ...\n')
                    continue
                elif header[1] == 'UNKNOWN':
                    print('\nA unknown error was detected. Please, try again ...\n')
                    continue

        elif protocol == 2:

            server.sendall(f'LIST\n'.encode('utf-8')) #
            data = server.recv(512).decode('utf-8')

            while '\r\n\r\n' not in data:
                data = server.recv(512).decode('utf-8')

            data = data.split('\r\n\r\n') # Removing '\r\n\r\n' from data

            # Creating a rectangle with server files

            try:

                print('-' * 40)
                print(data[0])
                print('-' * 40)

            except Exception as UnknownError:
                print('\nA unknown error was detected. Please, try again ...\n')
                continue

            else:
                again = str(input('Do you want to continue? (Y/N): ')).lower() #
                if again == 'y':
                    continue
                sys.exit(0)

            
            
