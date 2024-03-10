###############################################################
#                                                             #
#  Author @pedrohcdsouza                                      #
#  Date: 10/03/2024                                           #
#                                                             #
###############################################################

import os, sys

strDir = os.path.abspath(__file__)
strDir = os.path.dirname(strDir)

ArcName = str(input("Please enter the desired filename (including the extension): "))
ArqDir = strDir + f'/{ArcName}'

with open(ArqDir,'r') as Arc_r:
    ArcData = Arc_r.readlines()

Keyword = str(input("Please enter a keyword: "))










ArcDest = str(input("Please enter the destination file name: "))