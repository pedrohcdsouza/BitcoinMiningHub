'''Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), 
com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente. Para gerar a lista deverá ser utilizado LIST COMPREHENSIONS. 
Após a lista ser gerada, o programa deverá informar as quantidades de elementos que estão no 1º quartil (valores entre 0 e 24), no 2º quartil (entre 25 e 49), 
no 3º quartil (entre 50 e 74) e no 4º quartil (entre 75 e 99).'''

#pedrohcdsouza arquive

import random

n = int(input("LIST Create\nWrite the range of your list: "))
listn = list()
x = random(0,99)

if n < 0:
    print("Write a valid number!")
else:
    a = 0
    while a < n:
        listn.append(x)
        a += 1
    print(listn)

