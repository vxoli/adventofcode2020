readInput() = split.(split(read("d06-input.txt", String), "\n\n"))
data = readInput()

# Part 1

global count = 0
for line in data
	txt = ""
	for x in 1:length(line)
		txt = union(txt,line[x])
	end
	global count += length(txt)
end
println(count)

# Part 2

