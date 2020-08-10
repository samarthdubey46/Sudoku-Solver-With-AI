import random

class sudoku:
    def __init__(self):
        self.grid = Grid = [[0 for x in range(9)] for y in range(9)]

    def MakeSudoku(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = 0
        for i in range(7):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
            while (not self.CheckValid(self.grid, row, col, num) or self.grid[row][col] != 0):  # if taken or not valid reroll
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            self.grid[row][col] = num
        return self.grid

    def CheckValid(self,Grid, row, col, num):
        # check if in row
        valid = True
        # check row and collumn
        for x in range(9):
            if (Grid[x][col] == num):
                valid = False
        for y in range(9):
            if (Grid[row][y] == num):
                valid = False
        rowsection = row // 3
        colsection = col // 3
        for x in range(3):
            for y in range(3):
                # check if section is valid
                if (Grid[rowsection * 3 + x][colsection * 3 + y] == num):
                    valid = False
        return valid

