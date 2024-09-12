# Master Library Code

import socket, struct

connectedAgents = dict() # Defining the Connected Agents
transactionsDict = dict() # Defining the Transactions List PS: It's a directory
tNumber = 0 # Transaction Number
numClient = 0

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
            
            transaction = str(input('Waiting for Transactions...\n'))
            print('print for see the data...\n\n')

            if transaction == 'print': # Soluction for Print the List Transactions
                print(f'Transactions: {transactionsDict}\nConnected Agents: {connectedAgents}')
                continue

            transactionsDict[tNumber] = transaction
            tNumber += 1

        except Exception as exp:
            print('ERROR: Invalid transaction ...\n')
            continue

def connectAgents(server): # Function to connect agents

    while True:

        try: # Start of agent connection PS: finish line in 75

            connection, IP = server.accept() # Connecting the agent
            connectedAgents[f'{IP[0]}'] = ''

            # Hearing the PROTOCOL-Type
            
            while True:

                protocol = connection.recv(1)
                protocol = struct.unpack('c', protocol)

                # PROTOCOL - G

                if protocol == b'G':
                    
                    name = hear(10, connection)
                    if name != bytes(10):
                        connectedAgents[f'{IP[0]}'] = name

                    if len(transactionsDict) == 0:
                        response = struct.pack('c', b'W')
                        connection.sendall(response)
                        connection.close()
                    
                    numTrans = transactionsDict[len(transactionsDict) - 1]

                    
                    

                    




        except: # finish agent line

            del connectedAgents[f'{IP[0]}']
            continue
        



