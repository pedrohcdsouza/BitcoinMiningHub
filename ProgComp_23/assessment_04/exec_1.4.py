from cotacao_dolar import *

#pedrohcdsouza arquive


cot_1 = list(map(lambda c: c[1], filter(lambda c: c[0].startswith('2022-01'), cotacoes_dolar)))
print(cot_1)


        
    