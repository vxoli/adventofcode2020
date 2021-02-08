# read data file
readInput() = split(read("d09-input.txt", String), "\n")
stringData = readInput()
# convert strings to Integer
data = []
for i in stringData
    push!(data, parse(Int,i))
end

# test data
# data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
preamble = 25 #25 for main problem, 5 for testing

for (idx,i) in enumerate(data[preamble+1:end])
    global solution = false
    # println("idx",idx," i",i)
    for j in data[idx:idx+preamble-1]
        for k in data[idx:idx+preamble-1]
            if (j + k == i) &&  (j != k)
                # println("i",i,"j",j,"k",k)
                global solution = true
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