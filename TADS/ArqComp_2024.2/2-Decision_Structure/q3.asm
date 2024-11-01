# Q3) Escreva um programa para ler dois números inteiros e mostrar na tela o maior deles, bem como a diferença entre eles (a diferença é sempre um valor positivo)

.text
	main:	
		addi $2, $0, 5  # Reading a Intenger
		syscall
		add $8, $0, $2 # Saving on R8
		
		addi $2, $0, 5
		syscall
		add $9, $0, $2 # Saving on R9
		
		slt $10, $8, $9 # R8 less then R9, $10 <= 1
		
		beq $10, $0, bigger
		
		add $4, $0, $9 # Saving on R4 the variable to be printed
		sub $11, $9, $8
		
		j endline
		
	bigger:
		
		sub $11, $8, $9
		add $4, $0, $8
	
	endline:
		
		addi $2, $0, 1
		syscall # Print variable
		
		addi $4, $0, '|'
		addi $2, $0, 11
		syscall
	
		add $4, $0, $11 # Saving on R4 the difference between R8 and R9 or R9 and R8
		
		
		addi $2, $0, 1
		syscall
		
		addi $2, $0, 10
		syscall # End app
		 
		