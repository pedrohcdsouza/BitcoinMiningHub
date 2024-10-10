#pedrohcdsouza arquive

value = 0

while True:
    n = float(input("Write a value: \nEX: 10.25"))
    if n == 0:
        break
    elif n < 0.01:
        print("Write a valid number!")
        quit()
    else:
        value += n

value100 = int(value * 100)  # multiplying for 100 to remove cents.

withdrawl = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

print(f"Total value: {value:.2f}")

for i in withdrawl: # i = note
    if value100 >= i:
        n_of_notes = value100 // i
        value100 -= n_of_notes * i
        print(f"{n_of_notes} amount of {i / 100:.2f}")




