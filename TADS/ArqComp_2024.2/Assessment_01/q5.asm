# Faça um programa que leia um número inteiro entre 0 e 999 e imprima a soma dos algarismos desse número. Ex.: 358 gera uma saída de 16, pois 3+5+8 = 16

.text
	main:
	
		# Input
			
		addi $2, $0, 5
		syscall
		  
		div $8, $2, 100 # Catching the first Case
		
		mfhi $9 # Moving Hi (Rest from Division)
		
		div $9, $9, 10 # Catching the second Case
		
		mfhi $10 # Catching the third Case
		
		 # Adding the values
		
		add $11, $8, $9 
		add $11, $11, $10
		
		add $4, $0, $11 # Adding the value at register to print
		
		# Print
		
		addi $2, $0, 1
		syscall
		
		
		
		
		
		
		  