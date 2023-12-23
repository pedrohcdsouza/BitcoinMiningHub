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
zonaleste = 0
for i in lstComponentes:
    if i[11] == "ZL":
        zonaleste += 1
print(zonaleste)
        
    


