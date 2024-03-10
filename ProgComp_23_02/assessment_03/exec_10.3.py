#pedrohcdsouza arquive

phrase = str(input("Palindrome VERIFICATOR\nWrite your phrase: ")).lower().replace(" ", "").replace("-","").replace("é","e").replace("á","a").replace("í","i").replace("ã","a").replace("?","")
phrase_reversed = phrase[::-1]

if phrase != phrase_reversed:
    print("Your phrase isn't palindrome!")
else:
    print("Your phrase is palindrome!")