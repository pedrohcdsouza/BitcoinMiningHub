# Q4) Faça um programa para ler duas notas de um aluno do IFRN em um curso semestral. E apresentar a média.

.text
	main:
		
		addi $2, $0, 5
		syscall
		
		# Input
		
		add $8, $0, $2 # Saving result in register '8'
		
		addi $2, $0, 5
		syscall
		
		# Input
		
	 	mul $9, $8, $2 # Multiplying the 2 grades
	 	
	 	div $4, $9, $2 # Dividing the result by 2
	 	
	 	addi $2, $0, 1
	 	syscall
	 	
	 	# Print
	 	
	 	