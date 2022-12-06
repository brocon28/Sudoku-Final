import pygame
from constants import *
from sudoku_generator import SudokuGenerator

class Cell():
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.tempnum = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.space = self.width / 9
        self.clicked = False

        self.gap = self.width / 9
        self.pos_x = self.col * self.gap
        self.pos_y = self.row * self.gap

    def set_cell_value(self, value):
        self.value = cell_value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self, screen):
        # Checks if the cell already has a number already on the board
        if self.value != 0:
            num = FONT.render(str(self.value), 1, (0, 0, 0))
            screen.blit(num, (self.pos_x + (self.gap/2 - num.get_width()/2), self.pos_y + (self.gap/2 - num.get_height()/2)))

        # Checks if the cell is empty but has a temporary number which is in light grey
        elif self.value == 0 and self.tempnum != 0:
            num = FONT.render(str(self.tempnum), 1, (128, 128, 128))
            screen.blit(num, (self.pos_x+5, self.pos_y+5))

        if self.clicked == True:
            pygame.draw.rect(screen, (255, 0, 0), (self.pos_x, self.pos_y, self.gap, self.gap), 3)





