# Master Library Code

# LEMBRAR DE DEIXAR O CÓDIGO MAIS LIMPO

import struct, threading, sys

connectedAgents = dict() # Defining the Connected Agents
agentsList = list()
transactionsDict = dict() # Defining the Transactions List PS: It's a directory
foundedList = list()
tNumber = 0 # Transaction Number
nonceLock = threading.Lock()

def validateNonce(nonce, numTrans):
    return False

def StopingServer():
    for conn in agentsList:
        response = struct.pack('c', b'Q')  # PROTOCOL - Q

def FindNonce(numTrans):
    for conn in agentsList:
        response = struct.pack('!ci', b'I', numTrans) # PROTOCOL - I 
        conn.sendall(response)
    

def hear(bytes, connection): # Function to hear whatever

    try:
        data = connection.recv(bytes)
        while len(data) != bytes:
            data += connection.recv(1)
    except:
        connection.close()

def hearTransactions(): # Function to hear user-Transaction

    while True:

        try:
            
            global tNumber

            print('Waiting for transactions...\n')
            transaction = str(input('Write the transaction: \n'))
            bitsZero = int(input('Write the bitsZero: \n'))

            if transaction == 'print': # Soluction for Print the List Transactions
                print(f'Transactions: {transactionsDict}\nConnected Agents: {connectedAgents}')
                continue

            if transaction == 'exit': # Soluction for Close the Server
                print('Closing the server ...')
                sys.exit()

            transactionsDict[tNumber] = [bitsZero, transaction]
            tNumber += 1

        except Exception as exp:
            print('ERROR: Invalid transaction ...\n')
            continue

def connectAgents(server): # Function to connect agents

    while True:

        try: # Start of agent connection PS: finish line in 75

            connection, IP = server.accept() # Connecting the agent
            connectedAgents[f'{IP[0]}'] = '' # Adding the agent ip in dict
            agentsList.append(connection)

            while True:

                # Hearing the PROTOCOL-Type

                protocol = connection.recv(1)
                protocol = struct.unpack('c', protocol)
                protocol = protocol[0]

                # PROTOCOL - G

                if protocol == b'G':

                    name = hear(10, connection)
                    if name != bytes(10):
                        connectedAgents[f'{IP[0]}'] = name # Adding the agent name in Dict

                    if len(transactionsDict) == 0: # PROTOCOL - W

                        response = struct.pack('c', b'W')
                        connection.sendall(response) # Sending the protocol W
                        connection.close()
                    
                    # Separating data

                    for k, v in transactionsDict.items():
                        if k not in foundedList:
                            numTrans = k
                            bitsZero = transactionsDict[k][0]
                            actTrans = transactionsDict[k][1]
                            tranSize = len(actTrans)
                            break                        
                    numClient = len(connectedAgents)
                    winSize = 1000000

                    # Preparing a response

                    response = struct.pack(
                        f'!cHHIBI{tranSize}s',
                        b'T',
                        numTrans,
                        numClient,
                        winSize,
                        bitsZero, 
                        tranSize,
                        actTrans.encode()
                    )

                    connection.sendall(response) # Sending the protocol G
                
                # PROTOCOL - S

                if protocol == b'S':

                    data = hear(6, connection)
                    numTrans, nonce = struct.unpack('!Hi', data)
                    
                    with nonceLock:
                        if validateNonce(numTrans, nonce): # PROTOCOL - A
                            response = struct.pack('!ci', b'A', numTrans)
                            connection.sendall(response)

                            FindNonce(numTrans)

                            foundedList.append(numTrans)
                        else: # PROTOCOL - R
                            response = struct.pack('!ci', b'R', numTrans)
                            connection.sendall(response)

        except SystemExit:

            StopingServer()
            sys.exit()

        except: # finish agent line

            del connectedAgents[f'{IP[0]}']
            agentsList.remove(connection)
            continue
        



