# read data file
f = open('d12-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

#test data
# data = ["F10","N3","F7","R90","F11"]

# ensure input data in list
# data = [list(line) for line in data]

directions = {"E","S","W","N"}
rotations = {"L","R"}
current_posn = {"E":0, "S":0, "W":0, "N":0}
#dictionary of direction and current value
# set starting facing direction to east
# 90 degrees = E, 180 = S, 270 = W, 0/360 = N
compass = 90 

for line in data:
    instruction = line[0]
    value = int(line[1:])
    print(line,instruction,value)
    if instruction == "F":
        if compass % 360 == 0:
            instruction = "N"
        if compass % 360 == 90:
            instruction = "E"
        if compass % 360 == 180:
            instruction = "S"
        if compass % 360 == 270:
            instruction == "W"
    if instruction in directions:
        if instruction == "N":
            current_posn["N"] += value
        if instruction == "S":
            current_posn["S"] += value
        if instruction == "E":
            current_posn["E"] += value
        if instruction == "W":
            current_posn["W"] += value
    if instruction in rotations:
        if instruction == "R":
            compass += value
        if instruction == "L":
            compass -= value
    
print(current_posn["E"], current_posn["W"], current_posn["N"], current_posn["S"])
location = (current_posn["E"]-current_posn["W"]) + (current_posn["N"]- current_posn["S"]) 
print(f"Manhatten distance is: {location}")
