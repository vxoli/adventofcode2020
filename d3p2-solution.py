f = open('d3-input.txt', 'r')
data = f.readlines()
length = len(data[0])
routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for route in range(len(routes)):
    col = 0
    trees = 0
    for row in range(len(data), routes[route][1]):
        print(route,row,col)
        if data[row][col] == "#":
                trees += 1 
        col = (col + routes[route][0]) % (length-1)

print(trees)
