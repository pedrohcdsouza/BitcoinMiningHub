#pedrohcdsouza arquive

n = int(input("Sum of Values CACULATOR\nWrite a number: "))

if n < 0 or n == 0:
    print("Write a valid number!")

else:
    while True:
        n_2 = int(input("Write another number (0 to stop): "))
        if n_2 == 0:
            break
        else:
            n = n+n_2
    print(f"The sum of the values: {n}.")

    
