.text
	main:
		addi $2, $0, 5
		syscall
		add $8, $0, $2
		
		addi $9, $0, 10
		
		div $8, $9
		mfhi $10
		mflo $8
		mul $10, $10, 1
		add $18, $0, $10
		
		div $8, $9
		mfhi $11
		mflo $8
		mul $11, $11, 2
		add $18, $18, $11
		
		div $8, $9
		mfhi $12
		mflo $8
		mul $12, $12, 4
		add $18, $18, $12
		
		div $8, $9
		mfhi $13
		mflo $8
		mul $13, $13, 8
		add $18, $18, $13
		
		div $8, $9
		mfhi $14
		mflo $8
		mul $14, $14, 16
		add $18, $18, $14
		
		div $8, $9
		mfhi $15
		mflo $8
		mul $15, $15, 32
		add $18, $18, $15
		
		div $8, $9
		mfhi $16
		mflo $8
		mul $16, $16, 64
		add $18, $18, $16
		
		div $8, $9
		mfhi $17
		mflo $8
		mul $17, $17, 128
		add $4, $18, $17
		
		addi $2, $0, 1
		syscall
		addi $2, $0, 10
		syscall
		
		
		
		