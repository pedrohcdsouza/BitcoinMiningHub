#pedrohcdsouza arquive

phrase = str(input("Letter in sentence CHECKER\nWrite your phrase: "))
letter = str(input("Now write the letter: "))
count = 0
a = 0
position = ""

for j in phrase.lower():
    a += 1
    if j == letter.lower():
        count += 1
        position += f"{a};"
if letter in phrase.lower():
    print(f'The letter {letter.upper()} was repeated {count} times in the phrase "{phrase}"\nin the positions: {position}')
else:
    print(f"The letter {letter.upper()} isn't on the Phrase.")

#OBS: A questão explícitava que a posição 1 deveria ser representado por 1 e não 0.