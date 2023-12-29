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

# ## Filtrando e tratando apenas os dados necessários
dictMelhores = sorted(dictCartola['atletas'], key=lambda x: x['media_num'] * x['jogos_num'], reverse=True)
melhores_tecnicos = [x for x in dictMelhores if x['posicao_id'] == 6]
melhores_atacantes = [x for x in dictMelhores if x['posicao_id'] == 5]
melhores_meias = [x for x in dictMelhores if x['posicao_id'] == 4]
melhores_zagueiros = [x for x in dictMelhores if x['posicao_id'] == 3]
melhores_laterais = [x for x in dictMelhores if x['posicao_id'] == 2]
melhores_goleiros = [x for x in dictMelhores if x['posicao_id'] == 1]
t = 0 #jogador1
goleiro = [melhores_goleiros[t]['nome'],melhores_goleiros[t]['apelido_abreviado'],dictCartola['clubes'][str(melhores_goleiros[t]['clube_id'])]['nome'],float(melhores_goleiros[0]['media_num'] * melhores_goleiros[0]['jogos_num'])]
#

formacoes = {
    "343": {"Goleiro": 1, "Zagueiro": 3, "Lateral": 0, "Meia": 4, "Atacante": 3, "Técnico": 1},
    "352": {"Goleiro": 1, "Zagueiro": 3, "Lateral": 0, "Meia": 5, "Atacante": 2, "Técnico": 1},
    # Adicione as demais formações com suas respectivas quantidades de jogadores por posição
}

if wanted_roster in formacoes:
    num_jogadores_por_posicao = formacoes[wanted_roster]

    # Mapeamento dos nomes das posições para seus respectivos IDs
    posicoes_ids = {"Goleiro": 1, "Zagueiro": 3, "Lateral": 2, "Meia": 4, "Atacante": 5, "Técnico": 6}

    # Selecionando os jogadores de cada posição de acordo com a formação escolhida
    selected_players = []
    for posicao, quantidade in num_jogadores_por_posicao.items():
        posicao_id = posicoes_ids[posicao]
        jogadores_da_posicao = [x for x in dictMelhores if x['posicao_id'] == posicao_id]
        sorted_players = sorted(jogadores_da_posicao, key=lambda x: x['media_num'] * x['jogos_num'], reverse=True)[:quantidade]
        selected_players.extend(sorted_players)

    # Exibindo a seleção do Cartola FC
    print("Seleção do Cartola FC:")
    for player in selected_players:
        posicoes = ["Goleiro", "Zagueiro", "Lateral", "Meia", "Atacante", "Técnico"]
        print(f"Posição: {posicoes[player['posicao_id'] - 1]}")
        print(f"Nome: {player['nome']} ({player['apelido']})")
        print(f"Time: {dictCartola['clubes'][str(player['clube_id'])]['nome']}")
        print(f"Pontuação: {player['media_num'] * player['jogos_num']}")
