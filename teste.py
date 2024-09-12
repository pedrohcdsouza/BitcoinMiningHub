import struct

transactionsDict = dict()
transactionsDict[0] = [5, 'oi']
transactionsDict[1] = [6, 'pedro']

foundedDict = dict()
foundedDict[0] = [5, 'oi']

connectedAgents = ['pedro', 'joao', 'leticia']

# Itera pelas transações e pega a primeira que não está no foundedDict
for k, v in transactionsDict.items():
    if v not in foundedDict.values():
        bitsZero = v[0]
        actTrans = v[1]
        tranSize = len(actTrans)
        break                        

# Dados necessários
numTrans = len(transactionsDict)  # Número de transações
numClient = len(connectedAgents)   # Número de clientes conectados
winSize = 1000000                  # Tamanho da janela
bitsZero = bitsZero                # Bits zero iniciais
tranSize = tranSize                # Tamanho da transação

# Empacota os valores com struct.pack
response = struct.pack(
    '!HHIBI',  # Formato: 2 bytes (H), 2 bytes (H), 4 bytes (I), 1 byte (B), 4 bytes (I)
    numTrans,  # Número da transação (2 bytes)
    numClient, # Número de clientes (2 bytes)
    winSize,   # Tamanho da janela (4 bytes)
    bitsZero,  # Número de bits zero (1 byte)
    tranSize   # Tamanho da transação (4 bytes)
)

print(response)
