# Q4) Faça um programa que leia dois números e escreva a relação de grandeza entre eles. Ex. 345 e 23 gera a saída 345>23. Ex.: 24 e 38 gera a saída 24<38. Ex.: 12 e 12 gera a saída 12=12

.text
	main:	
		addi $2, $0, 5  # Reading a Intenger
		syscall
		add $8, $0, $2 # Saving on R8
		
		addi $2, $0, 5
		syscall
		add $9, $0, $2 # Saving on R9
		
		beq $8, $9, equals # If equals
		
		slt $10, $8, $9 # If R8 less then R9, R10 = 1
		
		beq $10, $0, bigger
		# else
		
		addi $2, $0, 1
		add $4, $0, $9
		syscall
		
		addi $2, $0, 11
		addi $4, $0, '>'
		syscall
		
		addi $2, $0, 1
		add $4, $0, $8
		syscall
		
		j endline
		
	bigger:
	
		addi $2, $0, 1
		add $4, $0, $8
		syscall
		
		addi $2, $0, 11
		addi $4, $0, '>'
		syscall
		
		addi $2, $0, 1
		add $4, $0, $9
		syscall
		
		j endline
					
	equals:
		addi $2, $0, 1
		add $4, $0, $8
		syscall
		
		addi $2, $0, 11
		addi $4, $0, '='
		syscall
		
		addi $2, $0, 1
		add $4, $0, $9
		syscall	
	
	endline:
		