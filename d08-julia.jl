# read data file
readInput() = split(read("d08-input.txt", String), "\n")
data = readInput()
# test data
# data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]

# initialise variables
global codeLine = 1
global accumulator = 0
global executedCodeLines = []
global repeatedLines = false

# loop until a line is repeated
while !(repeatedLines)
    # split input data into components
    command = data[codeLine][1:3]
    value = parse(Int64, data[codeLine][5:end])
    # if the line of code has been executed then change the repeatedLines variable
    if codeLine in executedCodeLines
        global repeatedLines = true
        break
    else push!(executedCodeLines, codeLine)
    end
    # executed the commands
    if command == "acc"
        global accumulator += value
        global codeLine += 1
    end
    if command == "nop"
        codeLine += 1
    end
    if command == "jmp"
        codeLine += value
    end
end
# print result
println("Immediately before any instruction is executed a second time, what value is in the accumulator?")
println(accumulator)
