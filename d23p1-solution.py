# read input file

f = open("d23-input.txt","r")
data = f.readlines()
# split numbers into list and drop 0th entry containing original number read form file
for i in range(len(data[0])):
    data.append(int(data[0][i]))
data.pop(0)

# test data
data = list("389125467")
# convert string to integer
for i in range(len(data)):
    data[i] = int(data[i])

