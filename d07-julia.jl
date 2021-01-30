readInput() = split(read("d07-input.txt", String), "\n")
data = readInput()

# data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.", "dark orange bags contain 3 bright white bags, 4 muted yellow bags.", "bright white bags contain 1 shiny gold bag." , "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags." , "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags." , "dark olive bags contain 3 faded blue bags, 4 dotted black bags.", "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags." , "faded blue bags contain no other bags.", "dotted black bags contain no other bags."]
myBags = []
data_clean = [split(data[i], " contain ") for i in 1:length(data)]

# find the bags that can contain "shiny gold bags"
myBags = [data_clean[s][1][1:length(data_clean[s][1])-5] for s in 1:length(data_clean) if occursin("shiny gold", data_clean[s][2])]

# find bags that can contain bags that can contain "shiny gold bags"
for bag_col in myBags
	union(myBags, [data_clean[s][1][1:length(data_clean[s][1])-5] for s in 1:length(data_clean) if occursin(bag_col, data_clean[s][2])])
end
# remove duplicate bag colours
myBags = list(dict.fromkeys(myBags))	
print(myBags)
print(len(myBags))