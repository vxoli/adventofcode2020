f = open("d04-input.txt", "r")
data = read(f, String)
close(f)
# need to strip the double '\n\n' from the dataset
data = split(data, "\n\n")
# Part 1
valid = 0
for passport in data
	if (occursin("byr", passport) & occursin("iyr", passport) & occursin("eyr", passport) & occursin("hgt", passport) & occursin("hcl", passport) & occursin("ecl", passport) & occursin("pid", passport))
        global valid = valid + 1
    end
end
print("Part 1: Valid passports = $valid")