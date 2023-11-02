#pedrohcdsouza arquive

phrase = str(input("Vowel quantity CALCULATOR\nWrite your phrase: ")).lower().replace("â","a").replace("á","a").replace("à","a").replace("ã","a").replace("ê","e").replace("é","e").replace("è","e").replace("î","i").replace("í","i").replace("ì","i").replace("ô","o").replace("ó","o").replace("ò","o").replace("û","u").replace("ú","u").replace("ù","u")
count = 0

for letter in phrase:
    if letter in "aeiou":
        count += 1
print(f"The number of vowels in the phrase is {count}")
