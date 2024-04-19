import constants
import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen #maybe something else, not so sure yet?

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        self.value = value

    def draw(self):
        BLACK=(0,0,0)
        WHITE=(255,255,255)
        RED=(255,0,0)
        GREEN=(0,255,0)
        BLUE=(0,0,255)
        square_rect=pygame.Rect(100,100,200,200)
        pygame.draw.rect(self.screen, BLACK, square_rect,10)





