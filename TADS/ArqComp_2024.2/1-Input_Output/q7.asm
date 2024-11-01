# Q7) Faça um programa que leia um número entre 0 e 9999 e imprima cada algarismo em uma linha diferente.

.text
	main:
		
		# Input
	
		addi $2, $0, 5
		syscall
		
		div $8, $2, 1000 # Catching the first Case
		
		mfhi $9
		div $9, $9, 100 # Catching the second Case 
		
		mfhi $10
		div $10, $10, 10 # Catching the third Case
		
		mfhi $11 # Catching the four Case
		
		addi $2, $0, 11
		add $4, $0, '\n'
		syscall
		
		addi $2, $0, 1
		add $4, $0, $8
		syscall
		
		addi $2, $0, 11
		add $4, $0, '\n'
		syscall
		
		addi $2, $0, 1
		add $4, $0, $9
		syscall
		
		addi $2, $0, 11
		add $4, $0, '\n'
		syscall
		
		addi $2, $0, 1
		add $4, $0, $10
		syscall
		
		addi $2, $0, 11
		add $4, $0, '\n'
		syscall
		
		addi $2, $0, 1
		add $4, $0, $11
		syscall
		