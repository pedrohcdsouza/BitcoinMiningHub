#pedrohcdsouza arquive

text = str(input("Vigenère CIPHER\nWrite your text: "))
keyword = str(input("Now, write your keyword: "))
repeated_keyword = keyword * (len(text) // len(keyword))
print(repeated_keyword)