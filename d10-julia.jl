# read data file
stringData = split(read("d10-input.txt", String), "\n")
# convert strings to Integer
data = []
for i in stringData
    push!(data, parse(Int,i))
end
println(data)
# test data
data = [16,10,15,5,1,11,7,19,6,12,4]
# data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

# start solution
global rating = 0
global selectedAdaptors = []
global differences = [0,0,0,0]
for i in data
    global rating
	global possibleAdaptors = []
	for j in data
		if j in selectedAdaptors
			continue
        end
		if (j - rating) <=3
			push!(possibleAdaptors, j)
        end
	differences[1] += (minimum(possibleAdaptors) - rating) == 1
	differences[2] += (minimum(possibleAdaptors) - rating) == 2
	differences[3] += (minimum(possibleAdaptors) - rating) == 3
	rating += minimum(possibleAdaptors) - rating
	push!(selectedAdaptors,data[data.index(minimum(possibleAdaptors))])
    end
end
    # rating increased by 3
rating += 3
# number of differences of 3 increased by 1
differences[3] += 1

print(rating)
print(differences)
print(differences[1] * differences[3])
