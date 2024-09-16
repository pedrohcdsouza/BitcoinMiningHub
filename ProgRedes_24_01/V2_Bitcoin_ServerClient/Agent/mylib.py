import threading, struct, time, sys, hashlib

# STATIC VARIABLES

threadLock = threading.Lock()

# DYNAMIC VARIABLES

checkwork = False

def checkWork(sock):

    global checkwork
    while checkwork:

        protocol = sock.recv(1)

        if protocol == b'I':
            checkwork = False
            _ = sock.recv(2)
        
        elif protocol == b'Q':
            print('THE SERVER WAS CLOSED ...\n')
            sys.exit()
        
        else:
            print('ERROR: SOMETHING WRONG WITH SERVER/CLIENT COMMUNICATION ...\n')
            sys.exit()

def startMining(sock):

    response = sock.recv(13)
    while len(response) != 13:
        response += sock.recv(1)

    numT, numA, winS, bits, size = struct.unpack('!HHIBI', response)

    trans = sock.recv(size)
    while len(trans) != size:
        trans += sock.recv(1)
    
    global checkwork
    checkwork = True

    while checkwork:
        
        # nonce = (numA * winS) - 1
        nonce = 0
        # nonce < (numA * winS) + winS
        while True:

            bValue = struct.pack('i', nonce)
            hashx = hashlib.sha256(bValue + trans).digest()
            binario = ''.join(format(byte, '08b') for byte in hashx)
            
            if binario[:bits] == '0' * bits:

                response = struct.pack('!cHi', b'S', numT, nonce)
                sock.sendall(response)
                break
            
            nonce += 1
        
        with threadLock:
            
            protocol = sock.recv(1)

            if protocol == b'A':
                print(f'TRANSACTION {numT} FOUNDED BY US ...\n')
                _ = sock.recv(2)
                p = sock.recv(100)
                print(p)
            elif protocol == b'R':
                _ = sock.recv(2)
            elif protocol == b'Q':
                print('THE SERVER WAS CLOSED ...\n')
                sys.exit()
            elif protocol == b'I':
                _ = sock.recv(2)
            else:
                print('ERROR: SOMETHING WRONG WITH SERVER/CLIENT COMMUNICATION ...\n')
                sys.exit()

            checkwork = False

def startApplication(sock, name):

    while True:

        if isinstance(name, str):
            name = name.encode('utf-8')

        request = struct.pack('!c10s', b'G', name)
        sock.sendall(request)

        protocol = sock.recv(1)

        if protocol == b'W':
            time.sleep(10)
        
        elif protocol == b'Q':
            print('THE SERVER WAS CLOSED ...\n')
            sys.exit()
        
        elif protocol == b'T':
            startMining(sock)
        
        else:
            print('ERROR: SOMETHING WRONG WITH SERVER/CLIENT COMMUNICATION ...\n')
            sys.exit()