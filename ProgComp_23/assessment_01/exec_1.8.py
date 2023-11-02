#pedrohcdsouza arquive

x = float(input("Escreva o X: "))
y = float(input("Escreva o Y: "))

if x > 0 and y > 0:
    print("1 Quadrante")
elif x < 0 and y > 0:
    print("2 Quadrante")
elif x > 0 and y < 0:
    print("3 Quadrante")
elif x < 0 and y < 0:
    print("4 Quadrante")
elif x == 0 and y != 0:
    print("Está no eixo X")
elif y == 0 and x != 0:
    print("Está no eixo Y")
else:
    print("Está na origem")