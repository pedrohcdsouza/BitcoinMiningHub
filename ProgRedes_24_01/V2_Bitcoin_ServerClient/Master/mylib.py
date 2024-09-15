import struct, hashlib, threading, sys

# STATIC VARIABLES

threadLock = threading.lock()

# DYNAMIC VARIABLES

Agents = dict()
Transactions = dict()
Founded = list()

def writeTransactions(server):
    
    t = 1

    while True:

        try:

            transaction = str(input('WRITE THE TRANSACTION:\n'))

            if transaction == 'quit': # PROTOCOL - Q

                response = struct.pack('!c', b'Q')

                for i in Agents.items():

                        allConn = i[1]
                        allConn.sendall(response)
                
                server.close()
                sys.exit()

            bits = str(input('WRITE THE BITS TO BE ZERO:\n'))
            Transactions[t] = [bits, transaction]

            t += 1
        except SystemExit:
            print('THE SERVER WAS CLOSED ...\n')

        except:
            print('ERROR: Invalid transaction ...\n')
            continue



def hearAgents(conn, ip):

    while True:

        protocol = conn.recv(1)
        protocol , _ = struct.unpack('c', protocol)

        if protocol == b'G': # PROTOCOL - G

            name = conn.recv(10)
            while len(name) != 10:
                name += conn.recv(1)
            name = struct.unpack('10s', name)
            Agents[ip] = [name,conn]
        
            if len(Transactions) == 0 or len(Transactions) == len(Founded): # PROTOCOL - W
                
                response = struct.pack('c', b'W')
                conn.sendall(response)
            
            else: # PROTOCOL - T

                for k,i in Transactions.items():

                    if k not in Founded:

                        numT = k
                        numA = len(Agents)
                        winS = 1000000
                        bits = i[0]
                        size = len(i[1])
                        tran = i[1]

                        response = struct.pack(f'!cHHIBI{size}s', b'T',numT,numA,winS,bits,size,tran)
                        conn.sendall(response)

                        break

        elif protocol == b'S': # PROTOCOL - S
            
            with threadLock:

                data = conn.recv(6)
                while len(data) != 6:
                    data += conn.recv(1)
                numT, nonce = struct.unpack('!HI', data)

                bits, trans = Transactions[numT]

                if isinstance(trans, str): 
                    trans = trans.encode('utf-8')
                
                nonceValue = struct.pack('I', nonce)
                transHash = hashlib.sha256(nonceValue + trans).digest()
                transBin = ''.join(format(byte, '08b') for byte in transHash)

                if transBin[:bits] == '0' * bits: # PROTOCOL - A and I

                    Founded.append(numT)

                    response = struct.pack('!cH', b'A',numT)
                    conn.sendall(response)

                    response = struct.pack('cH', b'I',numT)

                    for i in Agents.items():

                        allConn = i[1]
                        allConn.sendall(response)
                
                else: # PROTOCOL - R

                    response = struct.pack('!cH', b'R', numT)



def connectAgents(server):

    while True:
        
        try:

            conn, addr = server.accept()
            ip, _ = addr
            Agents[ip] = ['',conn]

            hearAgents(conn, ip)

        except ConnectionResetError:
            del Agents[ip]
            continue
            
        except:
            del Agents[ip]
            conn.close()
            continue
            


