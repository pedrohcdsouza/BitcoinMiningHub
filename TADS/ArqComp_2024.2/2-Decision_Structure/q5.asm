# Q5) Fa�a um programa que receba tr�s notas (entre 0 e 100) e calcule a m�dia ponderada dessas notas com pesos 1, 2 e 3. Informe a m�dia e se o aluno foi aprovado, escreva ap�s a m�dia o a letra A. Caso o aluno seja reprovado, informe, ap�s a m�dia, a letra R. A m�dia para aprova��o � 60.

.text
	main:	
		addi $2, $0, 5  # Reading a Intenger
		syscall
		add $8, $0, $2 # Saving on R8
		
		addi $2, $0, 5
		syscall
		add $9, $0, $2 # Saving on R9
		
		addi $2, $0, 5
		syscall
		add $10, $0, $2 # Saving on R10
		
		mul $11, $9, 2
		add $11, $8, $9
		
		mul $15, $10, 3
		add $11, $11, $15
		
		
		addi $16, $0, 6
		div $11, $16
		
		addi $12, $0, 60 # Adding the media value
		
		slt $13, $11, $12 # If media < 60, $13 <= 1
		
		beq $13, $0, aprovate
		
		#reprovate:
		
		add $4, $0, $11
		addi $2, $0, 1
		syscall
		
		addi $4, $0, 'R'
		add $2, $0, 11
		syscall
		
		j endline
		
	aprovate:
		
		add $4, $0, $11
		addi $2, $0, 1
		syscall
		
		addi $4, $0, 'A'
		addi $2, $0, 11
		syscall
	
	endline: