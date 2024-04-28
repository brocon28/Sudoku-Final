import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.select = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        cell_size = 50
        x = self.col*cell_size
        y = self.row*cell_size

        color = (255, 255, 255)

        if self.select:
            color = (255, 0, 0)

        pygame.draw.rect(self.screen, color,
                         (x, y, cell_size, cell_size))
        if self.value != 0: #if set_cell_value != 0: --- is this self.value
            font = pygame.font.Font(None,36)
            text = font.render(str(self.value), True, (0, 0, 0))
            rect_text = text.get_rect(center=(x+cell_size//2, y+cell_size//2))
            self.screen.blit(text, rect_text)
        # elif self.value is not None:
        #     font = pygame.font.Font(None, 36)
        #     text = font.render(str(self.value), True, (0, 0, 0))
        #     rect_text = text.get_rect(center=(x+cell_size//2, y+cell_size//2))
        #     self.screen.blit(text, rect_text)


class Board:
    def __init__(self, width, height, screen, difficulty, game_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell = [[Cell(game_board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.cell_selected = None

    def draw(self):
        # make grid lines
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (i*50, 0), (i*50, 450), 3)
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, i*50), (450, i*50), 3)
            else:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (i * 50, 0), (i * 50, 450))
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, i * 50), (450, i * 50))
        # make cells
        for row in range(9):
            for col in range(9):
                self.cell[row][col].draw()

    def select(self, row, col):
        self.cell_selected = (row, col)
        self.cell[row][col].select = True
        return self.cell[row][col]


    def click(self, x, y):
        if 0 <= x <= 450 and 0 <= y <= 450:
            row = y//50
            col = x//50
            return row, col
        else:
            return None

    def clear(self):
        if self.cell_selected:
            row, col = self.cell_selected
            self.cell[row][col].set_cell_value(0)
            self.cell[row][col].set_sketched_value(None)

    def sketch(self, value):
        if self.cell_selected:
            row, col = self.cell_selected
            self.cell[row][col].set_sketched_value(value)

    def place_number(self, value):
        if self.cell_selected:
            row, col = self.cell_selected
            self.cell[row][col].set_cell_value(value)
            self.cell[row][col].select = False #deslect cell when done

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if self.cell[row][col].value == 0:
                    self.cell[row][col].set_sketched_value(None)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cell[row][col].value == 0:
                    return False
        return True #fix issue here, premature exiting

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.cell[row][col].draw()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cell[row][col].value == 0:
                    return row, col
                else:
                    return None

    def check_board(self):
        for x in range(9):
            if not self.valid_groups([self.cell[x][i].value for i in range(9)]) or \
                    not self.valid([self.cell[i][x].value for i in range(9)]):
                return False
        for z in range(0, 9, 3):
            if not self.valid_groups([self.cell][z][p] for p in range(9)) or \
                    not self.valid_groups([self.cell[p][z]for p in range(9)]):
                return False
        return True

    def valid_groups(self, kind):
        kind = [y for y in kind if y != 0]
        return len(set(kind)) == len(kind)

    def valid(self, row, col, num):
        if num in [self.cell[row][x].value for x in range(9)]:
            return False

        if num in [self.cell[y][col].value for y in range(9)]:
            return False

        row_start = (row//3)*3
        col_start = (col//3)*3
        if num in [self.cell[row_start+y][col_start+x].value for y in range(3) for x in range(3)]:
            return False

        return True
