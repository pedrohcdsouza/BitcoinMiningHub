.text
	main:
		# Read the Age
		addi $2, $0, 5
		syscall
		add $8, $0, $2
		
		# Read the Service Time
		addi $2, $0, 5
		syscall
		add $9, $0, $2
		
		# Variable with 65 years
		addi $10, $0, 65
		# Variable with 40 yers
		addi $11, $0, 40
		# Variable with 60 years
		addi $12, $0, 60
		# Variable with 35 years
		addi $13, $0, 36
		
		# If age > 65 years
		
		slt $14, $8, $10
		beq $14, $0, retire
		# else
		
		
		slt $15, $9, $11
		beq $15, $0, retire
		#else
		
		slt $16, $8, $12
		beq $16, $0, morethen
		#else
		addi $4, $0, 'N'
		j end
	
	morethen:
		slt $17, $9, $13
		beq $17, $0, retire
		#else
		addi $4, $0, 'N'
		j end
		  
		
	retire:
		addi $4, $0, 'S'
	end:
		addi $2, $0, 11
		syscall
	
		