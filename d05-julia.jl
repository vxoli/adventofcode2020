using DelimitedFiles
f = open("d05-input.txt")
data = readdlm(f, '\t', String, '\n')
close(f)
println(data)
maxseatid=0

for line in data
    # split the ticketdata into row and seat info
    row_code = line[1:7]
    seat_code= line[8:length(line)]
    seatrow = []
    seatid = 0
    for s in range(0,128,1)
        seatrow.append(s)
    end
    for s in row_code
        if s == "F"
            seatrow = seatrow[1:length(seatrow)/2]
        else
            seatrow = seatrow[(length(seatrow)/2)+1:length(seatrow)]
        end
    end
    seatnum = []
    for s in range(0,8,1)
        seatnum.append(s)
    end
    for s in seat_code
        if s == "L"
            seatnum = seatnum[1:length(seatnum)/2]
        else
            seatnum = seatnum[(length(seatnum)/2)+1:length(seatnum)]
        end
    end
end
    seatid = seatrow[0] * 8 + seatnum[0]
    maxseatid = (seatid * (seatid > maxseatid)) + (maxseatid * (seatid <= maxseatid))
    print(seatrow,seatnum, seatid, maxseatid)
