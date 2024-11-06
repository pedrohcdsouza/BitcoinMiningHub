.text
	main:
		#Reading I
		addi $2, $0, 5
		syscall
		add $8, $0, $2
		
		#Reading J
		addi $2, $0, 5
		syscall
		add $9, $0, $2
		
		#Reading M
		addi $2, $0, 5
		syscall
		add $10, $0, $2
		
		# IF I % M = J % M
		
		div $8, $10
		mfhi $8
		div $9, $10
		mfhi $9
		
		beq $8, $9, equals
		# Else
		addi $4, $0, 'N'
		j end
	
	equals:
		addi $4, $0, 'S'
		
	end:
		addi $2, $0, 11
		syscall
		
		addi $2, $0, 10
		syscall
		