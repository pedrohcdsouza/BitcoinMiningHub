###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

# Verificando o diretório do programa.
import os, sys, mylib
from datetime import datetime                     
strDir = os.path.abspath(__file__)  
strDir = os.path.dirname(strDir)

# Váriaveis de pre-alocação.
PacketCab = {}
Packets = {}
BrokenPackets = 0
i1 = 0
i2 = 0
Payload = {}

# Criando um laço de repetição para solicitar o nome do arquivo (e abrindo-o). Tratando as exceções caso necessário.
while True:
    try:
        ArcName = str(input("Please enter the desired filename (including the extension): "))
        ArcDir = os.path.join(strDir, ArcName)
        with open(ArcDir, 'rb') as reader:
            # Salvando na memoria os dados do TCPDUMP.
            TcpDump = reader.read(24)
            #  Criando um laço de repetição para salvar na memoria os dados de cada pacote capturado.
            while True:
                PacketCab[i1] = reader.read(16)
                if not PacketCab[i1]:
                    break
                PacketLenght = int.from_bytes(PacketCab[i1][8:11], 'little')
                OrgLenght = int.from_bytes(PacketCab[i1][12:16], 'little')
                if PacketLenght != OrgLenght:
                    BrokenPackets += 1
                Packets[i1] = reader.read(PacketLenght)
                i1 += 1
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
    else:
        break

# Analisando os dados capturados.

FirstPacketTime = datetime.fromtimestamp(int.from_bytes(PacketCab[0][0:4], 'little'))
LastPacketTime = datetime.fromtimestamp(int.from_bytes(PacketCab[i1-1][0:4], 'little'))

print(f'\nThe first packet was captured at: {FirstPacketTime}.')
print(f'The last packet was captured at: {LastPacketTime}.')
print(f'The capture duration was: {LastPacketTime-FirstPacketTime} seconds.\n')

while True:
    try:
        UserChoose = str(input(f'\nDo you want to read a package?\nChoose the package index, or x to exit.\n'))

        if UserChoose == 'x':
            print("Finishing the program...")
            break
        else:
            UserChoose = int(UserChoose)
            print(f'Header:\n{PacketCab[UserChoose]}\nPacket:\n{Packets[UserChoose]}')
            continue
    except KeyError:
        print("The desired indice doesn't exists.")
        continue
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")

# Obs: O código está incompleto, e não foi utilizado o mylib. Pórem, a lógica do que deveriamos fazer está lá. Um While True que chama cada função de leitura de cabeçalho.





