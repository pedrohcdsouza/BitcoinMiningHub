#pedrohcdsouza arquive


import csv,os
STRDIR = os.path.abspath(__file__)
STRDIR = os.path.dirname(STRDIR)+'\\archives'


# ## Opening the archive and reading only the required data
with open(STRDIR +'\\ca-2017-01.csv','r',encoding='utf-8') as READarq:
    lstArq_data = list() # Default List
    lstFlag = list()
    lstProd = list()
    Reader = csv.reader(READarq, delimiter = ';')
    Header = READarq.readline()[:-1]
    for line in Reader:
        lstFlag.append(line[15])
        lstProd.append(line[10])
        dados = [line[0],line[1],line[10],line[11],line[12],line[15]]
        lstArq_data.append(dados)
#

# ## Opening one archive and writing the required data
with open(STRDIR +'\\serie_historica_anp.csv','w',encoding='utf-8') as WRITEarq:
    Header = ['Regiao – Sigla', 'Estado – Sigla', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Bandeira']
    lstArq_serie = lstArq_data
    lstArq_serie.insert(0,Header)
    for line in lstArq_serie:
        strLine = ';'.join([str(item) for item in line])
        WRITEarq.write(f'{strLine}\n')
#

# ## Coding LIST A 
lstFlag = set(lstFlag) #Name of each product
lstProd = set(lstProd) #Name of each flag'
