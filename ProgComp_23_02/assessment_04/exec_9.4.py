'''
Faça um programa que leia dois valores: x e n (x e n deverão ser solicitados ao usuário), onde x é a quantidade de elementos que a lista deverá armazenar positivo e n 
serão os valores inteiros a serem inseridos na lista, o programa deve terminar a leitura dos números quando for informado o valor 0 (o valor 0 não deverá fazer parte da lista). 
A lista só deverá armazenar os x menores números informados, 
seguindo a lógica abaixo:
'''

#pedrohcdsouza

n = int(input("Enter the number of elements in the list: ")) # Range of the list
listn = []

if n <= 0:
    print("Value not valid!")
else:
    while True:
        listn.sort()
        x = int(input("Enter a value: "))
        
        if x == 0:
            print("\nSystem over!\n")
            break

        elif len(listn) < n:
            listn.append(x)

        elif n == len(listn): 
            if x < listn[-1]:
                listn[-1] = x
            
        print(listn)

    print(f"Your list is: {listn}")


    


