using DelimitedFiles

f = open("d02-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)

# data = [x.strip().split() for x in data]
valid = 0
for row in 1:length(data)
	# min value = split(split(data[row])[1],"-")[1]
	# max value = split(split(data[row])[1],"-")[2]
	# character = split(split(data[row])[2],":")[1]
	# password to test = split(data[row])[3]
	# number occurances of letter = length(collect(eachmatch(Regex(split(split(data[row])[2],":")[1]), split(data[row])[3])))
	maximum = parse(Int, split(split(data[row])[1],"-")[2])
	minimum = parse(Int, split(split(data[row])[1],"-")[1])
    char_count = length(collect(eachmatch(Regex(split(split(data[row])[2],":")[1]), split(data[row])[3])))
	global valid += (char_count >= minimum) * (char_count <= maximum)
end
print("Part 1: Valid passwords: ", valid)