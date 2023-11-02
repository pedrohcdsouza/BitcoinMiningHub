#pedrohcdsouza arquive

number_1 = int(input("Write the first cateto: "))
number_2 = int(input("Now the second one: "))
number_3 = int(input("And the hypotenuse: "))

if number_1 > 0 and number_2 > 0 and number_3 > 0:
    if (number_1**2)+(number_2**2) == (number_3)**2:
            print("You've got a Pythagorean trio")  
    else:
            print("You don't have a Pythagorean trio")
else:
    print("Type valid numbers")