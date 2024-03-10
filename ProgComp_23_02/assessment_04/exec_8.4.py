'''
Desenvolva um programa em Python que solicite ao usuário dois valores inteiros: o primeiro representando a quantidade de listas na matriz e o segundo indicando a quantidade de elementos em cada lista. Com base nesses valores, o programa deve gerar aleatoriamente os elementos da matriz, exibir a matriz original e, em seguida, calcular e apresentar a matriz transposta.

A matriz transposta de uma matriz M com m linhas e n colunas é obtida trocando as linhas pelas colunas e vice-versa, resultando em uma matriz Mt com n linhas e m colunas.
'''

#pedrohcdsouza arquive

import random

columns_range = int(input("MATRIZ\nWrite the column range:  ")) #coluna
rows_range = int(input("Now, write the row range:  ")) #linha

if columns_range <= 0 or rows_range <= 0:
    print("Write valid number!")
else:
    matrix = [[random.randint(0,9) for _ in range(columns_range)] for _ in range (rows_range)] #matriz
    matrix_transpose = [list(i) for i in zip(*matrix)]

    print("MATRIX LIST:")
    for i in matrix:
        print(i)
    print("MATRIX TRANPOSE LIST:")
    for i in matrix_transpose:
        print(i)

