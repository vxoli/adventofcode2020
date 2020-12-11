# read data file
f = open('d9-input.txt', 'r')
data = f.readlines()
# test data
data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 5#25 for main problem, 5 for testing

for i in range(5,len(data)):
    solution = False
    for j in range(i-5,i):
        for k in range(i-5,i):
            if j == k:
                continue
            if data[j] + data[k] == data[i]:
                print(data[j], data[k], data[i])
                break
            else:
                print(data[i])
    if solution == False:
        print(data[i])