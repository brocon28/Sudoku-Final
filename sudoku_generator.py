import math
import random
import pygame

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[" " for _ in range(self.row_length)] for _ in range(self.row_length)]
        self.box_length = int(math.sqrt(self.row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.get_board():
            for col in row:
                print(col,end=" ")
            print()

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(self.box_length):
            for col in range(self.box_length):
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num)

    # def unused_in_box(self, row_start, col_start, num):
    #     for row in range(row_start, row_start + 3):
    #         for col in range(col_start, col_start + 3):
    #             if self.board[row][col] == num:
    #                 return False
    #     return True

    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start + i][col_start + j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
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
        self.fill_remaining(0,3)

    def remove_cells(self):
        for i in range(self.removed_cells):
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            while self.board[row][col] == 0:
                row = random.randint(0, self.row_length - 1)
                col = random.randint(0, self.row_length - 1)
            self.board[row][col] = 0

# class Cell:
#     # Constructor for this class
#     def __int__(self, value, row, col, screen):
#         self.value = value
#         self.row = row
#         self.col = col
#         self.screen = screen
#
#     # Setter for this cell's value
#     def set_cell_value(self, value):
#         pass
#
#     # Setter for this cell's sketched value
#     def set_sketched_value(self, value):
#         pass
#
#     # Draws this cell, along with the value inside it.
#     # If this cell has a nonzero value, that value is displayed.
#     # Otherwise, no value is displayed in the cell.
#     # The cell is outlined red if it is currently selected
#     def draw(self):
#         pass

class Board():

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.row, self.col = 9,9
        self.color = (0,0,0)
        self.board = generate_sudoku(9,difficulty)
        self.margin = 1

    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes
    # Draws every cell on this board.
    def draw(self):
        for rows in range(self.row):
            for cols in range(self.col):

                if str(self.board[rows][cols]) != "0":
                    x = pygame.draw.rect(self.screen, self.color, [(self.margin + self.width) * cols + self.margin,(self.margin + self.height) * rows + self.margin,self.width, self.height], 1)
                    font = pygame.font.Font(None, 25)

                    cell_text = font.render(str(self.board[rows][cols]), True, self.color)
                    x_rect = cell_text.get_rect(center=x.center)
                    self.screen.blit(cell_text, x_rect)
                else:
                    x = pygame.draw.rect(self.screen, self.color, [(self.margin + self.width) * cols + self.margin, (self.margin + self.height) * rows + self.margin, self.width, self.height], 1)
                    font = pygame.font.Font(None, 25)

                    cell_text = font.render("", True, self.color)
                    x_rect = cell_text.get_rect(center=x.center)
                    self.screen.blit(cell_text, x_rect)

        pygame.draw.line(self.screen, self.color, [0, 122], [457, 122], 2)
        pygame.draw.line(self.screen, self.color, [0, 246], [457, 246], 2)
        pygame.draw.line(self.screen, self.color, [0, 368], [457, 368], 2)

        pygame.draw.line(self.screen, self.color, [153, 0], [153, 368], 2)
        pygame.draw.line(self.screen, self.color, [305, 0], [305, 368], 2)


    def board_solution(self):
        return

    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.
    def select(self, row, col):
        pass

    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.
    def click(self, x, y):
        pass

    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.
    def clear(self):
        pass

    # Sets the sketched value of the current selected cell equal to user entered value.
    # It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        pass

    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value):
        pass

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        pass

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        pass

    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        pass

    # Finds an empty cell and returns its row and col as a tuple (x, y).
    def find_empty(self):
        pass

    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        pass

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    sudoku.print_board()
    return board