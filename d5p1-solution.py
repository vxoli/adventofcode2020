f = open('d5-input.txt', 'r')
data = f.readlines()
for line in data:
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
    print(seatrow,seatnum)
