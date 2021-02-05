# read data file
readInput() = split(read("d09-input.txt", String), "\n")
data = readInput()
# test data
# data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 25 #25 for main problem, 5 for testing

for (idx, i) in enumerate(data[preamble:end])
    solution = false
    # print("idx",idx,"i",i)
    for j in data[idx:idx+preamble]
        for k in data[idx:idx+preamble]
            if (j + k == i) &  (j != k)
                # print("i",i,"j",j,"k",k)
                solution = true
                break
            end
        end
        if solution == true
            break
        end
    end
    if solution == false
        print(i)
        break
    end
end