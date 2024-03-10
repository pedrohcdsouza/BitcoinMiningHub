'''
Fazer um programa para gerar automaticamente uma lista (utilizar LIST COMPREHENSIONS) de dimensão de n elementos (n deverá ser solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente. Determinar (usar laço de repetição – NÃO USAR a biblioteca statistics.py): 

A média dos valores dos elementos da lista; 
A mediana dos valores dos elementos da lista;
A variância populacional dos valores dos elementos da lista;
O desvio-padrão populacional dos valores dos elementos da lista.
Para fins de conferência, o aluno poderá utilizar as funções mean(), median(), pvariance() e pstdev() da biblioteca statistics.py.
'''

#pedrohcdsouza arquive

import random

n = int(input("Write a value: "))
if n <= 0:
    print("Write a valid number!")
else:
    listn = sorted([random.randint(0,99) for _ in range(n)])

    if n % 2 == 0: # Checking if it's odd or even to get the median
        median = (listn[n//2] + listn[(n//2)-1])/2

    else:
        median = listn[n//2]
    
    media = 0
    variance = 0
    for i in listn:
        media += i/n

    for i in listn:
        variance += ((i-media)**2)/n

    devitation = variance**(1/2)

    print(f'The list "{listn}" has\nAVARAGE: "{media:.2f}"\nMEDIAN: "{median:.2f}"\nPOPULATION VARIANCE: "{variance:.2f}"\nSTANDART DEVITATION: "{devitation:.2f}"\n')


    
    

