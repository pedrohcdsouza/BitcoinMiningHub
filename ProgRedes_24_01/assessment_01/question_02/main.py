###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 12/03/2024                                           #
#                                                             #
###############################################################

import sys
from mylib import *

if sys.argv >= 2:
    findNonce(sys.argv[1],sys.argv[2])
else:
    print("\nPlease enter 2 arguments.\n")
    sys.exit()