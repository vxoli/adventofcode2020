# read data file
f = open('d16-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
# Test data
# data = ["class: 1-3 or 5-7","row: 6-11 or 33-44","seat: 13-40 or 45-50","your ticket:","7,1,14","","nearby tickets:","7,3,47","40,4,50","55,2,20","38,6,12"]

# Split data into areas - fields, my ticket, nearby tickets
fields, myTicket, nearbyTickets = {}, [], []
# split fields into dictionary with class type, min and max values
for idx, line in enumerate(data):
    if line == "": continue
    if line[:11] == "your ticket":
        break
    # split the line into text before the colon to form the key, then the value pairs afer the colon seperated by ' or ' to form value pairs
    fields[line.split(": ")[0]] = (line.split(": ")[1].split(" or ")[0], line.split(": ")[1].split(" or ")[1])
    #the min of the min value
    min_min = int(fields[line.split(": ")[0]][0].split("-")[0])
    # the max of the min value
    min_max = int(fields[line.split(": ")[0]][0].split("-")[1])
    #the min of the max value
    max_min = int(fields[line.split(": ")[0]][1].split("-")[0])
    #the max of the max value
    max_max = int(fields[line.split(": ")[0]][1].split("-")[1])
    # redefine the dictionary entry with new min/max values
    fields[line.split(": ")[0]] = (min_min, min_max, max_min, max_max)
# split myTicket data into list
for line in data[idx+1:]:
    if line == "": continue
    if line[:14] == "nearby tickets":
        break
    myTicket.append(line)
# split nearbyTicket data into list
for line in data[idx+4:]:
    if line == "": continue
    nearbyTickets.append(line)
# ignore my ticket
# loop though each field, and compare ticket values to given parameters
# store sum of invalid parameters
# can combine all parameters into one set to compare with each line of list
validParams = set() # define empty set
ticketScanningErrorRate = 0
# add paramteters to set as union of sets of values from fields
for keys in fields:
    validParams = validParams.union(set(range(fields[keys][0],fields[keys][1]+1)),set(range(fields[keys][2],fields[keys][3]+1)))
# loop though nearbyTickets and identify invalid tickets
inValid = set()
validTickets = set()
for ticket in nearbyTickets:
    values = ticket.split(",")
    for value in values:
        if not(int(value) in validParams):
            inValid.add(ticket)
# remove inValid tickets and generaate list of validTickets
validTickets = set(nearbyTickets).difference(inValid)
# using valid tickets loop though
# a dictionary to hold possible fields for each col
valid_tickets = list(validTickets)
possibleFields = {i: set(fields.keys()) for i in range(len(validTickets))}
for ticket in validTickets:
    for i, value in enumerate(ticket.split(",")):
        print(i,value)
        for field in fields:
            possible = False
            if value in fields[field]: # have to adapt fields[field] to work with my code.
                possible = True
            if not possible:
                possibleFields[i].discard(field)
print(possibleFields)
