#pedrohcdsouza arquive

salary = float(input(f"Please, write your salary: ")) #salário = float(input(f"Por favor informe seu salário: ))
provision = float(input(f"Please, write the monthly provision of a loan: ")) #prestação = float(input(f"Por favor, informe a prestação mensal do empréstimo: ))

if salary < 0 and provision < 0:
    print ("Enter a valid value!") #print ("Escreva um valor válido!")
elif (provision/salary) < 0.2:
    print ("Loan granted!") #print ("Empréstimo concecido!")
else:
    print ("Loan not granted.") #print ("Empréstimo não concecido!")
