import random, pygame, sys

WIDTH = 540
HEIGHT = 600
LINE_WIDTH = 2
BOARD_ROWS = 10
BOARD_COLS = 9
SQUARE_SIZE = 60
RED = (255, 0, 0)
GRAY = (168, 168, 168)
BG_COLOR = (255, 255, 245)
BG_COLOR_1 = (0,255,0)
LINE_COLOR = (0, 0, 0)
CHIP_COLOR = (171, 176, 172)
FIXED_CHIP_COLOR = (0, 0, 0)

i = 0

class SudokuGenerator:

    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = 3
        self.board = [[" " for _ in range(self.row_length)] for _ in range(self.row_length)]

    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(3):
            for col in range(3):
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3,
                                                                                                 col - col % 3, num)

    def unused_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

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
        self.fill_remaining(0, 3)

    def remove_cells(self):
        for i in range(self.removed_cells):
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            while self.board[row][col] == 0:
                row = random.randint(0, self.row_length - 1)
                col = random.randint(0, self.row_length - 1)
            self.board[row][col] = 0


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board