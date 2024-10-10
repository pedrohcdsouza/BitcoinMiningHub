#pedrohcdsouza arquive

n = int(input("Number of decimal places CALCULATOR\nWrite a value: "))
places = 0


if n < 0:
    print("Write a valid number!")
else:
    while True:
        if n == 0:
            break
        else:
            n//=10
            places+=1
    print(f"Your number has {places} places.")