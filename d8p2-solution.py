# read data file
f = open('d8-input.txt', 'r')
data = f.readlines()
# test data
data = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"]

# initialise variables
codeLine = 0
accumulator = 0
executedCodeLines = []
lastJmpLine = []
repeatedLines = False

# TRY:
# identify all the lines with jmp or nop
# loop through the list changing each in turn to the other
# if code executes - flag success
# if code repeats revert data set and swop next matching command and try again

# while until a line is repeated
while not(repeatedLines):
    # split input data into components
    command = data[codeLine][0:3]
    value = data[codeLine][3:]
    # if the line of code has been executed then change the repeatedLines variable
    if codeLine in executedCodeLines:
        repeatedLines = True
        break
    else: executedCodeLines.append(codeLine)
    # executed the commands
    if command == "acc":
        accumulator += int(value)
        codeLine += 1
    if command == "nop":
        codeLine += 1
    if command == "jmp":
        codeLine += int(value)

# change jmp to noc in penultiate jmp executed
lineToChange = int(executedCodeLines[-2])
if data[lineToChange][0:3] == "jmp":
    data[lineToChange] = data[lineToChange].replace("jmp","nop")
if data[lineToChange][0:3] == "nop":
    data[lineToChange] = data[lineToChange].replace("nop", "jmp")

# rerun routine
# reset variables
codeLine = 0
accumulator = 0
executedCodeLines = []
lastJmpLine = []
repeatedLines = False

# while loop till end of code segment reached
while codeLine <= len(data)-1:
    # split input data into components
    print(codeLine, data[codeLine], lineToChange, repeatedLines)
    command = data[codeLine][0:3]
    value = data[codeLine][3:]
    # if the line of code has been executed then change the repeatedLines variable
    if codeLine in executedCodeLines:
        repeatedLines = True
        break
    else: executedCodeLines.append(codeLine)
    # executed the commands
    if command == "acc":
        accumulator += int(value)
        codeLine += 1
    if command == "nop":
        codeLine += 1
    if command == "jmp":
        lastJmpLine.append(codeLine)
        codeLine += int(value)

print(accumulator, lineToChange, codeLine, repeatedLines)