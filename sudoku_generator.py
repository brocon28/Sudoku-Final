import math
import random
import pygame

empty_locations = []
puzzle_solution = []

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

class Cell:
    # Constructor for this class
    def __init__(self, value, row, col, screen, board, count):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.board = board
        self.color = (0,0,0)
        self.margin = 1
        self.width = 50
        self.height = 40
        self.count = count
        self.can_edit = False

    def data(self):
        return (self.row, self.col, self.width, self.height)

    def draw(self):
        global empty_locations

        if self.count <= 1:
            if self.value != "0":
                z = pygame.draw.rect(self.screen, self.color, [(self.margin + self.width) * self.col + self.margin,
                                                               (self.margin + self.height) * self.row + self.margin,
                                                               self.width, self.height], 1)
                font = pygame.font.Font(None, 25)

                cell_text = font.render(str(self.board[self.row][self.col]), True, self.color)
                z_rect = cell_text.get_rect(center=z.center)
                self.screen.blit(cell_text, z_rect)

                self.can_edit = False
            else:
                z = pygame.draw.rect(self.screen, self.color, [(self.margin + self.width) * self.col + self.margin,
                                                               (self.margin + self.height) * self.row + self.margin,
                                                               self.width, self.height], 1)
                font = pygame.font.Font(None, 25)

                cell_text = font.render("", True, self.color)
                z_rect = cell_text.get_rect(center=z.center)
                self.screen.blit(cell_text, z_rect)

                self.can_edit = True

            empty_locations.append((z.x, z.y, z.width, z.height))
            empty_locations.append((self.row, self.col, self.can_edit))
        else:
            if self.value != "0":
                z = pygame.draw.rect(self.screen, self.color, [(self.margin + self.width) * self.col + self.margin,
                                                               (self.margin + self.height) * self.row + self.margin,
                                                               self.width, self.height], 1)
                font = pygame.font.Font(None, 25)

                cell_text = font.render(str(self.board[self.row][self.col]), True, self.color)
                z_rect = cell_text.get_rect(center=z.center)
                self.screen.blit(cell_text, z_rect)

                self.can_edit = False
            else:
                z = pygame.draw.rect(self.screen, self.color, [(self.margin + self.width) * self.col + self.margin,
                                                               (self.margin + self.height) * self.row + self.margin,
                                                               self.width, self.height], 1)
                font = pygame.font.Font(None, 25)

                cell_text = font.render("", True, self.color)
                z_rect = cell_text.get_rect(center=z.center)
                self.screen.blit(cell_text, z_rect)

                self.can_edit = True

class Board:
    def __init__(self, screen, board):
        self.screen = screen
        self.difficulty = board
        self.row, self.col = 9,9
        self.color = (0,0,0)
        self.board = board
        self.margin = 1
        self.count = 0

    def draw(self):
        self.count += 1

        for rows in range(self.row):
            for cols in range(self.col):

                indiv_cell = Cell(str(self.board[rows][cols]), rows, cols, self.screen, self.board, self.count)

                indiv_cell.draw()

        pygame.draw.line(self.screen, self.color, [0, 122], [457, 122], 2)
        pygame.draw.line(self.screen, self.color, [0, 246], [457, 246], 2)
        pygame.draw.line(self.screen, self.color, [0, 368], [457, 368], 2)

        pygame.draw.line(self.screen, self.color, [153, 0], [153, 368], 2)
        pygame.draw.line(self.screen, self.color, [305, 0], [305, 368], 2)

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
    return board