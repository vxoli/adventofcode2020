# read data file
f = open('d11-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]
#test data
data = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]
rowWidth = len(data[0])
numRows = len(data)
oldData = data
newData = [i.replace("L","#") for i in data]
cardinalPoints = []
unoccupied = ["L","."]
occupied = ["#"]
for row in range(0,numRows-1):
	for col in range(0,rowWidth-1):
		# cardinalPoints represent in row,col
		# [immediately up, immediatly down, immediately left, immediatly right, diagonal up-left, diagonal up-right, diagonal down-left, diagonal-down-right]
		cardinalPoints = [["up",row-1,col],["down",row+1,col],["left",row,col-1],["right",row,col+1],["up-left",row-1,col-1],["up-right",row-1,col+1],["down-left",row+1,col-1],["down-right",row+1,col+1]]
		# consider each seat simultaneously
		# consider immediatly up
		# Floor (.) never changes; seats don't move, and nobody sits on the floor.
		if oldData[row][col] == ".":
			continue
		# apply rules:
		# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
		if oldData[row][col] == "L" and row - 1 >=0 and col - 1 >=0 and row + 1 <= numRows and col + 1 <= rowWidth:
			print("row",row,"col",col, "nrow", numRows, "ncol",rowWidth)
		#	print("up",oldData[row-1][col],"down",oldData[row+1][col],"left",oldData[row][col-1],"right",oldData[row][col+1],"up-left",oldData[row-1][col-1],"up-right", oldData[row-1][col+1],"down-left",oldData[row+1][col-1],"down-right",oldData[row+1][col+1])
				
			if oldData[row-1][col] in unoccupied and oldData[row+1][col] in unoccupied and oldData[row][col-1] in unoccupied and oldData[row][col+1] in unoccupied and oldData[row-1][col-1] in unoccupied and oldData[row-1][col+1] in unoccupied and oldData[row+1][col-1] in unoccupied and oldData[row+1][col+1] in unoccupied:
				newData[row][col] == "#"
		# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
		if oldData[row][col] == "#" and row - 1 >=0 and col - 1 >=0 and row + 1 <= numRows and col + 1 <= rowWidth:
			counter = 0
			if oldData[row-1][col] in occupied:
				counter += 1
			if oldData[row+1][col] in occupied:
				counter += 1
			if oldData[row][col-1] in occupied:
				counter += 1
			if oldData[row][col+1] in occupied:
				counter += 1
			if oldData[row-1][col-1] in occupied:
				counter += 1
			if oldData[row-1][col+1] in occupied:
				counter += 1
			if oldData[row+1][col-1] in occupied:
				counter += 1
			if oldData[row+1][col+1] in occupied:
				counter += 1
			if counter >=4:
				newData[row][col] == "L"
        # Otherwise, the seat's state does not change.
			else:
				newData[row][col] = oldData[row][col]
				
for i in oldData:
	print(i)
for i in newData:
	print(i)