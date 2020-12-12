# read data file
f = open('d9-input.txt', 'r')
data = f.readlines()
# test data
# data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 25 #25 for main problem, 5 for testing
for i in range(0,len(data)):
    data[i] = data[i].strip("\n")
# print(data[preamble:])

for idx, i in enumerate(data[preamble:]):
    solution = False
    # print("idx",idx,"i",i)
    for j in data[idx:idx+preamble]:
        for k in data[idx:idx+preamble]:
            if int(j) + int(k) == int(i) and (int(j) != int(k)):
                # print("i",i,"j",j,"k",k)
                solution = True
                break
        if solution == True:
            break
    if solution == False:
        print(i)
        break