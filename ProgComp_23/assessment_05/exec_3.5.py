#pedrohcdsouza arquive

import os
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# ## Abrindo o arquivo
with open(strDiretorio + '\\relacao_servidores_ifrn.csv','r',encoding='utf-8') as arqLeitura:
    strCabecalho = arqLeitura.readline()[:-1]
    lstComponentes = list()
    while True:
        strLinha = arqLeitura.readline()[:-1]
        if not strLinha: break
        strLinha = strLinha.split(';')
        lstComponentes.append(strLinha)
#

# ## Separando dados
siglas = []
for sigla in lstComponentes:
    if sigla[11] not in str(siglas):
        siglas.append([sigla[11]])

#

# ## Montando a lista A
lista_a = siglas
for tipo in lstComponentes:
    if tipo[1] not in lista_a[siglas.index(tipo[11])]:
        lista_a[siglas.index(tipo[11])].append(tipo[1])


    
    
    
    

    
    


        
    


