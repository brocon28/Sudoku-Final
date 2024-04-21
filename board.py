from sudoku_generator import SudokuGenerator as SG
from constants import *
import pygame
import cell
class Board:
    def __init__(self, width,height,screen,difficulty):
        self.width = width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.cells=[]


    def draw(self):
        for i in range (1,BOARD_ROWS):#big horizontal lines
            pygame.draw.line(self.screen,BLACK,(0,i*SQUARE_SIZE),(WIDTH,i*SQUARE_SIZE),10)
        for i in range(1,9):#little horizontal lines
            pygame.draw.line(self.screen,BLACK,(0,i*200/3),(WIDTH,i*200/3),5)
        for i in range(1,9):#little vertical lines
            pygame.draw.line(self.screen,BLACK,(i*200/3,0),(i*200/3,HEIGHT),5)
        for i in range (1,BOARD_COLS):#big vertical lines
            pygame.draw.line(self.screen,BLACK,(i*SQUARE_SIZE,0),(i*SQUARE_SIZE,HEIGHT),10)






    def select(self, row, col):
        for i in self.cells:
            for j in i:
                if j.row==row and j.col==col:
                    j.touch==True
                    return j

    def click(self, x, y):
        row = x//SQUARE_SIZE
        col = y//SQUARE_SIZE
        return row, col

    def clear(self):
        pass
    #we might not need this (logically)

    def sketch(self, value):
        pass
    #do later

    def place_number(self, value):
        pass
    #do later

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j]=self.original[i][j](self.cells[i][j]).value = self.board[i][j]
                self.update.board()
                self.draw()

    def is_full(self):
        total = 0
        for i in range (0, 9, 1):
            for j in range (0, 9, 1):
                if SG.print_board()[i][j] > 0:
                    total += 1
        if total == 81:
            return True
        else:
            return False

    def update_board(self):
        for i in self.cells:
            for j in i:
                self.board[j.row][j.col] = j.value
    def find_empty(self):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if SG.print_board()[i][j] == 0:
                    print(str(i)+", "+str(j))


    def check_board(self):
        total=0
        for i in range (0, 9, 1):
            if SG.valid_in_row(i) is True and SG.valid_in_col(i) is True:
                total += 1
        if total == 9:
            return True
        else:
            return False
        #think this needs to pull the valid functions from sudoku_generator
