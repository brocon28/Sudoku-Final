import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(self.row_length**.5)
        self.board = [[0 for i in range(self.row_length)]
                      for x in range(self.row_length)]

    def get_board(self):
        return self.board

    def print_board(self):
        self.fill_values()
        #winning_board = self.get_board()
        self.remove_cells()
        board = self.get_board()
        for row in board:
            print(row)
        # for row in self.board:
            # print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start+i][col_start+j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and self.valid_in_col(col, num) and
                self.valid_in_box(row-row % self.box_length, col-col % self.box_length, num))

    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length+1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start+i][col_start+j] = nums.pop()

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
        while removable_cells > 0:
            row = random.randint(0, self.row_length-1)
            col = random.randint(0, self.row_length-1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removable_cells -= 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    winning_board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board