# read data file
f = open('d13-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
print(data)