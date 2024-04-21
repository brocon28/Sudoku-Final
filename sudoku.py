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
LINE_COLOR = (0, 0, 0)
CHIP_COLOR = (171, 176, 172)
FIXED_CHIP_COLOR = (0, 0, 0)


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

def draw_menu(screen):
    start_title_font = pygame.font.Font(None, 70)
    select_title_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 40)

    screen.fill(BG_COLOR)

    title_surf = start_title_font.render("Welcome to Sudoku", 1, LINE_COLOR)
    title_rect = title_surf.get_rect(center=(WIDTH//2, HEIGHT//2-150))
    screen.blit(title_surf, title_rect)

    select_title_surf = select_title_font.render("Select Game Mode:", 1, LINE_COLOR)
    select_title_rect = select_title_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(select_title_surf, select_title_rect)


    easy=button_font.render("Easy",0,(255,255,255))
    med=button_font.render("Medium",0,(255,255,255))
    hard=button_font.render("Hard",0,(255,255,255))

    easy_surf=pygame.Surface((easy.get_size()[0]+20,easy.get_size()[1]+20))
    easy_surf.fill(LINE_COLOR)
    easy_surf.blit(easy,(10,10))
    med_surf = pygame.Surface((med.get_size()[0] + 20, med.get_size()[1] + 20))
    med_surf.fill(LINE_COLOR)
    med_surf.blit(med, (10, 10))
    hard_surf = pygame.Surface((hard.get_size()[0] + 20, hard.get_size()[1] + 20))
    hard_surf.fill(LINE_COLOR)
    hard_surf.blit(hard, (10, 10))


    easy_rect=easy.get_rect(center=(WIDTH//2-120,HEIGHT//2+100))
    med_rect=med.get_rect(center=(WIDTH//2,HEIGHT//2+100))
    hard_rect=hard.get_rect(center=(WIDTH//2+120,HEIGHT//2+100))

    screen.blit(easy_surf,easy_rect)
    screen.blit(med_surf, med_rect)
    screen.blit(hard_surf, hard_rect)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    return 'easy'
                elif med_rect.collidepoint(event.pos):
                    return 'medium'
                elif hard_rect.collidepoint(event.pos):
                    return 'hard'
        pygame.display.update()

def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if win:
        text="Game Won!"
    else:
        text = "Game Over :("
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    if win:
        exit_text=button_font.render("EXIT",0,(255,255,255))
        exit_surf=pygame.Surface((exit_text.get_size()[0]+20,exit_text.get_size()[1]+20))
        exit_surf.fill(LINE_COLOR)
        exit_surf.blit(exit_text,(10,10))
        exit_rect=exit_surf.get_rect(center=(WIDTH//2+135,570))
        screen.blit(exit_surf,exit_rect)

    else:
        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surf.fill(LINE_COLOR)
        restart_surf.blit(restart_text, (10, 10))
        restart_rect = restart_surf.get_rect(center=(WIDTH//2, 570))
        screen.blit(restart_surf, restart_rect)

