import requests, datetime
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
dictCartola = requests.get(strURL, verify=False).json()

# ## Solicite ao usuário o ano desejado (o ano informado não pode ser superior ao ano atual, 
# para isso deve-se usar as funções/métodos da biblioteca DATETIME para obter/validar o ano atual;

current_year = datetime.datetime.now().year

#verificando se o ano é maior que o ano atual!
wanted_year = int(input("Write a year: "))
while wanted_year > current_year or wanted_year < 2021:
    wanted_year = int(input(f"O ano desejado não pode sair maior que {current_year} e menor que 2021.\n"))
#
if wanted_year == current_year:
    print("algo tem que acontecer")
else:
    print("algo tem que acontecer e fodase")