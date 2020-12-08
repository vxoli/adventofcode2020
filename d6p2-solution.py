import string
f = open('d6-input.txt', 'r')
data = f.readlines()
data_clean = []
lst = ""
count = 0
group = []
lttrs = []
for lines in data:
	group.append(lines)
	if lines == "\n":
		for i in range(0,len(group)-1):
			for idx, letter in enumerate(string.ascii_lowercase):
				print(idx, letter, i, group[i])
				if letter in group[i]:
					lttrs[idx] += 1
					print(lttrs[idx])
#				if letters[idx] == len(group)-1:
#					count += 1
		group = []
		lttrs = []
print(count)
# clean data string - get groups into one line each
#for lines in data:
#	if lines == "\n":
#		data_clean.append(lst.replace("\n", ""))
#		lst = ""
#		continue
#	else:
#		lst += lines
