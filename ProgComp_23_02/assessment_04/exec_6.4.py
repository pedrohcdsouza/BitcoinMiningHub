'''
Fazer um programa para gerar automaticamente uma lista (utilizar LIST COMPREHENSIONS) de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), 
com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente. Imprimir a lista original gerada, em seguida, ordená-la de forma crescente 
(usar laço de repetição) e imprimi-la. 

LEMBRANDO: NÃO USAR SORT() NEM SORTED()
'''

#pedrohcdsouza arquive

import random

n = int(input("LIST Create\nWrite the range: "))

if n <= 0:
    print("Write a valid number!")
else:
    listn = [random.randint(0, 99) for _ in range(n)] # OBS para depois: conseguir fazer uma váriavel receber listn sem modificar listn
    print(f"Original list: {listn}")
    for i in range(n):
        for j in range(n-1):
            if listn[j] > listn[j+1]:
                listn[j], listn[j+1] = listn[j+1], listn[j]
    print(f"Sorted list: {listn}")


                
                
                



