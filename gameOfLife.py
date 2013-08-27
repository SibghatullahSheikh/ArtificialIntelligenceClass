originalMatrix = [	[0, 0, 0, 0, 0, 0], #0
					[0, 0, 0, 0, 0, 0], #1
					[0, 1, 0, 1, 0, 0], #2
					[0, 0, 1, 1, 0, 0], #3
					[0, 0, 1, 0, 0, 0], #4
					[0, 0, 0, 0, 0, 0]] #5

rowsLength = len(originalMatrix) # number of rows in matrix
colLength = len(originalMatrix[0]) # number of col in matrix
padValue = 9 #val of pad

for row in range(0, rowsLength):
	originalMatrix[row].append(padValue)
	originalMatrix[row].insert(0, padValue)
	
originalMatrix.append([padValue] * (rowsLength+2)) #pad matrix perimeter with -1
originalMatrix.insert(0, [padValue] * (rowsLength+2))

#### End of initialization
newMatrix = [		[9, 9, 9, 9, 9, 9, 9, 9],
					[9, 0, 0, 0, 0, 0, 0, 9], #0
					[9, 0, 0, 0, 0, 0, 0, 9], #1
					[9, 0, 0, 0, 0, 0, 0, 9], #2
					[9, 0, 0, 0, 0, 0, 0, 9], #3
					[9, 0, 0, 0, 0, 0, 0, 9], #4
					[9, 0, 0, 0, 0, 0, 0, 9],
					[9, 9, 9, 9, 9, 9, 9, 9]] #5

def printFormattedMatrix(matrix):
	for row in range(0, len(matrix)):
		print matrix[row]
	
#printFormattedMatrix(originalMatrix)
	

					


for row in range(1, len(originalMatrix)-1): #loop thru rows of matrix
	for col in range(1, len(originalMatrix[row])-1):
		#print "%s, %s" %(row, col)
		neighbors = ["0"] * 8
		neighbors[0] = originalMatrix[row-1][col-1]
		neighbors[1] = originalMatrix[row-1][col]
		neighbors[2] = originalMatrix[row-1][col+1]
		neighbors[3] = originalMatrix[row][col-1]
		neighbors[4] = originalMatrix[row][col+1]
		neighbors[5] = originalMatrix[row+1][col-1]
		neighbors[6] = originalMatrix[row+1][col]
		neighbors[7] = originalMatrix[row+1][col+1]
		#printFormattedMatrix(originalMatrix)

		#print "Live Neighbors: %s" %neighbors.count(1)
		#print "Self: %s" %originalMatrix[row][col]

		#print
		self = originalMatrix[row][col] 

		if(self == 0):
			if(neighbors.count(1) == 3):
				newMatrix[row][col] = 1

		if(self == 1):
			if(neighbors.count(1) <= 1 or neighbors.count(1) >= 4):
				newMatrix[row][col] = 0
			else:
				newMatrix[row][col] = self

	 

	
def returnClockwiseNeighbors(matrix, x, y):
	return null
	


print printFormattedMatrix(newMatrix)