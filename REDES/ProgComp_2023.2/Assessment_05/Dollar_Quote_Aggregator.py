#pedrohcdsouza arquive

import requests,os,datetime,sys
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

print(f"DOLLAR QUOTE\n")

current_date = datetime.date.today()
tester = []

# ## Abrindo o arquivo do ano selecionado
while True:
    try:
        wanted_year = int(input("Choose a year (0 to stop): "))
        if wanted_year == 0: 
            sys.exit()
        elif wanted_year > current_date.year: 
            print("ERROR: O ano inserido é maior que o ano atual.")
        else:
            strURL = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
            strURL += f'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
            strURL += f'@dataInicial=%2701-01-{wanted_year}%27&@dataFinalCotacao=%2712-31-{wanted_year}%27&$format=json'
            dictCotacoes = requests.get(strURL).json()
            if dictCotacoes['value'] != tester: 
                break
            else:
                print("ERROR: O ano inserido não possuí arquivos na database.")
                continue
    except SystemExit:
        print("Finalizando o programa...")
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
# print(dictCotacoes)
#
        
# ## Tratando os dados
lstMonth = []
dictMonth = {'JAN':'01','FEV':'02','MAR':'03','ABR':'04','MAI':'05','JUN':'06','JUL':'07','AGO':'08','SET':'09','OUT':'10','NOV':'11','DEZ':'12'}
meses = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
for month_letter, month_number in dictMonth.items():
    filterMonth = lambda x: x['dataHoraCotacao'][5:7] == month_number
    filteredData = list(filter(filterMonth, dictCotacoes['value']))
    lstMonth.append(filteredData)
dictFinal = {}
times = 0
cotVenda = 0
cotCompra = 0
# print(lstMonth)
for month in lstMonth:
    for cot in month:
        cotVenda += cot['cotacaoVenda']
        cotCompra += cot['cotacaoCompra']
    dictFinal[meses[times]] = {'media_compra':f'{cotCompra/len(month):.5f}','media_venda':f'{cotVenda/len(month):.5f}'}
    times += 1
    cotVenda = 0
    cotCompra = 0
print(dictFinal)
#

# ## Montando e criando arquivo do JSON
with open(strDiretorio + f'\\medias_cotacoes_{wanted_year}.json','w',encoding='utf-8') as arqEscrita:
    arqEscrita.write(str(dictFinal))
#

# ## Montando e criando arquivo do CSV
with open(strDiretorio + f'\\medias_cotacoes_{wanted_year}.csv','w',encoding='utf-8') as arqEscrita:
    strCabecalho = 'mes;media_compra;media_venda'
    arqEscrita.write(f'{strCabecalho}\n')

    for mes, dados in dictFinal.items():
        strLinha = f"{mes};{dados['media_compra']};{dados['media_venda']}\n"
        arqEscrita.write(strLinha)








