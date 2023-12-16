import requests, datetime, os, sys, json
# ##
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
current_year = datetime.datetime.now().year
#

# ## Verificando o ano e fazendo a leitura dos arquivos.
while True:
    try:
        wanted_year = int(input(f"Escolha um ano (0 para sair): "))
        if wanted_year == 0:
            print("Saindo do programa!")
            sys.exit()
        elif wanted_year == current_year:
            dictCartola = requests.get(strURL, verify=True).json()
            break
        else:
            strNomeArq = strDiretorio + f'\\cartola_fc_{wanted_year}.json'
            dictOpen = open(strNomeArq,'r',encoding='UTF-8')
            dictCartola = dictOpen.read()
            dictCartola = json.loads(dictCartola)
            dictOpen.close()
            break
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base10!")
        continue
    except FileNotFoundError:
        print("\nERROR: O ano desejado não possui arquivo!")
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
#

# ## Filtrando apenas os dados necessários
dictAtletas = dict()
for atleta in range(len(dictCartola['atletas'])):
    dictAtletas[atleta] = dictCartola['atletas'][atleta]
#



    
    
