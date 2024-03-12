###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 12/03/2024                                           #
#                                                             #
###############################################################

###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 12/03/2024                                           #
#                                                             #
###############################################################

import time, hashlib

def findNonce(dataToHash, bitsToBeZero):
    print('Código em execução... ')

    StartTime = time.time()
    nonce = 0
    while True:
        h = hashlib.sha256()
        dataBytes = dataToHash.encode('utf-8')  # Convertendo a string em bytes
        nonceBytes = nonce.to_bytes(4, byteorder='big')
        h.update(dataBytes + nonceBytes)
        h_bin = ''.join(format(byte, '08b') for byte in h.digest())

        if h_bin[0:bitsToBeZero] == '0'*bitsToBeZero:
            break
        else:
            nonce += 1
            print(nonce)

    EndTime = time.time()

    print(nonce)
    print(f'O tempo foi: {round(EndTime-StartTime,2)} segundos.')
    print(h.hexdigest())

