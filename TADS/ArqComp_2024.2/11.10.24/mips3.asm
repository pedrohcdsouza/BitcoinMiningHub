.text
	main:
		addi $2, $0, 5
		syscall
		add $8, $0, $2
		
		add $4, $0, $13
		addi $2, $0, 1
		syscall