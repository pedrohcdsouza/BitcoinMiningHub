#pedrohcdsouza arquive

import requests, datetime, os, sys, json

# ## 
STRURL = 'https://api.cartolafc.globo.com/atletas/mercado'
STRDIR = os.path.abspath(__file__)
STRDIR = os.path.dirname(STRDIR)
C_YEAR = datetime.datetime.now().year
#

# ## Check the year and if the file is available.
while True:
    try:
        wanted_year = int(input(f"Choose an year (0 to stop): "))
        if wanted_year == 0:
            print("Exiting the program!")
            sys.exit()
        elif wanted_year == C_YEAR:
            dictCartola = requests.get(STRURL, verify=True).json()
            break
        else:
            ArcDir = STRDIR + f'\\cartola_fc_{wanted_year}.json'
            with open(ArcDir, 'r', encoding='utf-8') as dictOpen:
                dictCartola = dictOpen.read()
                dictCartola = json.loads(dictCartola)
            break
    except FileNotFoundError:
        print("\nERROR: The desired year has no file!")
        continue
    except ValueError:
        print("\nERROR: The value entered must be a base-10 integer!")
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
#
        
# ## Choosing the line-up
roster = {
    "343": {"Goalkeeper": 1, "Defender": 3, "Wingback": 0, "Midfielder": 4, "Forward": 3, "Tech": 1}, #OBS: Wingback == Lateral
    "352": {"Goalkeeper": 1, "Defender": 3, "Wingback": 0, "Midfielder": 5, "Forward": 2, "Tech": 1},
    "433": {"Goalkeeper": 1, "Defender": 2, "Wingback": 2, "Midfielder": 3, "Forward": 3, "Tech": 1},
    "442": {"Goalkeeper": 1, "Defender": 2, "Wingback": 2, "Midfielder": 4, "Forward": 2, "Tech": 1},
    "451": {"Goalkeeper": 1, "Defender": 2, "Wingback": 2, "Midfielder": 5, "Forward": 1, "Tech": 1},
    "532": {"Goalkeeper": 1, "Defender": 3, "Wingback": 2, "Midfielder": 3, "Forward": 2, "Tech": 1},
    "541": {"Goalkeeper": 1, "Defender": 3, "Wingback": 2, "Midfielder": 4, "Forward": 1, "Tech": 1}
}

while True:
    try:
        wanted_roster = str(input("Escolha uma escalação (0 para sair): ")).replace("-","").replace(".","").replace(" ","")
        if wanted_roster == 0:
            print("Exiting the program!")
            sys.exit()
        elif wanted_roster not in roster.keys():
            print("Chosen line-up not valid!")
        else:
            break
    except:
        print(f"\nERROR: {sys.exc_info()[0]}")
#   

# ## Filtering the required data
dictMelhores = sorted(dictCartola['atletas'], key=lambda x: x['media_num'] * x['jogos_num'], reverse=True) #Top ranked players

best_goalkeeper = [x for x in dictMelhores if x['posicao_id'] == 1]
best_defender = [x for x in dictMelhores if x['posicao_id'] == 2]
best_wingback = [x for x in dictMelhores if x['posicao_id'] == 3]
best_midfielder = [x for x in dictMelhores if x['posicao_id'] == 4]
best_forward = [x for x in dictMelhores if x['posicao_id'] == 5]
best_tech = [x for x in dictMelhores if x['posicao_id'] == 6]


if wanted_roster in roster: #
    numPlayer = roster[wanted_roster]

    pos_ids = {"Goalkeeper": 1, "Defender": 2, "Wingback": 3, "Midfielder": 4, "Forward": 5, "Tech": 6}

    selected_players = []
    for pos, qnt in numPlayer.items():
        pos_id = pos_ids[pos]
        playerPos = [x for x in dictMelhores if x['posicao_id'] == pos_id]
        sorted_players = sorted(playerPos, key=lambda x: x['media_num'] * x['jogos_num'], reverse=True)[:qnt]
        selected_players.extend(sorted_players)

    #Displaying the CARTOLA FC team
    print("CARTOLA FC team:")
    for player in selected_players:
        score = player['media_num'] * player['jogos_num']
        positions = ["Goleiro", "Zagueiro", "Lateral", "Meia", "Atacante", "Técnico"]
        print(f"Position: {positions[player['posicao_id'] - 1]}")
        print(f"Name: {player['nome']} ({player['apelido']})")
        print(f"Team: {dictCartola['clubes'][str(player['clube_id'])]['nome']}")
        print(f"Score: {score:.3f}\n")