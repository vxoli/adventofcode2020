using DelimitedFiles

f = open("d03-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)
global trees = 0
global col = 1
global line_length = length(data[1])
for row in 1:length(data)
    if data[row][col] == '#'
        global trees += 1
    end
    global col = (col + 2) % (line_length)+1 # julia doesnt allow zero index - this calulates across 2 mod line_length then adds one to make total across 3
end
print("Trees encountered: $trees")
