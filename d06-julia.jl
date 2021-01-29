readInput() = split.(split(read("d06-input.txt", String), "\n\n"))
data = readInput()

# Part 1

global part1 = 0
global part2 = 0
for line in data
	txt = ""
	for x in 1:length(line)
		txt = ∪(txt,line[x]) # ∪ symbol for union
	end
	global part1 += length(txt)
end
println("the number of questions to which anyone answered "yes" = : $part1")

# Part 2

