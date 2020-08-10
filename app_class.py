import  pygame
from  tic import  *
from  settings import *
import  numpy as np
import  time
import sys
# from Intro import *
from  Buttons import *
import  tic

class App:
    def __init__(self):
        pygame.init()
        self.timeee = None
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        self.grid = grid
        self.prelockedcels = []
        self.solved = False
        self.selected = None
        self.mousepos = None
        self.state = "Playing"
        self.finished = False
        self.cellchanged = False
        self.font = pygame.font.SysFont("arial",cellsize // 2)
        self.playingButtons = []
        self.lockedcells = []
        self.changed_cells = []
        self.incorrect_cells = []
        self.correctcells = []
        self.cck = None
        self.tempgrid1 = gridtempcopy
        self.mchanged = None
        self.gridcopy = gridcopy
        self.clicked = False
        self.load()
        self.mouseposclick = (0,0)
        # print(s)

    def run(self):
        start = time.time()
        temp = None
        while self.running:
            # if self.finished != True:
            playtime = round(time.time() - start)
            if self.state == "Playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
                self.timeee = self.format_time(playtime)
                pygame.display.update()

        pygame.quit()
        # sys.exit()


    ###### PLAYING STATE FUNCTIONS #####
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = self.mouseonboard()
                print(pygame.mouse.get_pos())
                self.mouseposclick = pygame.mouse.get_pos()
                for i in self.playingButtons:
                    if self.mouseposclick[0] > i.x and self.mouseposclick[0] < i.x + i.width and self.mouseposclick[1] > i.y and self.mouseposclick[1] < i.y + i.height:
                        i.para = True
                    else:
                        i.para = False
                    print(self.clicked)
                if(self.selected):
                    pass
                else:
                    self.selected = None
                    for button in self.playingButtons:
                        if button.highlited:
                            button.click()

            # USER CLICK
            if event.type == pygame.KEYDOWN:
                if self.selected and self.selected not in self.lockedcells:
                    if str(event.unicode).isdigit() and event.unicode != '0':
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.gridcopy[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.cellchanged = True
                        self.mchanged = self.selected
                        num = self.grid[self.selected[1]][self.selected[0]]
                        pos = (self.selected[1],self.selected[0])
                        self.incorrect_cells = []
                        if valid(self.grid,num=num,pos=pos) and solve(self.gridcopy):
                            print("Right",num,pos)
                        else:
                            self.incorrect_cells.append(self.selected)
                            print("Wrong", num, pos)
                if event.key == pygame.K_a:
                    solve(self.tempgrid1)
                    self.grid = self.tempgrid1
                    self.incorrect_cells = []
                    self.drawnumber(self.window, "WON", [100,100], YELLOW)
                    print("Congrats")
                    # self.finished = True
                    # self.lockedcells = []


    def playing_update(self):
        self.mousepos = pygame.mouse.get_pos()
        mouse_temp = (self.mousepos[0],self.mousepos[1] - 40)
        for button in self.playingButtons:
            if button.para != False:
                button.function()
            button.update(mouse_temp)
        if self.cellchanged:
            # self.incorrect_cells = []
            if self.allcelldone(self.grid):
                # self.checkallcells()
                for yidx,row in enumerate(self.grid):
                    for xidx,num in enumerate(row):
                        if  valid(self.grid,num,(yidx,xidx)) and [xidx,yidx] not in self.lockedcells:
                            pass
                        else:
                            if [xidx,yidx] not in self.lockedcells:
                                self.incorrect_cells.append([xidx,yidx])
                                print([yidx,xidx])


                print("con")
    def tetx(self,window):
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('WINNER', True, GREEN, BLACK)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        window.blit(text,textRect)
    def playing_draw(self):
        self.window.fill(BLACK)
        for button in self.playingButtons:
            button.draw(self.window)
        if self.selected:
            self.drawselect(self.window,self.selected)
        self.shadelocked(self.window,self.lockedcells,PINK)
        self.shadelocked(self.window,self.incorrect_cells,RED)
        self.drawnumbers(self.window)
        self.Drawgrid(self.window)
        self.displaytime(self.timeee)
        for i in self.playingButtons:
            if i.text != None:
                i.show_text()
        if self.finished:
            pass
        if self.allcelldone(self.grid):
            if len(self.incorrect_cells) == 0:
                self.tetx(self.window)

        pygame.display.update()
        self.cellchanged = False
    ### BOARD FUNCTIONS #####
    def allcelldone(self,grid):
        for row in grid:
            for num in row:
                if num == 0:
                    return  False
        return  True
    def checkallcells(self):
        self.checkrows()
        self.checkColumnswhendone()
        self.checksmallgridwhendone()
        if len(self.incorrect_cells) == 0:
            print("Congrats")
    def checkrows(self):
        for yidx,row in enumerate(self.grid):
            possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(9):
                if self.grid[yidx][i] in possibles:
                    possibles.remove(self.grid[yidx][i])
                    # print("Right")
                else:
                    if [i,yidx] not in self.lockedcells:
                        self.incorrect_cells.append([i,yidx])
                        # print("WRONG")
                    if [i,yidx] in self.lockedcells:
                        for kk in range(9):
                            if self.grid[yidx][kk] == self.grid[yidx][i] and [kk,yidx] not in self.lockedcells:
                                self.incorrect_cells.append([kk,yidx])



    def checkColumnswhendone(self):
        for xidx in range(9):
            possiblesc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for yidx, row in enumerate(self.grid):
                if self.grid[yidx][xidx] in possiblesc:
                    possiblesc.remove(self.grid[yidx][xidx])
                    if [xidx, yidx] in self.incorrect_cells:
                        self.incorrect_cells.remove([xidx, yidx])
                else:
                    if [xidx, yidx] not in self.lockedcells:
                        self.incorrect_cells.append([xidx, yidx])
                    if [xidx, yidx] in self.lockedcells:
                        for k, row in enumerate(self.grid):
                            if self.grid[k][xidx] == self.grid[yidx][xidx] and [xidx, k] not in self.lockedcells:
                                self.incorrect_cells.append([xidx, k])

    def checksmallgridwhendone(self):
        for x in range(3):
            for y in range(3):
                possibless = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(3):
                    for j in range(3):
                        # print(x*3+i,y*3+j)
                        xidx = x * 3 + i
                        yidx = y * 3 + j
                        if self.grid[yidx][xidx] in possibless:
                            possibless.remove(self.grid[yidx][xidx])
                        else:
                            if [xidx, yidx] not in self.lockedcells and [xidx, yidx] not in self.incorrect_cells:
                                self.incorrect_cells.append([xidx, yidx])
                                # print("Wrong")
                                return False
                            if [xidx, yidx] in self.lockedcells:
                                for k in range(3):
                                    for ll in range(3):
                                        xidx2 = x * 3 + k
                                        yidx2 = y * 3 + k
                                        if self.grid[yidx2][xidx2] == self.grid[yidx][xidx] and [xidx2,yidx2] not in self.lockedcells:
                                            self.incorrect_cells.append([xidx2, yidx2])



    ###HELPING FUNCTIONS #####
    def drawnumbers(self,window):
        for yidx,row in enumerate(self.grid):
            for xidx,num in enumerate(row):
                if num != 0:
                    pos = [xidx*cellsize + gridpos[0],yidx * cellsize + gridpos[1]]
                    self.drawnumber(window,str(num),pos,YELLOW)
    def shadelocked(self,window,lockedcells,color):
        for cells in lockedcells:
            pygame.draw.rect(window,color,(cells[0]*cellsize + gridpos[0],cells[1]*cellsize + gridpos[1],cellsize,cellsize))
    def drawselect(self,window,pos):
        pygame.draw.rect(window,LIGHTBLUE,((pos[0] * cellsize) + gridpos[0],(pos[1] * cellsize) + gridpos[1],cellsize,cellsize))
    def Drawgrid(self,window):
        pygame.draw.rect(window,BLUE,(gridpos[0],gridpos[1],WIDTH-150,HEIGHT-150),2)
        for x in range(9):
            pygame.draw.line(window,BLUE,(gridpos[0] + (x*cellsize) , gridpos[1]),(gridpos[0] + (x*cellsize) , gridpos[1]+ 450),2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLUE, (gridpos[0] , gridpos[1] +  (x * cellsize)),(gridpos[0] + 450 , gridpos[1] + (x * cellsize)), 2 if x % 3 == 0 else 1)
    def mouseonboard(self):
        if self.mousepos[0] < gridpos[0] or self.mousepos[1] < gridpos[1]:
            return False
        if self.mousepos[0] > gridpos[0]+gridsize or self.mousepos[1] > gridpos[1]+gridsize:
            return False
        return  [(self.mousepos[0] - gridpos[0]) // cellsize,(self.mousepos[1]-gridpos[1]) // cellsize]
    def loadButtons(self):
        self.playingButtons.append(Buttono(window=self.window,x=20,y=40,width=100,height=40,color=(27,142,207),highlitedcolor=(255,55,0),para=False,function=self.quit,text="Quit",BUTTON_TEXT_COLOUR=(0,0,0),BUTTON_TEXT_SIZE=40))

    def quit(self):
        self.running = False

    def drawnumber(self,window,text,pos,color):
        font = self.font.render(text,False,color)
        font_width = font.get_width()
        font_height = font.get_height()
        pos[0] += (cellsize - font_width) // 2
        pos[1] += (cellsize - font_height) // 2
        window.blit(font,pos)
    def load(self):
        self.loadButtons()
        for yidx,row in enumerate(self.grid):
            for xidx,num in enumerate(row):
                if num != 0:
                    self.lockedcells.append([xidx,yidx])
    def displaytime(self,times):
        font = pygame.font.SysFont('arial', 50, bold=True)
        text = font.render(times, True, RED)
        text_size = text.get_size()
        self.window.blit(text,(450,10))

    def format_time(self,secs):
        sec = secs % 60
        minute = secs // 60
        hour = minute // 60

        mat = " " + str(minute) + ":" + str(sec)
        return mat






