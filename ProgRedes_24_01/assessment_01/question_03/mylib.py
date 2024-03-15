###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

import datetime

def ReadTcpDump(reader):
    TcpDump = reader.read(24)
    return TcpDump
def ReadArcHeader(reader):
    PacketHeader = reader.read(16)
    PacketTimeCap = datetime.datetime.fromtimestamp(PacketHeader[:3], 'little')
    CapLenght = PacketHeader[8:11]
    OrgLenght = PacketHeader[12:16]
    return PacketHeader, PacketTimeCap, CapLenght, OrgLenght
def ReadArc(reader, CapLenght, OrgLenght):
    ArcBroken = False
    if CapLenght != OrgLenght: ArcBroken = True
    VariableData = reader.read(CapLenght)
    
    


    




# with open(arqDir, 'rb') as r:
#     tcpdumpHEADER = r.read(24)
#     packetHEADER = r.read(16)
# MagicNumber = tcpdumpHEADER[0:4]
# print(MagicNumber)
# TimeStamp = datetime.datetime.fromtimestamp(int.from_bytes(packetHEADER[0:4], 'little'))
# print(TimeStamp)







