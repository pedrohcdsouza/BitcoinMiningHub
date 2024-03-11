###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 10/03/2024                                           #
#                                                             #
###############################################################

import os, sys

strDir = os.path.abspath(__file__)
strDir = os.path.dirname(strDir)

while True:
    try:
        ArcName = str(input("Please enter the desired filename (including the extension): "))
        ArcDir = os.path.join(strDir, ArcName)
        with open(ArcDir,'rb') as Arc_rb:
            ArcData = Arc_rb.read()
        Keyword = str(input("Please enter a keyword: "))
        KeyLen = len(Keyword)
    except FileNotFoundError:
        print("\nThe desired file was not found!\nTry again...\n")
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
        sys.exit()
    else:
        break

BytesList = []
for i, byte in enumerate(ArcData):
    byte_password = ord(Keyword[i % KeyLen])
    BytesList.append(byte ^ byte_password)

while True:
    try:
        ArcDest = str(input("Please enter the destination file name: "))
        ArcDestDir = os.path.join(strDir, ArcDest)

        with open(ArcDestDir, 'wb') as Arc_wb:
            for byte in BytesList:
                Arc_wb.write(byte.to_bytes(1, byteorder='big'))
    except FileNotFoundError:
        print("\nThe file name is invalid!\n")
        usercommand = str(input("\nPress 0 -> Exit\nPress 1 -> Return\n"))
        if usercommand == 0:
            sys.exit()
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
        sys.exit()
    else:
        break