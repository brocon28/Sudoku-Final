import pygame,sys
from constants import *




class Board:

    def __init__(self, width,height,screen,difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
    def draw(self):
        for i in range (1, BOARD_ROWS):
            pygame.draw.line(self.screen,LINE_COLOR,(0,i*SQUARE_SIZE),(WIDTH,i*SQUARE_SIZE),LINE_WIDTH)
        for i in range (1, BOARD_COLS):
            pygame.draw.line(self.screen,LINE_COLOR,(i*SQUARE_SIZE,0),(i*SQUARE_SIZE,HEIGHT),LINE_WIDTH)

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass