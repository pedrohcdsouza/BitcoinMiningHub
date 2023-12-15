import requests, datetime, os, sys
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

current_year = datetime.datetime.now().year

# ## Verificando o ano.
while True:
    try:
        wanted_year = int(input(f"Escolha um ano: "))
        break
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base10!")
        continue
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
        sys.exit()
#
# ## Fazendo a leitura dos arquivos.
try:
    if wanted_year == current_year:
        dictCartola = requests.get(strURL, verify=True).json()
    else:
        strNomeArq = strDiretorio + f'\\cartola_fc_{wanted_year}.json'

        dictOpen = open(strNomeArq,'r',encoding='UTF-8')
        dictCartola = dictOpen.read()
        dictOpen.close()
except FileNotFoundError:
    print("\nERROR: O ano desejado não possui arquivo!")
except:
    print(f"\nERROR: {sys.exc_info()[0]}")
    sys.exit()
#
print(dictCartola)
# esquemastaticos = ('343','352','433','442','451','532','541')






    
    
