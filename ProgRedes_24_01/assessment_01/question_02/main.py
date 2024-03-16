###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 12/03/2024                                           #
#                                                             #
###############################################################

import sys
from mylib import *

if len(sys.argv) == 3:
    Nonce, ProgramTime, HashHex = findNonce(sys.argv[1],sys.argv[2])
    print(f'Number of attempts: {Nonce} Nonces.')
    print(f'Program time: {ProgramTime} Seconds.')
    print(f'Hashlib hexa: {HashHex}.')
else:
    print("\nPlease enter 2 arguments.\n")