# mainmenu.py

import random

def escolherOPCAO(opt, dictCartelas):
    if not isinstance(opt, int) or opt < 1 or opt > 4:
        return None
    elif opt == 1:
        for cartela in range(1, 25):
            dictCartelas[cartela] = {
                "B": [random.randint(1, 15) for _ in range(5)],
                "I": [random.randint(16, 30) for _ in range(5)],
                "N": [random.randint(31, 45) for _ in range(5)]
            }
        return dictCartelas
