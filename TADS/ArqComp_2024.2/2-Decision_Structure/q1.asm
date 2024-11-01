# Q1) Faça um programa para ler dois números e informe qual deles é o maior.

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
		
		j endline
		
	bigger:
		
		add $4, $0, $8
	
	endline:
		
		addi $2, $0, 1
		syscall # Print variable
		
		addi $2, $0, 10
		syscall # End app
		 
		
		
		