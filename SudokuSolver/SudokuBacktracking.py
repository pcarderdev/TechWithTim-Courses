import numpy as np
'''
Naive algorithm:
1. Pick empty square
2. Try all numbers
3. Find one that works
4. Repeat
5. Backtrack
'''
board = np.array([ 
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
])

solution = np.array([
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
])

def checkSolution(board,i,j,value):
    # Check row - value in board[i]
    # Check column - value in board[:,j]
    # Check box - value in board[x:x+2,y:y+2]
    # x and y values determine start indices of the box
    x = i-i%3
    y = j-j%3
    if(value in board[i] or value in board[:,j] or value in board[x:x+3,y:y+3]):
        return False
    return True

def backTracking(board, i, j):
    if j==9:
        if i==8:
            return True
        i+=1
        j=0
    if board[i,j] == 0:
        val = 1
        while val < 10:
            if (checkSolution(board, i, j, val)):
                board[i,j] = val
                if (backTracking(board, i, j+1)):
                    return True
            val+=1
        board[i,j] = 0
        return False
    return backTracking(board, i, j+1)

backTracking(board, 0, 0)
print(np.array_equal(board, solution))

            


    
    



