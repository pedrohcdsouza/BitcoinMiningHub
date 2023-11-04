#pedrohcdsouza arquive

keyword = "surprise"
wrong = 0
right = 0

print("Hangman")
while True:
    attempt = str(input("Write a letter: ")).lower()
    found = 0 
    for pos in range(len(keyword)): 
        if attempt == keyword[pos]:
            right += 1
            print(f"You've got. The letter {attempt} was in {pos + 1}.")
            found = 1
    if found == 0:
        print("You wrong.")
        wrong += 1
        if wrong == 6:
            print("You've got 6 wrong letter. Game is over.")
            break
    elif right == len(keyword):
        print("You've won the game!")
        break


    
        

        




