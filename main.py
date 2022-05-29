import requests
from bs4 import BeautifulSoup
import numpy as np


req = requests.get("https://sudokugenerator.com/sudoku/daily/")

soup = BeautifulSoup(req.content, "html.parser")


rows = soup.find_all('tr', class_="sudoku_row")

for row in rows:

        value = row.input['value']
        print(value)
        



grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


def fitHere(y,x,n):

        #print("checking ",n)
        for i in range(9):
                if grid[y][i] == n: #check rows
                        return False
                if grid[i][x] == n: #check columns
                        return False
        
        ysquare = y//3
        xsquare = x//3 #can only be 0,1,2
        
        #print(ysquare,xsquare)

        for i in range(3):
                for j in range(3):
                        if grid[(ysquare*3)+i][(xsquare*3)+j] == n:
                                return False

        return True

def solve():
        global grid
        for y in range(9):
                for x in range(9):
                        if grid[y][x] == 0:
                                for n in range(1,10):
                                        if fitHere(y,x,n):
                                                grid[y][x] = n
                                                solve()
                                                grid[y][x] = 0
                                return
        print(np.matrix(grid))

def main():
        print("Current Sudoku: \n", np.matrix(grid))
        print("\n Solved Sudoku:")
        solve()

