# read input file

f = open("d23-input.txt","r")
data = f.readlines()
# split numbers into list and drop 0th entry containing original number read form file
for i in range(len(data[0])):
    data.append(int(data[0][i]))
data.pop(0)

# test data
data = [int(i) for i in "389125467"]

cups = data
numberCups = len(cups)
currentCup = cups[0]
for turn in range (0,5):
    print("Turn: ",turn+1)
    #The crab picks up the three cups that are immediately clockwise of the current cup.
    pickupCups = [cups[(cups.index(currentCup)+1) % numberCups],cups[(cups.index(currentCup)+2) % numberCups],cups[(cups.index(currentCup)+3) % numberCups]]
    # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
    cups.remove(pickupCups[0])
    cups.remove(pickupCups[1])
    cups.remove(pickupCups[2])
    print("cups with pickup removed", cups, "Pickup: ",pickupCups)
    # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
    destinationCup = (currentCup - 1) + ((currentCup - 1 < min(cups)) * max(cups))
    print("destination cup", destinationCup)
    # If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up.
    while not(destinationCup in cups):
        destinationCup -= 1
    # If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
        destinationCup = ((destinationCup >= min(cups)) * destinationCup) + ((destinationCup < min(cups)) * (max(cups)))
    print("destination cup corrected", destinationCup)
    # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
    for i in range(len(pickupCups)):
        # delist the elements of pickupCups and add back to cups
        print(i, i+len(pickupCups), pickupCups[i],cups.index(destinationCup)+1+i,cups.index(destinationCup) )
        if cups.index(destinationCup) == 0:
            # store index of destinationCup as will change as string chages
            destinationCupIndex = 0
            # first element becomes last
            print(cups)
            cups.append(cups[0])
            print(cups)
            cups.pop(0)
            print(cups)
            #cup added to front
            cups.insert(0, pickupCups[i])
            print(cups)
        else:
            cups.insert(cups.index(destinationCup)+1+i, pickupCups[i])
    # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
    currentCup = cups[(cups.index(currentCup)+1) % numberCups]
    print(currentCup, cups)


