#pedrohcdsouza arquive

position_x = int(input("Cartesian ROBOT\nWrite the initial_position (X): "))
position_y = int(input("Write the initial_position (Y): "))
initial_x = position_x
initial_y = position_y
valid_moves = ""

print("[U north] [D south] [R east] [L west] \n[O northwest] [N northeast] [E southwest] [W southeast]")
moves = str(input("Now write the MOVES: \n")).upper()

for j in moves:
    if j == "U":
        position_y += 1
        valid_moves += "U"
    if j == "D":
        position_y -= 1
        valid_moves += "D"
    if j == "R":
        position_x += 1
        valid_moves += "R"
    if j == "L":
        position_x -= 1
        valid_moves += "L"
    if j == "O":
        position_y += 1
        position_x -= 1
        valid_moves += "O"
    if j == "N":
        position_y += 1
        position_x += 1
        valid_moves += "N"
    if j == "E":
        position_y -= 1
        position_x += 1
        valid_moves += "E"
    if j == "W":
        position_y -= 1
        position_x -= 1
        valid_moves += "W"

print(f"Your initial position was: ({initial_x},{initial_y})")
print(f"Your final position was: ({position_x},{position_y})")
print(f"You had {len(valid_moves)} valid moves!")
print(f"The valid moves were: {valid_moves}")

if initial_x > 0 and initial_y > 0:
    print(f"On the start you were in the first quadrant.")
elif initial_x < 0 and initial_y > 0:
    print(f"On the start you were in the second quadrant.")
elif initial_x < 0 and initial_y < 0:
    print(f"On the start you were in the third quadrant.")
elif initial_x > 0 and initial_y < 0:
    print(f"On the start you were in the fourth quadrant.")
else:
    print(f"On the start you were touching one of the axes.")

if position_x > 0 and position_y > 0:
    print(f"In the end you were in the first quadrant.")
elif position_x < 0 and position_y > 0:
    print(f"In the end you were in the second quadrant.")
elif position_x < 0 and position_y < 0:
    print(f"In the end you were in the third quadrant.")
elif position_x > 0 and position_y < 0:
    print(f"In the end you were in the fourth quadrant.")
else:
    print(f"In the end you were touching one of the axes.")









