'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos 
(n deverá ser solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros 
entre 0 e 999 (inclusive), gerados aleatoriamente. Para gerar a lista deverá ser 
utilizado LIST COMPREHENSIONS. Após a lista ser gerada o programa deverá solicitar um valor inteiro, 
informar se ele consta na lista, quantas ocorrências dele há na lista e quais as suas posições.
'''

#pedrohcdsouza arquive

import random

n = int(input("LIST Create\nWrite the number: "))
listn = list()
count = 0
pos = list()

if n < 0:
    print("Write a valid number!")
else:
    a = 0
    while a < n:
        listn.append(random.randint(0,999))
        a += 1
    verificator = int(input("Write a verificator number: "))
    if verificator not in listn:
        print("Verificador não está!")
    else:
        for i in listn:
            if i == verificator:
                count += 1
                pos.append(i)
        print(f"O verificador {verificator} apareceu {count} vezes nas posições {pos}")
                




