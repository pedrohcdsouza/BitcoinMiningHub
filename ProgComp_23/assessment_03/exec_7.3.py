#pedrohcdsouza arquive


dna = str(input("DNA to RNA CALCULATOR\nWrite the Series: ")).upper()
rna = ""

for letter in dna:
    if letter == "A":
        rna += "U"
    elif letter == "G":
        rna += "G"
    elif letter == "T":
        rna += "C"
    elif letter == "C":
        rna += "A"
    else:
        print("Invalid Series!")
        break
print(f"Your DNA Series was: {dna}\nYour RNA should be: {rna}")
