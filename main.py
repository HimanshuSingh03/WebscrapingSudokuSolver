import requests
from bs4 import BeautifulSoup
import numpy as np


tempgrid = []
grid = []


def scrape():
        print("scraping...")
        
        req = requests.get("https://sudokugenerator.com/sudoku/daily/")
        soup = BeautifulSoup(req.content, "html.parser")

        rows = soup.find_all('input', type="text")

        for row in rows:
                value = row.get('value')
                tempgrid.append(value)
        
        for x in range(len(tempgrid)):
                if tempgrid[x] == '':
                        tempgrid[x] = 0
                else:
                        tempgrid[x] = int(tempgrid[x])

        return tempgrid




def arrangegrid(tempgrid):
        global grid

        print("arranging...")

        for k in range(3):

                for i in range(3):
                        row_array = []
                        

                        for j in range(3):

                                index = ((9*j) + 3*i) + k*27
                                row_array.append(tempgrid[index])
                                
                                index = ((9*j +1) + 3*i) + k*27
                                row_array.append(tempgrid[index])
                                
                                index = ((9*j +2) + 3*i) + k*27
                                row_array.append(tempgrid[index])
                                
                        grid.append(row_array)

        
        return grid









def fitHere(y,x,n):
        global grid
        
        for i in range(9):
                if grid[y][i] == n: #check rows
                        return False
                if grid[i][x] == n: #check columns
                        return False
        
        ysquare = y//3
        xsquare = x//3 #can only be 0,1,2
        

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

        tempgrid = scrape()
        sudoku = arrangegrid(tempgrid)
        print("Daily Sudoku: \n", np.matrix(sudoku))
        
        print("\n Solved Sudoku:")
        solve()
        
main()