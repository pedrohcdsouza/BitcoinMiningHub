# Q4) Faça um programa para ler duas notas de um aluno do IFRN em um curso semestral. E apresentar a média.

.text
	main:
		
		# Input
		
		addi $2, $0, 5
		syscall
		
		add $8, $0, $2 # Saving result in register '8'
		
		# Input
		
		addi $2, $0, 5
		syscall
		
	 	add $9, $8, $2 # Adding the 2 grades
	 	
	 	addi $10, $0, 2
	 	div $9, $10 # Dividing the result
	 	
	 	addi $4, $0, $9
	 	
	 	# Print
	 	
	 	addi $2, $0, 1
	 	syscall
	 	
	 	# End service
	 	
	 	addi $2, $0, 10
	 	syscall