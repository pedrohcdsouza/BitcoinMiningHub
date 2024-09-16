import struct, hashlib, threading, sys, requests

# STATIC VARIABLES

TOKEN = '7281019772:AAEsW8LSoxz5BLl5zDGMCiAQrYhLZSIm9mw'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
threadLock = threading.Lock()

# DYNAMIC VARIABLES

agents = dict()
transactions = dict()
founded = list()

def getUpdates(offset=None):
    url = f'{BASE_URL}/getUpdates'
    params = {'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def sendMessage(chat_id, text):
    url = f'{BASE_URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=payload)
    return response.json()

def startBot():
    offset = None
    while True:
        updates = getUpdates(offset)
        for update in updates.get('result', []):
            chat_id = update['message']['chat']['id']
            text = update['message']['text']
            if text == '/start':
                sendMessage(chat_id, 'Bitcoin Server Commands:\n/validtrans\n/pendtrans\n/clients')
            elif text == '/validtrans':
                validTrans = [f'{k}:{v}' for k, v in transactions.items() if k in founded]
                sendMessage(chat_id, validTrans)
            elif text == '/pendtrans':
                pendTrans = [f'{k}:{v}' for k, v in transactions.items() if k not in founded]
                sendMessage(chat_id, pendTrans)
            elif text == '/clients':
                clients = [f'{k}:{v[0]}' for k, v in agents.items()]
                sendMessage(chat_id, clients)
            else:
                sendMessage(chat_id, 'ERROR: Invalid command ...')
            offset = update['update_id'] + 1

def writeTransactions(sock):
    
    t = 1

    while True:

        try:

            commands = str(input(''))

            if commands == '/newtrans':
                transaction = str(input('WRITE THE TRANSACTION:\n'))
                bits = int(input('WRITE THE BITS TO BE ZERO:\n'))

                transactions[t] = [bits, transaction]
                t += 1
            
            elif commands == '/validtrans':
                validTrans = [f'{k}:{v}' for k, v in transactions.items() if k in founded]
                print(f'FOUNDED LIST:\n{validTrans}')
            
            elif commands == '/pendtrans':
                pendTrans = [f'{k}:{v}' for k, v in transactions.items() if k not in founded]
                print(f'TRANSACTIONS LIST:\n{pendTrans}')
            
            elif commands == '/clients':
                clients = [f'{k}:{v[0]}' for k, v in agents.items()]
                print(f'CONNECTED AGENTS:\n{clients}')

            elif commands == '/close':
                response = struct.pack('c', b'Q')

                for i in agents.items():

                        allConn = i[1][1]
                        allConn.sendall(response)
                
                sys.exit()
            
            else:
                print('ERROR: Invalid command ...\n')

        except SystemExit:
            print('THE SERVER WAS CLOSED ...\n')
            break

        except Exception as exp:
            print('ERROR: Invalid command ...\n')
            print(exp)
            continue



def hearAgents(conn, ip):

    while True:

        protocol = conn.recv(1)
        protocol = struct.unpack('c', protocol)
        protocol = protocol[0]
        
        if protocol == b'G': # PROTOCOL - G
            name = conn.recv(10)
            while len(name) != 10:
                name += conn.recv(1)
            name = struct.unpack('!10s', name)
            agents[ip] = [name,conn]

            if len(transactions) == 0 or len(transactions) == len(founded): # PROTOCOL - W
                response = struct.pack('c', b'W')
                conn.sendall(response)
          
            else: # PROTOCOL - T

                for k,i in transactions.items():

                    if k not in founded:

                        numT = k
                        numA = len(agents)
                        winS = 1000000
                        bits = i[0]
                        size = len(i[1])
                        tran = i[1]

                        if isinstance(tran, str):
                            tran = tran.encode('utf-8')

                        response = struct.pack(f'!cHHIBI{size}s', b'T',numT,numA,winS,bits,size,tran)
                        conn.sendall(response)
                        break

        elif protocol == b'S': # PROTOCOL - S
            
            with threadLock:

                data = conn.recv(6)
                while len(data) != 6:
                    data += conn.recv(1)
                numT, nonce = struct.unpack('!HI', data)

                bits, trans = transactions[numT]

                if isinstance(trans, str): 
                    trans = trans.encode('utf-8')
                
                nonceValue = struct.pack('I', nonce)
                transHash = hashlib.sha256(nonceValue + trans).digest()
                transBin = ''.join(format(byte, '08b') for byte in transHash)

                if transBin[:bits] == '0' * bits: # PROTOCOL - A and I

                    founded.append(numT)
                    response = struct.pack('!cH', b'A',numT)
                    conn.sendall(response)
                    print(f'\nTRANSACTION {numT}: FOUNDED by {name}\n')

                    response = struct.pack('!cH', b'I',numT)

                    for i in agents.items():
                        allConn = i[1][1]
                        allConn.sendall(response)
                
                else: # PROTOCOL - R

                    response = struct.pack('!cH', b'R', numT)

def connectAgents(sock):

    while True:
        
        try:

            conn, addr = sock.accept()
            ip, _ = addr
            agents[ip] = ['',conn]
            hearAgents(conn, ip)

        except ConnectionResetError:
            del agents[ip]
            continue
            
        except:
            del agents[ip]
            conn.close()
            continue