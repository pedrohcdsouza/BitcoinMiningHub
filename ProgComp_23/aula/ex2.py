from exemplo_02 import *

arqSaida = open('nordeste_2.txt','w',encoding='UTF-8')

for k,v in dictNE.items():
    arqSaida.write(f'{v["capital"]}\n')
arqSaida.close()