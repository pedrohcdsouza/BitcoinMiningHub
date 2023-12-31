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

media_bandeira_produto = {}
postosprod = {}

for produto in setProd:
    for flag in setFlag:
        filtered_data = [data for data in lstArq_data if data[2] == produto and data[5] == flag]
        if flag not in postosprod:
            postosprod[flag] = {}
        postosprod[flag][produto] = len(filtered_data)
        total_valor = sum(float(item[4].replace(',', '.')) for item in filtered_data)
        media = total_valor / postosprod[flag][produto] if postosprod[flag][produto] > 0 else 0
        if flag not in media_bandeira_produto:
            media_bandeira_produto[flag] = {}
        
        media_bandeira_produto[flag][produto] = media

# Cálculo da média por produto e região
media_produto_regiao = {}
postosreg = {}
for produto in setProd:
    for regiao in setRegiao:
        filtered_data = [data for data in lstArq_data if data[2] == produto and data[0] == regiao]
        postosreg[regiao] = len(filtered_data)
        total_valor = sum(float(item[4].replace(',', '.')) for item in filtered_data)
        media = total_valor / postosreg[regiao] if postosreg[regiao] > 0 else 0

        if produto not in media_produto_regiao:
            media_produto_regiao[produto] = {}

        media_produto_regiao[produto][regiao] = media

# Gravando em arquivos
with open(STRDIR + '\\dados_estatisticos' + '\\media_bandeira.txt', 'w', encoding='utf-8') as media_bandeira_produto_file:
    media_bandeira_produto_file.write("bandeira – produto - valor_medio_venda – quantidade_postos\n")
    for flag, produtos in media_bandeira_produto.items():
        for produto, media in produtos.items():
            media_bandeira_produto_file.write(f"{flag} - {produto} - {media:.3f} - {postosprod[flag][produto]}\n")

with open(STRDIR + '\\dados_estatisticos' + '\\media_produto_regiao.txt', 'w', encoding='utf-8') as media_produto_regiao_file: #Não consegui achar uma lógica para colocar o ano, o mesmo vale para partes do arquivo que estão faltando.
    media_produto_regiao_file.write("produto – região – valor_medio – quantidade_postos\n")
    for produto, regioes in media_produto_regiao.items():
        for regiao, media in regioes.items():
            media_produto_regiao_file.write(f"{produto} – {regiao} – {media:.3f} - {postosreg[regiao]}\n")