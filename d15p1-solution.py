# given data set of starting numbers
data = [0,5,4,1,10,14,7]

spokenNumbers = {} #{i:0 for i in data}
turn = 0
numberSpoken = 0

# loop through starting numbers
while turn < 2020:
    turn += 1
    spokenNumber = data[turn-1]
    if spokenNumber in spokenNumbers:
        spokenNumbers[spokenNumber] = turn
        data.append(spokenNumber)
    else:
        spokenNumbers.update({spokenNumber:0})
        print(spokenNumbers)
        spokenNumbers[spokenNumber] = 0
        data.append(spokenNumber)

print(data, spokenNumbers)
