using DelimitedFiles

f = open("d04-input.txt")
data = readdlm(f, '\n', String, '\n')
close(f)
valid = 0
for passport in data
    println(passport)
	if (occursin("byr", passport) & occursin("iyr", passport) & occursin("eyr", passport) & occursin("hgt", passport) & occursin("hcl", passport) & occursin("ecl", passport) & occursin("pid", passport))
        global valid = valid + 1
    end
end
print(valid)