#pedrohcdsouza arquive

import os
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# ## Abrindo o arquivo
with open(strDiretorio + '\\relacao_servidores_ifrn.csv','r',encoding='utf-8') as arqLeitura:
    lstComponentes = list()
    while True:
        remCabecalho = arqLeitura.readline()[:-1]
        strLinha = arqLeitura.readline()[:-1]
        if not strLinha: break
        strLinha = strLinha.split(';')
        lstComponentes.append(strLinha)
#

# ## Separando dados da Lista A
siglas = {}
for tipo in lstComponentes:
    if tipo[11] not in siglas:
        siglas[tipo[11]] = [tipo[1]]
    else:
        if tipo[1] not in siglas[tipo[11]]:
            siglas[tipo[11]].append(tipo[1])

# Montando e criando arquivo da lista A
lista_a = [[sigla, len(tipos)] for sigla, tipos in siglas.items()]
# print(lista_a)

with open(strDiretorio + '\\servidores_campi.csv','w',encoding='utf-8') as arqEscrita:
    strCabecalho = ['campus', 'tipos_de_servidores']
    lista_a.insert(0,strCabecalho)

    for linha in lista_a:
        strLinha = ';'.join([str(item) for item in linha])
        arqEscrita.write(f'{strLinha}\n')

# ## Separando dados da Lista B
filterDocentes = lambda x:x[0] == 'docente'
lstDocentes = list(filter(filterDocentes,lstComponentes))
setDisciplinas = set(map(y,lstDocentes))




