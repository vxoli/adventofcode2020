f = open('d7-input.txt', 'r')
data = f.readlines()

data_clean = [data[i].split("contains") for i in range(len(data))]
matching = [data_clean[s] for s in range(len(data_clean)) if "shiny gold" in data_clean[s][1]]

print(len(matching))