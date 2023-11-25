'''
Faça um programa que solicite ao usuário um valor decimal positivo (esse valor corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

O programa deverá continuar solicitando saques até que seja informado o valor 0 (zero).

Ao término, o programa deverá listar todos os saques efetuados, mostrando quais cédulas/moedas foram entregues e o valor total dispensando.
'''

#pedrohcdsouza arquive

value = list()

while True:
    n = float(input("Write a value: "))
    if n == 0:
        break
    elif n < 0.01:
        print("Write a valid number!")
        quit()
    else:
        value.append(n)
valuesum = value.sum()*100 #multiplicado por 100 para remover os centavos.


