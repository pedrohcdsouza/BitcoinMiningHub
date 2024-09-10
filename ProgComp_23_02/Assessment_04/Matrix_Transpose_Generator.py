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

