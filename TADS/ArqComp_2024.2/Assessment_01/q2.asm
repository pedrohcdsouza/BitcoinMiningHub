# Q2) Faça um programa para ler um número inteiro e imprimir o quadrado desse número.

.text
	main:
		addi $2, $0, 5
		syscall
		
		# Catching the user input
		
		mul $4, $2, $2 # Adding the ² of user input on register '4'
		
		addi $2, $0, 1
		syscall
		
		# Priting the result
		
		addi $2, $0, 10 # Ending the service
		syscall