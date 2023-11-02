#pedrohcdsouza arquive

n = int(input("Triangulation Number CHECKER\nWrite a number: ")) #Número Triangular

if n <= 0:
    print("Write a valid number")
else:
    sum = 0
    checker = 1

    while sum < n:
        sum += checker
        checker += 1
    if sum == n:
        print(f"{n} is a Triangulation Number.")
    else:
        print(f"{n} isn't a Triangulation Number.")


