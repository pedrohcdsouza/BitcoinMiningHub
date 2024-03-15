###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

import os

strDir = os.path.abspath(__file__)  
strDir = os.path.dirname(strDir)   

#Funções Padrão
def ArqReader(Archive_Name):
    ArcDir = os.path.join(strDir, Archive_Name)
    with open(ArcDir,'rb') as Arc_rb:
        while True:
            Data = Arc_rb.read(16)
            if not Data:
                break
            BytesList = [f'{byte:02x}' for byte in Data]
    return BytesList

def TcpDump(BinData):
    TcpDHeader = BinData.read(24)
    MagicNumber = TcpDHeader.read(4)
    if hex(MagicNumber) == 'A1B2C3D4':
        TimeStamps = 0 # Isso significa que está em segundos e microssegundos.
    else:
        TimeStamps = 1 # Isso significa que está em microssegundos e nanossegundos.
    MajorVersion = int(TcpDHeader.read(2))
    MinorVersion = int(TcpDHeader).read(2)
    Reserved1 = TcpDHeader.read(4)
    Reserved2 = TcpDHeader.read(4)
    SnapLen = TcpDHeader.read(4)
    LinkType = TcpDHeader.read(4)
    return MagicNumber,TimeStamps,MajorVersion,MinorVersion,Reserved1,Reserved2,SnapLen,LinkType

#Funções Ethernet
    