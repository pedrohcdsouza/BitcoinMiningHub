#pedrohcdsouza arquive

cpf = str(input("CPF VERIFIER\nWrite your CPF: ")).lower().replace("-","").replace("_","").replace(".","") #CPF = Social Security Number
verify = 0
s = 10

for j in cpf[0:9]:
    verify += int(j) * s
    s -= 1

if verify*10%11 != int(cpf[9]):
    print("INVALID CPF!")
else:
    verify = 0
    s = 11

    for j in cpf[0:10]:
        verify += int(j) * s
        s -= 1

    if verify*10%11 != int(cpf[10]):
        print("INVALID CPF!")
    else:
        print(f'The CPF: "{cpf}" is valid!')

  



