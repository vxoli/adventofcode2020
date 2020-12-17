# given data set of starting numbers
data = [0,5,4,1,10,14,7]

# test data
data = [0,3,6]

spokenNumbers = {} #{i:0 for i in data}
turn = 0
numberSpoken = data[0]

# loop through starting numbers
while turn < 2020:
    turn += 1
    if turn <= 3:
        spokenNumber = data[turn-1]
        print(spokenNumber)
    if spokenNumber in spokenNumbers:
        spokenNumbers[spokenNumber] = turn - spokenNumbers[spokenNumber]
        data.append(spokenNumber)
    if not(spokenNumber in spokenNumbers):
        spokenNumbers.update({spokenNumber:turn})
        data.append(spokenNumber)

print(data, spokenNumbers)
