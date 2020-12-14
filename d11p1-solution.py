# read data file
f = open('d11-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
#test data
data = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]
rowWidth = len(data[0])
numRows = len(data)
oldData = data
newData = data
cardinalPoints = []
for row in range(numRows):
    for col in range(rowWidth):
        # cardinalPoints represent in row,col
        # [immediately up, immediatly down, immediately left, immediatly right, diagonal up-left, diagonal up-right, diagonal down-left, diagonal-down-right]
        cardinalPoints = [["up",row-1,col],["down",row+1,col],["left",row,col-1],["right",row,col+1],["up-left",row-1,col-1],["up-right",row-1,col+1],["down-left",row+1,col-1],["down-right",row+1,col+1]]
        # consider each seat simultaneously
        # consider immediatly up
        if row -1 >= 0 and col - 1 >= 0 and row + 1 <= numRows and col + 1 <= rowWidth:
            # Floor (.) never changes; seats don't move, and nobody sits on the floor.
            if data[row][col] == ".":
                continue
            # apply rules:
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            # Otherwise, the seat's state does not change.
