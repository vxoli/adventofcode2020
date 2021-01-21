using DelimitedFiles
f = open("d05-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)
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
