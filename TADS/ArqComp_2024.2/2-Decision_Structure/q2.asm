# Q2) Faça um programa para ler um número inteiro. Se o número for positivo, imprima o dobro do número, se for negativo, imprima o quadrado do número.

.text
	main:	
		addi $2, $0, 5  # Reading a Intenger
		syscall
		add $8, $0, $2 # Saving on R8
		
		slt $9, $8, $0 # 0 less then R8, $9 <= 1
		
		beq $9, $0, positive
		
		mul $8, $8, $8 # Save on R8 the result of R8 * R8
		add $4, $0, $8
		
		j endline
		
	positive:
		
		sll $8, $8, 1 # Double of a number
		add $4, $0, $8
		
		  
	
	endline:
		
		addi $2, $0, 1
		syscall # Print variable
		
		addi $2, $0, 10
		syscall # End app
		 