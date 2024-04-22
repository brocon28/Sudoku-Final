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
        if set_cell_value==0:
            self.value=''
        # if cell has non-zero value display it
        #otherwise no value displayed
        # outline cell red if currently selected

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty

    def draw(self):
        #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        #Draws every cell on this board.
        pass

    def select(self,row,col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        pass

    def click(self,x,y):
        #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.
        pass

    def clear(self):
        # clears the value cell. note the user can only remove the cell values
        # and sketched values that are filled by themselves
        pass

    def sketch(self,value):
        #Sets the sketched value of the current selected cell equal to user entered value.
        #It will be displayed at the top left corner of the cell using the draw() function
        pass

    def place_number(self,value):
        #Sets the value of the current selected cell equal to user entered value.
        #Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        #Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        pass

    def is_full(self):
        #Returns a Boolean value indicating whether the board is full or not.
        pass

    def update_board(self):
        #Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        pass

    def check_board(self):
        #Check whether the Sudoku board is solved correctly.
        pass
