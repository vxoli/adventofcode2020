using DelimitedFiles

f = open("d03-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)
global trees = 0
global col = 1
global line_length = length(data[1])
for row in 1:length(data)
    println(row, " ", col)
#    if data[row][col] == "#"
#        trees += 1
#    end
    col = (col + 3) % (line_length+1)
end
print(trees)
