# Q10) Fa�a um programa que leia um caractere min�sculo e imprima o seu equivalente mai�sculo.

.text
	main:
		
		# Input
		
		addi $2, $0, 12
		syscall
		
		addi $4, $2, -32 # ASCII Table (-32 = ASCII Code)
		
		# Print Char
		
		addi $2, $0, 11
		syscall
		
		# End service
		
		addi $2, $0, 10
		syscall