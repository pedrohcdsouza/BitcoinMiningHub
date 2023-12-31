import csv, os

STRDIR = os.path.abspath(__file__)
STRDIR = os.path.dirname(STRDIR)

if not os.path.exists(STRDIR + '\\dados_estatisticos'):
    os.mkdir(STRDIR + '\\dados_estatisticos')

archives_csv = []
for archives in os.listdir(STRDIR):
    if archives.startswith('ca-') and archives.endswith('.csv'):  # Verifica se o arquivo começa com 'ca-' e termina com '.csv'
        archives_csv.append(archives)

lstArq_data = []  # Inicializa a lista fora do loop para acumular dados de todos os arquivos
lstFlag = []
lstProd = []
lstRegion = []

for archive in archives_csv:
    ArcDir = os.path.join(STRDIR, archive)

    # Abrindo e lendo cada arquivo CSV
    with open(ArcDir, 'r', encoding='utf-8') as READarq:
        Reader = csv.reader(READarq, delimiter=';')
        Header = READarq.readline()[:-1]
        for line in Reader:
            lstFlag.append(line[15])
            lstProd.append(line[10])
            lstRegion.append(line[0])
            dados = [line[0], line[1], line[10], line[11], line[12], line[15]]
            lstArq_data.append(dados)


# Escrevendo os dados processados em um novo arquivo
with open(STRDIR + '\\dados_estatisticos\\serie_historica_anp.csv', 'w', encoding='utf-8') as WRITEarq:
    Header = ['Regiao – Sigla', 'Estado – Sigla', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Bandeira']
    lstArq_serie = lstArq_data
    lstArq_serie.insert(0, Header)
    for line in lstArq_serie:
        strLine = ';'.join([str(item) for item in line])
        WRITEarq.write(f'{strLine}\n')

# Codificando as listas lstFlag e lstProd
setFlag = set(lstFlag)  # Nome de cada produto
prodflag = 0
lstFlag = []
setProd = set(lstProd)  # Nome de cada bandeira
setRegiao = set(lstRegion)

media_bandeira = {}
for flag in setFlag:
    filtered_data = [data for data in lstArq_data if data[5] == flag]
    total_postos = len(filtered_data)
    total_valor = sum(float(item[4].replace(',', '.')) for item in filtered_data)
    media = total_valor / total_postos if total_postos > 0 else 0

    media_bandeira[flag] = media

# Cálculo da média por produto e região
media_produto_regiao = {}
for produto in setProd:
    for regiao in setRegiao:
        filtered_data = [data for data in lstArq_data if data[2] == produto and data[0] == regiao]
        total_postos = len(filtered_data)
        total_valor = sum(float(item[4].replace(',', '.')) for item in filtered_data)
        media = total_valor / total_postos if total_postos > 0 else 0

        if produto not in media_produto_regiao:
            media_produto_regiao[produto] = {}

        media_produto_regiao[produto][regiao] = media

# Gravando em arquivos
with open(os.path.join(STRDIR, 'dados_estatisticos', 'media_bandeira.txt'), 'w', encoding='utf-8') as media_bandeira_file:
    media_bandeira_file.write("bandeira – produto – ano – valor_medio_venda – quantidade_postos\n")
    for flag, media in media_bandeira.items():
        media_bandeira_file.write(f"{flag} – {media}\n")

with open(os.path.join(STRDIR, 'dados_estatisticos', 'media_produto_regiao.txt'), 'w', encoding='utf-8') as media_produto_regiao_file:
    media_produto_regiao_file.write("produto – região – ano – valor_medio – quantidade_postos\n")
    for produto, regioes in media_produto_regiao.items():
        for regiao, media in regioes.items():
            media_produto_regiao_file.write(f"{produto} – {regiao} – {media}\n")