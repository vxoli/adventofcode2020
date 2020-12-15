# read data file
f = open('d12-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

#test data
# data = ["F10","N3","F7","R90","F11"]

# ensure input data in list
# data = [list(line) for line in data]

directions = {"E","S","W","N"}
rotations = {"L","R"}
forward = {"F","B"}

location = [0,0] #two value list [east/west,north/south]. east positive, west negative/ north positive, south negative
# set starting facing direction
compass = 90 # 90 degrees = E, 180 = S, 270 = W, 0/360 = N

for line in data:
    instruction = line[0]
    value = int(line[1:])
    print(line,instruction,value)
    if instruction in forward:
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
            location[1] += value
        if instruction == "S":
            location[1] -= value
        if instruction == "E":
            location[0] += value
        if instruction == "W":
            location[0] -= value
    if instruction in rotations:
        if instruction == "R":
            compass += value
        if instruction == "L":
            compass -= value
    print(location, compass, compass % 360)
print(f"Manhatten distance is: {abs(location[0]) + abs(location[1])}")
