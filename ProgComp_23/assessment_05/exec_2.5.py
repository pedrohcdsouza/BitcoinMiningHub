import requests, datetime, os
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

# ## Solicite ao usuário o ano desejado (o ano informado não pode ser superior ao ano atual, 
# para isso deve-se usar as funções/métodos da biblioteca DATETIME para obter/validar o ano atual;

current_year = datetime.datetime.now().year

#verificando se o ano é maior que o ano atual!
while True:
    wanted_year = int(input(f"Escolha um ano de 2021 à {current_year}\n"))
    if wanted_year <= current_year and wanted_year > 2021:
        break
#
if wanted_year == current_year:
    dictCartola = requests.get(strURL, verify=False).json()
else:
    
    
