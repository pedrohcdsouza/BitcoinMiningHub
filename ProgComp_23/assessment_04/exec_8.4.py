'''
Desenvolva um programa em Python que solicite ao usuário dois valores inteiros: o primeiro representando a quantidade de listas na matriz e o segundo indicando a quantidade de elementos em cada lista. Com base nesses valores, o programa deve gerar aleatoriamente os elementos da matriz, exibir a matriz original e, em seguida, calcular e apresentar a matriz transposta.

A matriz transposta de uma matriz M com m linhas e n colunas é obtida trocando as linhas pelas colunas e vice-versa, resultando em uma matriz Mt com n linhas e m colunas.
'''

#pedrohcdsouza arquive

import random

coluna_range = int(input("MATRIZ\nWrite your matriz: "))
linha_range = int(input("Write the linha: "))

coluna = [random.randint(0,9) for _ in range(coluna_range)]
linha = [random.randint(0,9) for _ in range (linha_range)]

print(coluna)
print(linha)

