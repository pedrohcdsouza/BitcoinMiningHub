# Master Library Code

import socket, struct

def hearTransactions(): # Function to hear user-Transaction

    transactions = list() # Defining the List Transactions

    while True:

        try:

            print('Waiting for transactions ...\n')
            transaction = str(input('INPUT: '))

            if transaction == 'print': # Soluction for Print the List Transactions
                print(transactions)
                continue
            transactions.append(transaction)

        except Exception as exp:
            print('ERROR: Invalid transaction ...\n')
            continue
        
def connectMiners(server): # Function to connect miners

    while True:

        try: 

            connection, IP = server.accept() # Connecting the miner

        except:
            continue

        try:

            rawResponse = connection.recv(1)
            response = struct.unpack('c', rawResponse)


        except:
            continue
            