#pedrohcdsouza arquive

n = int(input("Narcissistic Number CHECKER\nWrite a number: "))
x = n
z = n

if n <= 0:
    print("Write a valid number!")
else:
    places = 0
    sum = 0
    while True:
        if n == 0:
            break
        else:
            n//=10
            places+=1
    while x > 0:
        digit = x % 10
        sum += digit**places
        x //= 10
    if sum == z:
        print("Narcissistic Number!")
    else:
        print("Isn't Narcissistic Number!")
