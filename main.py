import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print(np.matrix(grid))

def fitHere(y,x,n):
        for i in range(9):
                if grid[y][i] == n: #check rows
                        return False
                if grid[i][x] == n: #check columns
                        return False
        
        xsquare = x//3 #can only be 0,1,2
        ysquare = y//3

        for i in range(3):
                for j in range(3):
                        if grid[(xsquare*3 + 1)+i][(xsquare*3 + 1)+i] == n:
                                return False

        return True


print(fitHere(0,2,6))

