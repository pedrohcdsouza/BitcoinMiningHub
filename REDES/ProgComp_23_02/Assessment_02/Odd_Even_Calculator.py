#pedrohcdsouza arquive

n = float(input("Odd or Even CALCULATER\nWrite a Number: ")) #Par ou Impar calculadora

if n != int(n):
    print("Write a valid number!")
else:
    n = int(n)
    while n != 0:
        if n%2 == 0:
            print(f"{n} is a Odd Number!")
        else:
            print(f"{n} is a Even Number!")
        n = int(input("Write another number (0 to stop): "))
    print("End!")
