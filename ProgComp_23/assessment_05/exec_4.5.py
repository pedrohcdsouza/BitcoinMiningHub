#pedrohcdsouza arquive

import csv,os

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)+'\\archives'

lista_arquivos = []
with open(strDiretorio +'\\ca-2017-01.csv','r',encoding='utf-8') as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        lista_arquivos.append(linha[0])
print(lista_arquivos)
                           
        
        