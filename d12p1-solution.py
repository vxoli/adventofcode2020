# read data file
f = open('d12-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

#test data
data = ["F10","N3","F7","R90","F11"]

# ensure input data in list
data = [list(line) for line in data]
