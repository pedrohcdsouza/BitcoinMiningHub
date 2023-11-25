'''
Fazer um programa para gerar automaticamente uma lista (utilizar LIST COMPREHENSIONS) de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), 
com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente. Imprimir a lista original gerada, em seguida, ordená-la de forma crescente 
(usar laço de repetição) e imprimi-la. 

LEMBRANDO: NÃO USAR SORT() NEM SORTED()
'''

#pedrohcdsouza arquive

import random

n = int(input("LIST Create\nWrite the range: "))

listn = [random.randint(0, 99) for _ in range(n)]
#print(listn)
listninverse = []

while 


