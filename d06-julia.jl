readInput() = split.(split(read("d06-input.txt", String), "\n\n"))
data = readInput()

global count = 0

for lines in data
    # loop through a...z
    for letter in collect('a':'z')
        # if that letter in the line increment counter
		if occursin(letter, string(lines))
            global count += 1
        end
    end
end
println(count)
