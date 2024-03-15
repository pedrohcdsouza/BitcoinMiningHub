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
    
    MACDest = VariableData[:5]
    MACSour = VariableData[6:11]
    Type = VariableData[12:13]
    Payload = VariableData[14:len(VariableData-18)] # -18 Bytes por que é a quantidade para capturar apenas o Payload (FCS,MacDes,MacOrg,CRC)





