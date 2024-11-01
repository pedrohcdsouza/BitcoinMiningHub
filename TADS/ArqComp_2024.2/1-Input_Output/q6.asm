# Q6) Faça um programa que leia um número inteiro entre 0 e 999 e imprima esse número com 3 algarismos. Ex.: 23 gera uma saída 023. 8 gera uma saída 008.

.text
	main:
	
		# Input
			
		addi $2, $0, 5
		syscall
		  
		div $8, $2, 100 # Catching the first Case
		
		mfhi $9 # Moving Hi (Rest from Division)
		
		div $9, $9, 10 # Catching the second Case
		
		mfhi $10 # Catching the third Case
		
		add $4, $0, $8
		addi $2, $0, 1
		syscall
		
		add $4, $0, $9
		addi $2, $0, 1
		syscall
		
		add $4, $0, $10
		addi $2, $0, 1
		syscall
		