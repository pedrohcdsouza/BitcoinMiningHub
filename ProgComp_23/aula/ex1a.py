from exemplo_01 import *

arqSaida = open('nordeste.txt','w',encoding='UTF-8')
p = 0


for cidade in lstCapitais:
    arqSaida.write(f'{cidade[1]}/{cidade[0]}:{cidade[2]}\n')
    p += cidade[2]
arqSaida.write(f'População total: {p}')
arqSaida.close()

