# ## pedrohcdsouza archive

import sys, time, socket, os
from wrap import *

osDir = os.path.abspath(__file__)
osDir = os.path.dirname(osDir)

# Handling sys.argv

if len(sys.argv) == 2:
    arcName = ''
elif len(sys.argv) == 3:
    arcName = sys.argv[2]
else:
    print('ERROR: Invalid arguments ...')
    time.sleep(2)
    sys.exit(1)

# Handling arguments

try:

    protocol, request = sys.argv[1].split(':', 1) 
    url, content = request[2:].split('/', 1) # Ex: ['httpbin.org', '/image/jpeg']
    ext = content.split('/')[1] # Extension
    content = '/' + content # The split has cut a bar

except ValueError:

    print('VALUE_ERROR: Invalid URL Request ...')
    time.sleep(2)
    sys.exit(1)

except Exception as exc:

    print(exc)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: # Defining network and transport protocols (IPV4, TCP)

    # Defining application protocols and their specifications

    if protocol == 'http':
        
        server.connect((url, 80))

    elif protocol == 'https': 
        
        server.connect((url, 443))
        server = wrapSocket(server, url) # Function for secure listening

    else:
        print('ERROR: Invalid protocol ...')

    server.sendall(f'GET  {content} HTTP/1.1\r\nHost: {url}\r\n\r\n'.encode('utf-8')) # Sending the request to desired http-server

    # Listening to the answer

    data = server.recv(512)
    while b'\r\n\r\n' not in data:
        data += server.recv(512)

    rawHeader, rest = data.split(b'\r\n\r\n', 1) # Separating headers from other data
    rawHeader = rawHeader.decode('utf-8')

    # Checking response status

    status, header = rawHeader.split('\r\n', 1)
    status = status.split(' ', 1)[1]

    if status != '200 OK':
        print(f'ERROR: Invalid status ...\n{status}')
        time.sleep(2)
        sys.exit(1)

    # Handling header data

    arcSize = -1

    if arcName == '': # For to empty arcName

        for metadata in header.split('\r\n'): # Separating metadata
            key, value = metadata.split(': ')
            if key == 'Content-Length':
                arcSize = int(value)
            if key == 'Content-Type':
                arcName = value
                arcName = arcName.split('/')[1]

    else: # For to not empty arcName

        for metadata in header.split('\r\n'):
            print(metadata)
            key, value = metadata.split(': ')
            if key == 'Content-Length':
                arcSize = int(value)
    
    # Defining reader-mode

    if arcSize == -1: # Data-Reader Mode: Chunked
        print('Chunked')
    
    elif arcSize > 0: # Data-Reader Mode: Length

        actSize = len(rest)

        try:
            with open(osDir + f'\\{arcName}.{ext}', 'wb') as archive:
                
                print('Starting download ...\r\n')

                archive.write(rest)

                while actSize < arcSize:
                    data = server.recv(512)
                    archive.write(data)
                    actSize += 512
                
                print('Download done ...\r\n')
        
        except Exception as exc:
            print(exc)

    else: 
        print('ERROR: The disered file its empty ...')
        time.sleep(3)
        sys.exit(1)

        

    



    


