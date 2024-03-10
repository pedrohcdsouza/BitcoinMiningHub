#pedrohcdsouza arquive

var = str(input("Write something: "))

pos = 0
j = 1
while pos >= 0:
    print(var[0:pos+1])
    pos += j
    if pos >= len(var):
        j = -1
        pos -= 2
    elif pos < 0:
        break
