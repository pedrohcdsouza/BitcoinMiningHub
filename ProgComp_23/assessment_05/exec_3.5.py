import os, sys

# ## Obtendo diretorio atual
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
#

# ## Abrindo e lendo arquivo
strNomeArq = strDiretorio + '\\relacao_servidores_ifrn.csv'
arqLeitura = open(strNomeArq, 'r', encoding='utf-8')
cabecalho = arqLeitura.readline()[-1]
lstComponentes = list()
while True:
    strLinha = arqLeitura.readline()[:-1]
    if not strLinha: break
    strLinha = strLinha.split(';')
    lstComponentes.append(strLinha)
arqLeitura.close()


