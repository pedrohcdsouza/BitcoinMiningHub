# Q3) Faça um programa para ler dois números inteiros e imprimir a multiplicação desses dois números

.text
	main:
		
		# User input
		
		addi $2, $0, 5
		syscall
		
		add $8, $0, $2 # Saving result in register '8'
		
		# User input
		
		addi $2, $0, 5
		syscall
		
		mul $4, $8, $2 # Multipyling the inputs
		
		# Print
		
		addi $2, $0, 1
		syscall
		
		# End service
		
		addi $2, $0, 10
		syscall