# read data file
f = open('d9-input.txt', 'r')
data = f.readlines()
# test data
data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 5 #25 for main problem, 5 for testing
# convert input into integers
for i in range(0,len(data)):
    data[i] = int(data[i].strip("\n"))
