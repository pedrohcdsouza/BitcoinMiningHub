# Q3) Faça um programa para ler dois números inteiros e imprimir a multiplicação desses dois números

.text
	main:
	
		addi $2, $0, 5
		syscall
		
		# User input
		
		add $8, $0, $2 # Saving result in register '8'
		
		addi $2, $0, 5
		syscall
		
		# User input
		
		add $9, $0, $2 # Saving result in register '9'
		
		mul $4, $8, $9 # Multipyling the inputs
		
		addi $2, $0, 1
		syscall
		
		# Print
		