with open("d12-input.txt", "r") as fp:
    lines = [(line.rstrip()[0], int(line.rstrip()[1:]))  for line in fp.readlines()]
    dirs = ["E", "S", "W", "N", "L", "R", "F"]
curr_dir = "E"

curr_state = {"E":0, "W":0, "N":0, "S":0}

for line in lines:
    if line[0] == "F":
        curr_state[curr_dir] += line[1]
    
    if line[0] == "R":
        av = ["E", "S", "W", "N"]
        angle = line[1]
        v = int(angle/90)
        ndir = (av.index(curr_dir)+v) % len(av)
        ndir = av[ndir]
        curr_dir = ndir
        
    if line[0] == "L":
        av = ["E", "N", "W", "S"]
        angle = line[1]
        v = int(angle/90)
        ndir = (av.index(curr_dir)+v) % len(av)
        ndir = av[ndir]
        curr_dir = ndir
        
    
    if line[0] == "N":
        curr_state["N"] += line[1]
    if line[0] == "S":
        curr_state["S"] += line[1]
    if line[0] == "W":
        curr_state["W"] += line[1]
    if line[0] == "E":
        curr_state["E"] += line[1]
print(curr_state["E"],curr_state["W"],curr_state["S"],curr_state["N"])      
d = curr_state["E"]-curr_state["W"], curr_state["S"]-curr_state["N"]
print(f"Manhattan Distance of current positions from starting i.e. {curr_state} = {d[0]+d[1]}")
