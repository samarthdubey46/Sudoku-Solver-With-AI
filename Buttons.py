import pygame
from  settings import *
class Buttono:
    def __init__(self,window,x,y,width,height,color=(73,73,73),highlitedcolor=(183,183,183),function=None,para=False,text=None,BUTTON_TEXT_SIZE=None,BUTTON_TEXT_COLOUR=None):
        self.image = pygame.Surface((width,height))
        self.pos = (x,y)
        self.rect = self.image.get_rect()
        self.topleft = self.pos
        self.text = text
        self.color = color
        self.highcolor = highlitedcolor
        self.function = function
        self.para = para
        self.highlited = False
        self.width =width
        self.height = height
        self.x = x
        self.y = y
        self.clicked = False
        self.window = window
        self.BUTTON_TEXT_COLOUR = BUTTON_TEXT_COLOUR
        self.font = pygame.font.SysFont('arial', BUTTON_TEXT_SIZE, bold=True)
        # (20, 40) top Left Button
        # (103, 47) top Right
        # (116, 73) Bottom Right
        # (21, 79) Bottom Left



    def update(self,mouse):
        if self.rect.collidepoint(mouse):
            self.highlited = True
        else:
            self.highlited = False
    def draw(self,window):
        if self.highlited:
            self.image.fill(self.highcolor)
        else:
            self.image.fill(self.color)
        window.blit(self.image,self.pos)
    def show_text(self):
        if self.text != None:
            text = self.font.render(self.text, True, self.BUTTON_TEXT_COLOUR)
            text_size = text.get_size()
            text_x = self.x+(self.width/2)-(text_size[0]/2)
            text_y = self.y+(self.height/2)-(text_size[1]/2)
            self.window.blit(text, (text_x, text_y))
    def click(self):
        # (20, 40) top Left Button
        # (103, 47) top Right
        # (116, 73) Bottom Right
        # (21, 79) Bottom Left
        # if
        # if self.para:
        #     self.functions(self.para)
        # else:
        #     self.functions()
        pass
    def functions(self,paras=None):
        pass

