#pedrohcdsouza arquive

from lista_palavras import *

frase = input("Escreva uma frase: ")
ascii = sum([ord(i) for i in frase])
i = 0

while ascii != sum([ord(i) for i in lstPalavras[i]]):
    if ascii == sum([ord(i) for i in lstPalavras[i]]):
        print("Achou!")
else:
    print("Não achou!")

    






