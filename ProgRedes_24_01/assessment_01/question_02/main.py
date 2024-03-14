###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 12/03/2024                                           #
#                                                             #
###############################################################

import sys
from mylib import *

if len(sys.argv) == 3:
    findNonce(sys.argv[1],sys.argv[2])
else:
    print("\nPlease enter 2 arguments.\n")
    sys.exit()