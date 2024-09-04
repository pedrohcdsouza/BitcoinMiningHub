###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 12/03/2024                                           #
#                                                             #
###############################################################



import time, hashlib

# Criando DefUSER para calcular o hashlib desejado.
def findNonce(dataToHash, bitsToBeZero):

    print('\nCódigo em execução... \n')

    StartTime = time.time()
    Nonce = 0

    while True:
        HashLib = hashlib.sha256()

        dataBytes = dataToHash.encode('utf-8')
        # Adicionando o valor de Nonce para 4 bytes.
        nonceBytes = Nonce.to_bytes(4, byteorder='big')
        HashLib.update(dataBytes + nonceBytes)
        HashHex = HashLib.hexdigest()
        # Transformando o Hash para binário, assim, podendo ler os seus bits.
        HashBin = format(int(HashHex, 16), '0256b')
        if HashBin[0:int(bitsToBeZero)] == '0'*int(bitsToBeZero):
            break
        else:
            Nonce += 1

    EndTime = time.time()
    ProgramTime = round(EndTime-StartTime,3)

    return Nonce, ProgramTime, HashHex