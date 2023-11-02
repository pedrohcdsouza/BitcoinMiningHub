#pedrohcdsouza arquive

cathetus_1 = float(input("Write the first cathetus: "))
cathetus_2 = float(input("Write the second cathetus: "))

if cathetus_1 > 0 and cathetus_2 > 0:
    print(f"Your hypotenuse has: {((cathetus_1**2)+(cathetus_2)**2)**(1/2)}")
else:
    print("Write a valid number!")