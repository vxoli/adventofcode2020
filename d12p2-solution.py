# read data file
f = open('d12-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

#test data
data = ["F10","N3","F7","R90","F11"]

# ensure input data in list
# data = [list(line) for line in data]

directions = {"E","S","W","N"}
rotations = {"L","R"}
shipPosn = {"E":0, "S":0, "W":0, "N":0}
waypoint = {"E":10, "S":0, "W":0, "N":1}
#dictionary of direction and current value
# set starting facing direction to east
# 90 degrees = E, 180 = S, 270 = W, 0/360 = N
compass = 90 

for line in data:
    instruction = line[0]
    value = int(line[1:])
    if instruction == "F":
        if compass == 0:
            shipPosn["N"] += waypoint["N"] * value
        if compass == 90:
            shipPosn["E"] += waypoint["E"] * value
        if compass == 180:
            shipPosn["S"] += waypoint["S"] * value
        if compass == 270:
            shipPosn["W"] += waypoint["W"] * value
    if instruction in directions:
        waypoint[instruction] += value
    if instruction in rotations:
        if instruction == "R":
            compass += value
            compass = compass % 360
        if instruction == "L":
            compass -= value
            compass = compass % 360
    
distance = (shipPosn["E"]-shipPosn["W"]) + (shipPosn["S"]- shipPosn["N"]) 
print(f"Manhatten distance is: {distance}")
