###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

import os

# Verificando o diretório do programa.
strDir = os.path.abspath(__file__)  
strDir = os.path.dirname(strDir)

# Criando um laço de repetição para solicitar o nome do arquivo desejado.
PacketsCab = {}
Packets = {}
i = 0
while True: 
    try:
        ArcName = input("Please enter the desired filename (including the extension): ")
        ArcDir = os.path.join(strDir, ArcName)
        with open(ArcDir, 'rb') as reader:
            TcpDumpHEADER = reader.read(24)
            if not TcpDumpHEADER:
                print("\nThe file is empty. Please provide a non-empty file.\n")
                continue
            while True:
                packet_cab = reader.read(16)
                if not packet_cab:
                    break
                PacketsCab[i] = packet_cab
                length_bytes = reader.read(4)
                if not length_bytes:
                    break
                length = int.from_bytes(length_bytes, byteorder='little')
                packet_data = reader.read(length)
                Packets[i] = packet_data
                i += 1
    except Exception as exc:
        print(exc)
        break
    else:
        break


    