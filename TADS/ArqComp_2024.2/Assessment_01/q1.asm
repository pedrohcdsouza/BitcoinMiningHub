# Q1) Faça um programa para ler um número inteiro e imprimir o dobro desse número.

.text
	main:
		addi $2, $0, 5 # Adding the value '5' to register 2. (USER INPUT)
		syscall # Calling the SO
		
		mul $4, $2, 2 # Multiplying the USER INPUT and adding to register 4.
		
		addi $2, $0, 1 # Adding the value '1' to register 2. (PRINT)
		syscall
		
		
		
		
		
		
		
		
		