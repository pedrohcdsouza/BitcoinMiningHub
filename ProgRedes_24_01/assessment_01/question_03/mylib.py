###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

# Função para Leitura de cada cabeçalho.

def Ethernet(Packet, Indice):
    LenPacket = len(Packet)
    Payload = {}
    # Obs: A leitura é de LenPacket -4, pois os últimos 4 bytes são reservados ao FCS.
    Payload[Indice] = Packet[Indice][21:LenPacket-4]

    return Payload, Indice

def Ip(Payload, Indice):
    IpProtocol = Payload[Indice][9]
    SourceAddress = Payload[Indice][12:16]
    DestAddress = Payload[Indice][17:20]
    return IpProtocol, SourceAddress, DestAddress