.text
	main:
		addi $2, $0, 5
		syscall
		add $8, $0, $2
		
		addi $2, $0, 5
		syscall
		add $9, $0, $2
		
		addi $2, $0, 5
		syscall
		add $10, $0, $2
		
		slt $11, $8, $9
		slt $12, $10, $9
		
		beq $11, $12, negativo
		#else
		slt $11, $9, $8
		slt $12, $9, $10
		
		beq, $11, $12, positivo
		#else
		addi $4, $0, 'N'
		addi $2, $0, 11
		syscall
		j end
		
	positivo:
		addi $4, $0, 'P'
		addi $2, $0, 11
		syscall
		addi $4, $0, '+'
		syscall
		j end
	
	negativo:
		addi $4, $0, 'P'
		addi $2, $0, 11
		syscall
		addi $4, $0, '-'
		syscall
		j end
	
	end:
		addi $2, $0, 10
		syscall
	