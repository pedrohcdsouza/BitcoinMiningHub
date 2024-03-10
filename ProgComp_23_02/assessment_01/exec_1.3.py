#pedrohcdsouza arquive

value = int(input("Please, write a number: "))

if value > 0 and value%2 == 0:
    print("It's a positive pair!")
elif value < 0 and value%2 == 0:
    print("It's a negative pair!")
elif value > 0 and value%2 == 1:
    print("It's a positive impar!")
elif value < 0 and value%2 == 1:
    print("It's a negative impar!")
else:
    print("It's a neutral number!")

