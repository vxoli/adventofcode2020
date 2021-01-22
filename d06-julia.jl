using DelimitedFiles
f = open("d06-input.txt", "r")
data = readdlm(f,'\t', String, '\n')
close(f)

global data_clean = []
global list = ""
global count = 0

# clean data string - get groups into one line each
#for lines in data
#	if lines == '\n'
#		global data_clean = data_clean * replace(list, "\n" => "")
#		global list = ""
#		continue
#	else
#        global list = list * lines
#    end
#end
# loop through each line
for lines in data
# loop through a...z
    for letter in collect('a':'z')
# if that letter in the line increment counter
		if letter in lines
            global count += 1
        end
    end
end
println(count)
