from cotacao_dolar import *

#pedrohcdsouza arquive

listdolar = list()
listdolaravarage = list()
min = 0
max = 0
avg = 0

for i in cotacoes_dolar:
    if "2022-01" in i[0]:
        if i[1] > max:
            max = i
        if i[1] < min:
            min = i
print(min,max)




        
    