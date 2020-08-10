import  tic
import  copy
from  gridgenerator import *
WIDTH = 600
HEIGHT =600
PINK =(31,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,63,255)
LIGHTBLUE = (40,255,206)
RED = (255,0,50)
GREEN = (57,255,9)
YELLOW =(255,220,40)
GREY = (61,61,61)
ORANGE = (172,0,255)
AlPHAYELLOW = (55,144,0)
testboard = [[0 for x in range(9)] for x in range(9)]
sudokuu = sudoku()

grid = sudokuu.MakeSudoku()
gridcopy = copy.deepcopy(grid)
gridtempcopy = copy.deepcopy(grid)
# tic.solve(solved_board)
# tic.solve(testboard1)
# tic.print_board(solved_board)




gridpos = (75,100)
cellsize = 50
gridsize = cellsize*9
#Corners Of grid
leftup = (74, 96)
leftdown = (75, 548)
rightup = (523, 100)
rightdown = (525, 570)
