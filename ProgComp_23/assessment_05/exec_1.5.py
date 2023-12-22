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
        
# ## Escolhendo a escalação
roster = ["343","352","433","442","451","532","541"]
while True:
    wanted_roster = str(input("Escolha uma escalação (0 para sair): ")).replace("-","").replace(".","").replace(" ","")
    if wanted_roster == 0:
        print("Saindo do programa!")
        sys.exit()
    elif wanted_roster not in roster:
        print("Escalação desejada não é válida!")
    else:
        break
#

# ## Filtrando apenas os dados necessários
dictMelhores = sorted(dictCartola['atletas'], key=lambda x: x['media_num'] * x['jogos_num'], reverse=True)
melhores_tecnicos = [x for x in dictMelhores if x['posicao_id'] == 6]
melhores_atacantes = [x for x in dictMelhores if x['posicao_id'] == 5]
melhores_meias = [x for x in dictMelhores if x['posicao_id'] == 4]
melhores_zagueiros = [x for x in dictMelhores if x['posicao_id'] == 3]
melhores_laterais = [x for x in dictMelhores if x['posicao_id'] == 2]
melhores_goleiros = [x for x in dictMelhores if x['posicao_id'] == 1]
#

if wanted_roster == '343':
    print(f"\nESCALAÇÃO CARTOLA FC no {wanted_roster}")
    print(f"Goleiro: {melhores_goleiros[0]['nome']}, conhecido como: {melhores_goleiros[0]['apelido_abreviado']}\nJoga no: {dictCartola['clubes'][str(melhores_goleiros[0]['clube_id'])]['nome']}\npontuou: {float(melhores_goleiros[0]['media_num'] * melhores_goleiros[0]['jogos_num']):.2f}")
    print(f"Zagueiro: {melhores_zagueiros[0]['nome']}, conhecido como: {melhores_zagueiros[0]['apelido_abreviado']}\nJoga no: {dictCartola['clubes'][str(melhores_zagueiros[0]['clube_id'])]['nome']}\npontuou: {float(melhores_zagueiros[0]['media_num'] * melhores_zagueiros[0]['jogos_num']):.2f}")
    print(f"Zagueiro: {melhores_zagueiros[1]['nome']}, conhecido como: {melhores_zagueiros[1]['apelido_abreviado']}\nJoga no: {dictCartola['clubes'][str(melhores_zagueiros[1]['clube_id'])]['nome']}\npontuou: {float(melhores_zagueiros[1]['media_num'] * melhores_zagueiros[1]['jogos_num']):.2f}")
    print(f"Zagueiro: {melhores_zagueiros[2]['nome']}, conhecido como: {melhores_zagueiros[2]['apelido_abreviado']}\nJoga no: {dictCartola['clubes'][str(melhores_zagueiros[2]['clube_id'])]['nome']}\npontuou: {float(melhores_zagueiros[2]['media_num'] * melhores_zagueiros[2]['jogos_num']):.2f}")


    
    
