value = int(input('Valor: '))

firstCase = value // 100
bruteValue = value % 100
secondCase = bruteValue // 10
thirdCase = bruteValue % 10

print(f'Divisão: \n{firstCase}\n{secondCase}\n{thirdCase}')