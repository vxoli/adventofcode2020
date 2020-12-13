# read data file
f = open('d9-input.txt', 'r')
data = f.readlines()
# test data
data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
# convert data to integers
for i in range(0,len(data)):
    data[i] = int(data[i].strip("\n"))
    