import requests, datetime, os
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

current_year = datetime.datetime.now().year

# ## Verificando se o ano é maior/menor que o necessário.
while True:
    try:
        wanted_year = int(input(f"Escolha um ano de 2021 à {current_year}\n"))
        if wanted_year <= current_year and wanted_year >= 2021:
            break
    except :
        print("")
#
# ## Fazendo a leitura dos arquivos
if wanted_year == current_year:
    dictCartola = requests.get(strURL, verify=False).json()
else:
    strNomeArq = strDiretorio + f'\\cartola_fc_{wanted_year}.json'

    dictOpen = open(strNomeArq,'r',encoding='UTF-8')
    dictCartola = dictOpen.read()
    dictOpen.close()
#
esquemastaticos = ('343','352','433','442','451','532','541')






    
    
