# Master Library Code

import socket, struct

connectedAgents = dict() # Defining the Connected Agents
transactionsDict = dict() # Defining the Transactions List PS: It's a directory
tNumber = 0 # Transaction Number

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

            # Hearing the G Protocol

            rawResponse = connection.recv(11) # G + 10 bytes
            try:

                while len(rawResponse) != 11:
                    rawResponse += connection.recv(1)

                protocol, name = struct.unpack('c10s', rawResponse)

            except:
                continue

            if protocol != b'G':
                continue

            if name != bytes(10): 
                connectedAgents[f'{agentIP[0]}'] = name

            

        except: # finish agent line

            del connectedAgents[f'{IP[0]}']
            continue
        



