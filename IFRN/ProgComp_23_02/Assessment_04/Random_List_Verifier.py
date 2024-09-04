#pedrohcdsouza arquive

import random

n = int(input("LIST Create\nWrite the number: "))
pos = []
count = 0
pos_n = 0

if n < 0:
    print("Write a valid number!")
else:
    listn = [random.randint(0,999) for _ in range(n)]

    verificator = int(input("Write a verificator number: "))

    if verificator not in listn:
        print("Verificator not in!")
    else:
        for i in listn:
            pos_n += 1
            if i == verificator:
                count += 1
                pos.append(pos_n)
        print(f"The verifier {verificator} has appeared {count} times in {pos} positions")