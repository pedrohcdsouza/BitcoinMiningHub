# Master Library Code

import socket, struct

connectedAgents = dict() # Defining the Connected Agents
transactionsDict = dict() # Defining the Transactions List PS: It's a directory
foundedDict = dict()
tNumber = 0 # Transaction Number

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
                    connection.sendall(response)
                    connection.close()
                
                # Separating data

                for k, v in transactionsDict.items():
                    if v not in foundedDict:
                        bitsZero = v[0]
                        actTrans = v[1]
                        tranSize = len(actTrans)
                    break                        
                numTrans = transactionsDict[len(transactionsDict) - 1]
                numClient = len(connectedAgents)
                winSize = 1000000

                # Preparing a response

                response = struct.pack(
                    f'!HHIBI{tranSize}s',
                    numTrans,
                    numClient,
                    winSize,
                    bitsZero, 
                    tranSize,
                    actTrans
                )


                

                




        except: # finish agent line

            del connectedAgents[f'{IP[0]}']
            continue
        



