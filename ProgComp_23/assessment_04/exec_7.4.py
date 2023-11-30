'''
A partir do arquivo relacao_alunos_alunos_ifrn.py, fazer um programa que:

Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser a sigla do campus e a segunda a quantidade de alunos daquele campus, no final deverá adicionada a cada sub-lista o percentual correspondente de alunos do campus em relação ao total de alunos do IFRN (limitar a 2 casas decimais);

Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o ano de ingresso do aluno e a segunda posição a quantidade de alunos que ingressaram naquele ano;

Liste os campus, peça ao usuário para escolher um e montar uma segunda lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o nome do curso e a segunda posição deverá ser quantidade de alunos daquele curso naquele campus.
'''

#pedrohcdsouza arquive

from relacao_alunos_alunos_ifrn import *

cnat = len((list(filter(lambda y: "CNAT" in y[1], alunos))))
print(cnat)