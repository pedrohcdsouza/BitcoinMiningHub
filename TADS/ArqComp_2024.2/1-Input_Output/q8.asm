# Q8) Faça um programa que leia três números inteiros, representando a duração em horas, minutos e segundos de um experimento científico e informe essa duração em segundos.

.text
	main:
		
		addi $2, $0, 5
		syscall
		
		mul $8, $2, 360
		
		addi $2, $0, 5
		syscall
		
		mul $9, $2, 60
		
		addi $2, $0, 5
		syscall
		
		add $8, $8, $9
		add $8, $8, $2
		
		add $4, $0, $8
		addi $2, $0, 1
		syscall
		