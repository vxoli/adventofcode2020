using DelimitedFiles
f = open("d05-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)

# Part 1

global maxseatid=0
for line in data
    # split the ticketdata into row and seat info
    global row_code = line[1:7]
    global seat_code= line[8:end]
    global seatid = 0
    global seatrow = 0:127
    global seatnum = 0:7

    for s in row_code
        if s == 'F'
            global seatrow = seatrow[1:Integer(length(seatrow)/2)]
        else
            global seatrow = seatrow[Integer(length(seatrow)/2)+1:end]
        end
    end

    for s in seat_code
        if s == 'L'
            global seatnum = seatnum[1:Integer(length(seatnum)/2)]
        else
            global seatnum = seatnum[Integer(length(seatnum)/2)+1:end]
        end
        global seatid = seatrow[1] * 8 + seatnum[1]
        global maxseatid = (seatid * (seatid > maxseatid)) + (maxseatid * (seatid <= maxseatid))
    end
end

println(seatrow[1]," ", seatnum[1], " ", seatid, " ", maxseatid)

# Part 2
maxseatid=0
seatid=[]

for idx, line in enumerate(data):
    row_code = line[:7]
    seat_code= line[7:]
    seatrow = []
    for s in range(0,128,1):
        seatrow.append(s)
    for s in row_code:
        if s == "F":
            seatrow = seatrow[:int(len(seatrow)/2)]
        else:
            seatrow = seatrow[int(len(seatrow)/2):]
    seatnum = []
    for s in range(0,8,1):
        seatnum.append(s)
    for s in seat_code:
        if s == "L":
            seatnum = seatnum[:int(len(seatnum)/2)]
        else:
            seatnum = seatnum[int(len(seatnum)/2):]
    seatid.append(seatrow[0] * 8 + seatnum[0])

seatid.sort()
for s in range(0,len(seatid)-1):
    if (seatid[s+1] - seatid[s]) == 1:
        continue
    else:
        print((seatid[s+1]+seatid[s]) / 2)

