###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

import mylib

# Lendo o arquivo
ArcName = str(input("Please enter the desired filename (including the extension): "))
mylib.ArqReader(ArcName)

# Lendo o cabeçalho tcpdump
mylib.TcpDump(mylib.ArqReader[0])

