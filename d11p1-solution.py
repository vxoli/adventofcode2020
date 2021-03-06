# read data file
f = open('d11-input.txt', 'r')
data = [line.rstrip() for line in f.readlines()]

#test data
#data = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]

# ensure input data in list
data = [list(line) for line in data]

rowWidth = len(data[0])
numRows = len(data)
deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def count_occupied(row,col,grid):
	count = 0
	for i,j in deltas:
		xi,xj = row+i,col+j 
		if 0<=xi<numRows and 0 <=xj<rowWidth and grid[xi][xj] == "#":
			count += 1
	return count

def check_occupied(lines, thresh = 4):
	while True:
		valid = True
		temp_grid=[r.copy() for r in lines]
		for i,r in enumerate(temp_grid):
			for j,c in enumerate(r):
				count = count_occupied(i,j,temp_grid)
				if c == "L" and count ==0:
					lines[i][j] = "#"
				elif c == "#" and count >=thresh:
					lines[i][j]="L"
				valid&=(r[j]==lines[i][j])
		if valid:
			break
	ans = 0
	for i in range(numRows):
		for j in range(rowWidth):
			if lines[i][j] == "#":
				ans += 1
	print(f"There are {ans} valid seats.")
check_occupied(data)