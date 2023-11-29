from cotacao_dolar import *

'''
A partir do arquivo cotacao_dolar.py , fazer um programa que:

Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o mês (Janeiro, Fevereiro,..., Dezembro), 
a segunda posição deverá ser a maior cotação de venda do respectivo mês e a terceira posição deverá ser a data relativa a essa maior cotação.

Montar uma segunda lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o mês (Janeiro, Fevereiro,..., Dezembro), 
e a segunda posição deverá ser a média das cotações de venda do respectivo mês.
'''


#pedrohcdsouza arquive

monthly_max = [] #month,max,data
monthly_avarage = [] #month,avarage
 
jan_data = [x[0] for x in list(filter(lambda x: "2022-01" in x[0], cotacoes_dolar))] #all january datas
jan_values = [x[1] for x in list(filter(lambda x: "2022-01" in x[0], cotacoes_dolar))] #all january values
jan_index = jan_values.index(max(jan_values)) #index of data max

feb_data = [x[0] for x in list(filter(lambda x: "2022-02" in x[0], cotacoes_dolar))] 
feb_values = [x[1] for x in list(filter(lambda x: "2022-02" in x[0], cotacoes_dolar))] 
feb_index = feb_values.index(max(feb_values))

mar_data = [x[0] for x in list(filter(lambda x: "2022-03" in x[0], cotacoes_dolar))] 
mar_values = [x[1] for x in list(filter(lambda x: "2022-03" in x[0], cotacoes_dolar))] 
mar_index = mar_values.index(max(mar_values))

apr_data = [x[0] for x in list(filter(lambda x: "2022-04" in x[0], cotacoes_dolar))] 
apr_values = [x[1] for x in list(filter(lambda x: "2022-04" in x[0], cotacoes_dolar))] 
apr_index = apr_values.index(max(apr_values))

may_data = [x[0] for x in list(filter(lambda x: "2022-05" in x[0], cotacoes_dolar))] 
may_values = [x[1] for x in list(filter(lambda x: "2022-05" in x[0], cotacoes_dolar))] 
may_index = may_values.index(max(may_values))

jun_data = [x[0] for x in list(filter(lambda x: "2022-06" in x[0], cotacoes_dolar))] 
jun_values = [x[1] for x in list(filter(lambda x: "2022-06" in x[0], cotacoes_dolar))] 
jun_index = jun_values.index(max(jun_values))

jul_data = [x[0] for x in list(filter(lambda x: "2022-07" in x[0], cotacoes_dolar))] 
jul_values = [x[1] for x in list(filter(lambda x: "2022-07" in x[0], cotacoes_dolar))] 
jul_index = jul_values.index(max(jul_values))

aug_data = [x[0] for x in list(filter(lambda x: "2022-08" in x[0], cotacoes_dolar))] 
aug_values = [x[1] for x in list(filter(lambda x: "2022-08" in x[0], cotacoes_dolar))] 
aug_index = aug_values.index(max(aug_values))

sep_data = [x[0] for x in list(filter(lambda x: "2022-09" in x[0], cotacoes_dolar))] 
sep_values = [x[1] for x in list(filter(lambda x: "2022-09" in x[0], cotacoes_dolar))] 
sep_index = sep_values.index(max(sep_values))

oct_data = [x[0] for x in list(filter(lambda x: "2022-10" in x[0], cotacoes_dolar))] 
oct_values = [x[1] for x in list(filter(lambda x: "2022-10" in x[0], cotacoes_dolar))] 
oct_index = oct_values.index(max(oct_values))

nov_data = [x[0] for x in list(filter(lambda x: "2022-11" in x[0], cotacoes_dolar))] 
nov_values = [x[1] for x in list(filter(lambda x: "2022-11" in x[0], cotacoes_dolar))] 
nov_index = nov_values.index(max(nov_values))

dez_data = [x[0] for x in list(filter(lambda x: "2022-12" in x[0], cotacoes_dolar))] 
dez_values = [x[1] for x in list(filter(lambda x: "2022-12" in x[0], cotacoes_dolar))] 
dez_index = dez_values.index(max(dez_values))

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
values = [max(jan_values) , max(feb_values) , max(mar_values) , max(apr_values) , max(may_values) , max(jun_values) , max(jul_values) , max(aug_values) , max(sep_values) , max(oct_values) , max(nov_values) , max(dez_values)]
data = [jan_data[jan_index] , feb_data[feb_index] , mar_data[mar_index] , apr_data[apr_index] , may_data[may_index] , jun_data[jun_index] , jul_data[jul_index] , aug_data[aug_index] , sep_data[sep_index] , oct_data[oct_index] , nov_data[nov_index] , dez_data[dez_index]]
avarage = [(sum(jan_values)/len(jan_values)) , (sum(feb_values)/len(feb_values)) , (sum(mar_values)/len(mar_values)) , (sum(apr_values)/len(apr_values)) , (sum(may_values)/len(may_values)) , (sum(jun_values)/len(jun_values)) , (sum(jul_values)/len(jul_values)) , (sum(aug_values)/len(aug_values)) , (sum(sep_values)/len(sep_values)) , (sum(oct_values)/len(oct_values)) , (sum(nov_values)/len(nov_values)) , (sum(dez_values)/len(dez_values))]

for i in range(0,12):
    monthly_max.extend([[months[i],values[i],data[i]]])
    monthly_avarage.extend([[months[i],round(avarage[i],4)]])

print(f"\nHIGHEST DOLLAR VALUE PER MONTH\n")
for i in monthly_max:
    print(i)
print(f"\nAVARAGE DOLLAR VALUE PER MONTH\n")
for i in monthly_avarage:
    print(i)