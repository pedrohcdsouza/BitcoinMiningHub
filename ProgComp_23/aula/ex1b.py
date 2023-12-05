from exemplo_01 import *

arqSaida = open('nordeste.txt','w',encoding='UTF-8')
p = 0

arqOrd = sorted(lstCapitais,key=lambda c:c[2],reverse=True)


for cidade in lstCapitais:
    arqSaida.write(f'{cidade[1]}/{cidade[0]}:{cidade[2]}\n')
    p += cidade[2]

arqSaida.write(f'Cidade mais populosa: {arqOrd[0]}\n')
arqSaida.write(f'População total: {p}')
arqSaida.close()