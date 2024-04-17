from sudoku_generator import SudokuGenerator as SG
class Board:
    def __init__(self, width,height,screen,difficulty):
    def draw(self):
        pass

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
        total = 0
        for i in range (0, 9, 1):
            for j in range (0, 9, 1):
                if board[i][j] > 0:
                    total += 1
        if total == 81:
            return True
        else:
            return False

    def update_board(self):
        pass

    def find_empty(self):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if board[i][j] == 0:
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