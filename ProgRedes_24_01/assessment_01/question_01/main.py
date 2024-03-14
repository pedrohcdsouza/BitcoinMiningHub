###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 10/03/2024                                           #
#                                                             #
###############################################################

# Verificando o diretório do programa.
import os, sys                     
strDir = os.path.abspath(__file__)  
strDir = os.path.dirname(strDir)   

# Criando um laço de repetição para solicitar o nome do arquivo (e abrindo-o), e a palavra-chave desejada. Tratando as exceções caso necessário.
while True: 
    try:
        ArcName = str(input("Please enter the desired filename (including the extension): "))
        ArcDir = os.path.join(strDir, ArcName)
        with open(ArcDir,'rb') as Arc_rb:
            ArcData = Arc_rb.read()
        if not ArcData:
            print("\nThe file is empty. Please provide a non-empty file.\n")
            continue
        Keyword = str(input("Please enter a cripto keyword: "))
        if not Keyword:
            print("\nThe password is empty. Please provide a non-empty Keyword.\n")
            continue
        KeyLen = len(Keyword)
    except FileNotFoundError:
        print("\nThe desired file was not found!\nTry again...\n")
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
        sys.exit()
    else:
        break

# Verificando a posição atual byte do texto, e do byte da palavra-chave. E utilizando o operador xor (^).
BytesList = []
for i, byte in enumerate(ArcData):
    byte_password = ord(Keyword[i % KeyLen])
    BytesList.append(byte ^ byte_password)

# Criando um laço de repetição para solicitar o nome do arquivo (e cria-lo), escrevendo no arquivo cada byte 'criptografado' que foi colocado dentro da lista (BytesList). Tratando as exceções caso necessário.
while True:
    try:
        ArcDest = str(input("Please enter the destination file name: "))
        ArcDestDir = os.path.join(strDir, ArcDest)
        if os.path.exists(ArcDestDir):
            print("\nThe file already exists. Please provide a another name file.\n")
            continue
        with open(ArcDestDir, 'wb') as Arc_wb:
            for byte in BytesList:
                Arc_wb.write(byte.to_bytes(1, byteorder='big'))
    except FileNotFoundError:
        print("\nThe file name is invalid!\nCtrl^ to exit.\n")
        continue
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
        sys.exit()
    else:
        break