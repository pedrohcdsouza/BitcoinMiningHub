#pedrohcdsouza arquive

salary = float(input(f"Please, write your salary: "))
provision = float(input(f"Please, write the monthly provision of a loan: "))

if salary < 0 and provision < 0:
    print ("Enter a valid value!")
elif (provision/salary) < 0.2:
    print ("Loan granted!")
else:
    print ("Loan not granted.")
