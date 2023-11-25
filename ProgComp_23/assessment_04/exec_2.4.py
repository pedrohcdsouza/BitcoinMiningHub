'''Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), 
com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente. Para gerar a lista deverá ser utilizado LIST COMPREHENSIONS. 
Após a lista ser gerada, o programa deverá informar as quantidades de elementos que estão no 1º quartil (valores entre 0 e 24), no 2º quartil (entre 25 e 49), 
no 3º quartil (entre 50 e 74) e no 4º quartil (entre 75 e 99).'''

#pedrohcdsouza arquive

import random

n = int(input("LIST Create\nWrite the range of your list: "))
listn = list()
firstq = list()
secondq = list()
thirstq = list()
fourq = list()

if n < 0:
    print("Write a valid number!")
else:
    a = 0
    while a < n:
        listn.append(random.randint(0,99))
        a += 1
    for i in listn:
        if i >= 0 and i <= 24:
            firstq.append(i)
        elif i >= 25 and i <= 45:
            secondq.append(i)
        elif i >= 50 and i <= 74:
            thirstq.append(i)
        else:
            fourq.append(i)
    print(f"primeira lista {firstq}") 
    print(f"segunda lista {secondq}")
    print(f"terceira lista {thirstq}")
    print(f"quarta lista {fourq}")         


