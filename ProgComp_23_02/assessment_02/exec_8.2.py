#pedrohcdsouza arquive

n = float(input("Half Life CALCULATOR:\nWrite a number: "))
x = n
seconds = 0
minutes = 0
hours = 0

if n <= 0:
    print("Write a valid number!")
else:
    while n >= 0.5:
        n /= 2
        seconds += 50
    print(f"Initial mass: {x:.2f}g")
    print(f"Final mass: {n:.2f}g")
    while seconds > 3600:
        seconds -= 3600
        hours += 1
    while seconds > 60:
        seconds -= 60
        minutes += 1
    print(f"Time: {hours}:{minutes}:{seconds}")


    
    
    
        
    