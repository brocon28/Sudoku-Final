import math, random
import pygame
import sys
from constants import *
from sudoku_generator import *
from board_cell import * #board and cell class are included in this file, we should seperate them so sudoku.py contains ui components and main loop

###Main program loop

def main():

    pygame.init() #create pygame instance
    screen=pygame.display.set_mode((WIDTH,HEIGHT)) #set window dimensions
    pygame.display.set_caption("Sudoku Final Project") #window title
    screen.fill(BG_COLOR) #window background based on constants file

    while True:
        #check for events through pygame
        #get events
            #check if a click
                #check if in menu
                #check if in game
            #check if closing game

        pygame.display.update() #update canvas

def start_menu_screen():
#this will render 3? buttons with the difficulty settings
#while loop to check for input
    #figure out how to add buttons and read when they are selected
#returns an int, corresponding to difficulty that main() then passes into draw_screen
    pass


def draw_screen(difficulty:int):
#this function will take in difficulty, which is an int that corresponds to the selected difficulty in the initial menu
#will then call the sudoku maker function with "difficulty" and render canvas with provided board
#while loop to check for user input and save guesses
    #check for when fully solved
    print(difficulty)
    pass

if __name__ == "__main__":
    main()

#I did not touch anything below here --- James

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells=removed_cells
        self.box_length = int(self.row_length**.5)
        self.board = [[0 for i in range(self.row_length)]for x in range(self.row_length)]

    def get_board(self):
        return self.board

    def print_board(self):
        self.fill_values()
        winning_board = self.get_board()
        self.remove_cells()
        board = self.get_board()
        for row in board:
            print(row)
        #for row in self.board:
            #print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]
    
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col]==num:
                return False
            else:
                return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start+i][col_start+j]==num:
                    return False
                else:
                    return True

    def is_valid(self, row, col, num):
        return(self.valid_in_row(row,num) and self.valid_in_col(col,num)and
               self.valid_in_box(row-row%self.box_length, col-col%self.box_length,num))

    def fill_box(self, row_start, col_start):
        nums=list(range(1,self.row_length+1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start+i][col_start+j]=nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        removable_cells = self.removed_cells
        while removable_cells>0:
            row = random.randint(0,self.row_length-1)
            col=random.randint(0,self.row_length-1)
            if self.board[row][col]!=0:
                self.board[row][col]=0
                removable_cells-=1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    winning_board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

#gen = SudokuGenerator(9,40)
#gen.print_board()
#print(generate_sudoku(9,40))

class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen

    def set_cell_value(self,value):
        self.value=value

    def set_sketched_value(self,value):
        self.value=value

    def draw(self):
        cell_size = 50
        x = self.col*cell_size
        y = self.col*cell_size

        pygame.draw.rect(self.screen,(255,255,255),(x,y,cell_size,cell_size))
        if set_cell_value!=0:
            text = self.font.render(str(self.value),True,(0,0,0))
            rect_text = text.get_rect(center = (x+cell_size//2,y+cell_size//2))
            self.screen.blit(text,rect_text)
        elif self.sketch_value is not None:
            text = self.font.render(str(self.sketch_value),True,(128,128,128))
            rect_text = text.get_rect(center=(x+cell_size//2,y+cell_size//2))
            self.screen.blit(text,rect_text)

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty

    def draw(self):
    # make grid lines
    for i in range(10):
        if i%3==0:
            pygame.draw.line(self.screen,(0,0,0),(i*50,0),(i*50,450),3)
            pygame.draw.line(self.screen,(0,0,0),(0,i*50),(450,i*50),3)
        else:
            pygame.draw.line(self.screen, (0, 0, 0), (i * 50, 0), (i * 50, 450))
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 50), (450, i * 50))
    #make cells
    for row in range(9):
        for col in range(9):
            self.cell[row][col].draw()

    def select(self,row,col):
        self.cell_selected = (row,col)

    def click(self,x,y):
        if 0 <=x<=450 and 0<=y<=450:
            row=y//50
            col=x//50
            return row,col
        else:
            return None

    def clear(self):
        if self.cell_selected:
            row,col=self.cell_selected
            self.cell[row][col].set_cell_value(0)
            self.cell[row][col].set_sketched_value(None)

    def sketch(self,value):
        if self.cell_selected:
            row,col=self.cell_selected
            self.cell[row][col].set_sketched_value(value)

    def place_number(self,value):
        if self.cell_selected:
            row,col=self.cell_selected
            self.cell[row][col].set_cell_value(value)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if self.cell[row][col].value==0:
                    self.cell[row][col].set_sketched_value(None)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cell[row][col].value==0:
                    return False
                else:
                    return True

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.cell[row][col].draw()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cell[row][col].value==0:
                    return row,col
                else:
                    return None

    def check_board(self):
        for x in range(9):
            if not self.valid_groups([self.cell[x][i].value for i in range(9)]) or \
                not self.valid([self.cell[i][x].value for i in range(9)]):
                return False
        for z in range(0,9,3):
            if not self.valid_groups([self.cell][z][p] for p in range(9)) or \
                not self.valid_groups([self.cell[p][z]for p in range(9)]):
                return False
        return True

    def valid_groups(self,kind):
        kind = [y for y in group if y!=0]
        return len(set(kind)==len(kind))

    def valid(self,row,col,num):
        if num in [self.cell[row][x].value for x in range(9)]:
            return False

        if num in [self.cell[y][col].value for y in range(9)]:
            return False

        row_start = (row//3)*3
        col_start = (col//3)*3
        if num in [self.cell[row_start+y][col_start+x].value for y in range(3) for x in range(3)]:
            return False

        return True
