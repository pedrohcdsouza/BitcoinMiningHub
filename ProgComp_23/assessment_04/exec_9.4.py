'''
Faça um programa que leia dois valores: x e n (x e n deverão ser solicitados ao usuário), onde x é a quantidade de elementos que a lista deverá armazenar positivo e n 
serão os valores inteiros a serem inseridos na lista, o programa deve terminar a leitura dos números quando for informado o valor 0 (o valor 0 não deverá fazer parte da lista). 
A lista só deverá armazenar os x menores números informados, 
seguindo a lógica abaixo:
'''

#pedrohcdsouza arquive

n = int(input("Enter the number of elements in the list: ")) #Range of the list
listn = []

if n <= 0:
    print("Value not valid!")
else:
    while True:
        x = int(input("Enter a value: "))
        
        if x == 0:
            print("\nSystem over!\n")
            break

        elif len(listn) < n: #Checking if the list is shorter than the value entered

            listn.append(x)

        elif x < listn[n-1]: #Replace the value if it is smaller than the largest one
            sorted(listn)
            listn[n-1] = x
            
        print(listn)

    print(f"Your list was: {listn}")


    


