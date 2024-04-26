import random, pygame, sys
from sudoku_generator import SudokuGenerator

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

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = value
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        if value != 0:
            self.sketched_value = value

    def draw(self):
        chip_font = pygame.font.Font(None, 60)
        chip_surf = chip_font.render(str(self.value), 1, LINE_COLOR) if self.value != 0 else None

        chip_1_surf = chip_font.render('1', 1, LINE_COLOR)
        chip_2_surf = chip_font.render('2', 1, LINE_COLOR)
        chip_3_surf = chip_font.render('3', 1, LINE_COLOR)
        chip_4_surf = chip_font.render('4', 1, LINE_COLOR)
        chip_5_surf = chip_font.render('5', 1, LINE_COLOR)
        chip_6_surf = chip_font.render('6', 1, LINE_COLOR)
        chip_7_surf = chip_font.render('7', 1, LINE_COLOR)
        chip_8_surf = chip_font.render('8', 1, LINE_COLOR)
        chip_9_surf = chip_font.render('9', 1, LINE_COLOR)

        if self.sketched_value != 0 and self.value == 0:
            chip_surf = chip_font.render(str(self.sketched_value), 1, LINE_COLOR)

        if self.selected:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE,
                                                           SQUARE_SIZE, SQUARE_SIZE), 3)

        if chip_surf:
            chip_rect = chip_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                   self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_surf, chip_rect)

        if self.selected:
            pygame.draw.rect(screen, RED,
                             pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
            self.selected = False

        if self.value == 1:
            chip_1_rect = chip_1_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_1_surf, chip_1_rect)

        elif self.value == 2:
            chip_2_rect = chip_2_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_2_surf, chip_2_rect)

        elif self.value == 3:
            chip_3_rect = chip_3_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_3_surf, chip_3_rect)

        elif self.value == 4:
            chip_4_rect = chip_4_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_4_surf, chip_4_rect)

        elif self.value == 5:
            chip_5_rect = chip_5_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_5_surf, chip_5_rect)

        elif self.value == 6:
            chip_6_rect = chip_6_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_6_surf, chip_6_rect)

        elif self.value == 7:
            chip_7_rect = chip_7_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_7_surf, chip_7_rect)

        elif self.value == 8:
            chip_8_rect = chip_8_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_8_surf, chip_8_rect)

        elif self.value == 9:
            chip_9_rect = chip_9_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3))
            self.screen.blit(chip_9_surf, chip_9_rect)


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(self.difficulty, 9)
        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.selected_row = 0
        self.selected_col = 0

    def draw(self):
        self.screen.fill(BG_COLOR)
        button_font = pygame.font.Font(None, 35)

        for i in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE * 3), (WIDTH, i * SQUARE_SIZE * 3),
                             LINE_WIDTH * 3)

        for i in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - SQUARE_SIZE),
                             LINE_WIDTH)
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE * 3, 0),
                             (i * SQUARE_SIZE * 3, HEIGHT - SQUARE_SIZE),
                             LINE_WIDTH * 3)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.board[i][j])
                self.cells[i][j].draw()

        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surf.fill(LINE_COLOR)
        exit_surf.blit(exit_text, (10, 10))
        exit_rect = exit_surf.get_rect(center=(WIDTH // 2 + 135, 570))
        screen.blit(exit_surf, exit_rect)

        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surf.fill(LINE_COLOR)
        restart_surf.blit(restart_text, (10, 10))
        restart_rect = restart_surf.get_rect(center=(WIDTH // 2, 570))
        screen.blit(restart_surf, restart_rect)

        reset_text = button_font.render("RESET", 0, (255, 255, 255))
        reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surf.fill(LINE_COLOR)
        reset_surf.blit(reset_text, (10, 10))
        reset_rect = reset_surf.get_rect(center=(WIDTH // 2 - 140, 570))
        screen.blit(reset_surf, reset_rect)

    def update_display(self):
        pygame.display.update()

    def select(self, row, col):
        self.cells[self.selected_row][self.selected_col].selected = True

        if row in range(9) and col in range(9):
            self.row = row
            self.col = col
        self.cells[self.selected_row][self.selected_col].selected = True

    def click(self, x, y):
        cell_width = self.width // 9
        cell_height = self.height // 9
        click_row = x // cell_width
        click_col = y // cell_height
        position = (click_row, click_col)
        return position

    def clear(self):
        if not empty[clicked_row][clicked_col]:
            board.board[clicked_row][clicked_col] = 0

    def find_preset_values(self, sudoku_board):
        dict = []
        for row in range(9):
            rowdict = {}
            for i, val in enumerate(sudoku_board[row]):
                rowdict[i] = val
                if val == 0:
                    rowdict[str(i)] = False
                else:
                    rowdict[str(i)] = True
            dict.append(rowdict)
        return dict

    def sketch(self, value):
        self.sketch = value

    def place_number(self, value):
        self.number = value

    def reset_to_original(self):
        for i, dict in enumerate(self.find_preset_values()):
            for col in range(9):
                if dict[str(col)] == True:
                    dict[col] = 0

    def is_full(self):
        count = 0
        for row, dict in enumerate(self.find_preset_values(self.board)):
            for col in range(9):
                if dict[col] == 0:
                    count += 1
        if count == 0:
            return True
        else:
            return False

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def check_board(self):
        for row in range(9):
            for col in range(9):
                if not self.is_valid(row, col):
                    return False
        return True

    def is_valid(self, row, col):

        test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        for row in range(9):
            set1 = set(self.board[row])
            if set1 != test_set:
                return False

        for col in range(9):
            col_list = []
            for row in range(9):
                col_list.append(self.board[row][col])
            set2 = set(col_list)
            if set2 != test_set:
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = [self.board[row][col], self.board[row][col + 1], self.board[row][col + 2],
                       self.board[row + 1][col], self.board[row + 1][col + 1], self.board[row + 1][col + 2],
                       self.board[row + 2][col], self.board[row + 2][col + 1], self.board[row + 2][col + 2]]
                set3 = set(box)
                if set3 != test_set:
                    return False
        return True


def draw_menu(screen):
    start_title_font = pygame.font.Font(None, 70)
    select_title_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 40)

    screen.fill(BG_COLOR)

    title_surf = start_title_font.render("Welcome to Sudoku", 1, LINE_COLOR)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surf, title_rect)

    select_title_surf = select_title_font.render("Select Game Mode:", 1, LINE_COLOR)
    select_title_rect = select_title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(select_title_surf, select_title_rect)

    easy = button_font.render("Easy", 0, (255, 255, 255))
    med = button_font.render("Medium", 0, (255, 255, 255))
    hard = button_font.render("Hard", 0, (255, 255, 255))

    easy_surf = pygame.Surface((easy.get_size()[0] + 20, easy.get_size()[1] + 20))
    easy_surf.fill(LINE_COLOR)
    easy_surf.blit(easy, (10, 10))
    med_surf = pygame.Surface((med.get_size()[0] + 20, med.get_size()[1] + 20))
    med_surf.fill(LINE_COLOR)
    med_surf.blit(med, (10, 10))
    hard_surf = pygame.Surface((hard.get_size()[0] + 20, hard.get_size()[1] + 20))
    hard_surf.fill(LINE_COLOR)
    hard_surf.blit(hard, (10, 10))

    easy_rect = easy.get_rect(center=(WIDTH // 2 - 120, HEIGHT // 2 + 100))
    med_rect = med.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    hard_rect = hard.get_rect(center=(WIDTH // 2 + 120, HEIGHT // 2 + 100))

    screen.blit(easy_surf, easy_rect)
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
        text = "Game Won!"
    else:
        text = "Game Over :("
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    if win:
        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surf.fill(LINE_COLOR)
        exit_surf.blit(exit_text, (10, 10))
        exit_rect = exit_surf.get_rect(center=(WIDTH // 2 + 135, 570))
        screen.blit(exit_surf, exit_rect)

    else:
        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surf.fill(LINE_COLOR)
        restart_surf.blit(restart_text, (10, 10))
        restart_rect = restart_surf.get_rect(center=(WIDTH // 2, 570))
        screen.blit(restart_surf, restart_rect)


if __name__ == '__main__':
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    game_over = False
    win = False

    pygame.init()
    pygame.display.set_caption('Sudoku')

    chip_font = pygame.font.Font(None, 35)
    chip_1_surf_1 = chip_font.render('1', 1, GRAY)
    chip_2_surf_1 = chip_font.render('2', 1, GRAY)
    chip_3_surf_1 = chip_font.render('3', 1, GRAY)
    chip_4_surf_1 = chip_font.render('4', 1, GRAY)
    chip_5_surf_1 = chip_font.render('5', 1, GRAY)
    chip_6_surf_1 = chip_font.render('6', 1, GRAY)
    chip_7_surf_1 = chip_font.render('7', 1, GRAY)
    chip_8_surf_1 = chip_font.render('8', 1, GRAY)
    chip_9_surf_1 = chip_font.render('9', 1, GRAY)

    option = draw_menu(screen)
    if option == "easy":
        difficulty = 30
    elif option == 'medium':
        difficulty = 40
    elif option == 'hard':
        difficulty = 50

    board = Board(WIDTH, HEIGHT, screen, difficulty)
    board.draw()
    empty = board.find_preset_values(board.board)
    board.update_display()

    clicked_row = 0
    clicked_col = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    clicked_col = (clicked_col - 1) % 9
                    i = 0
                elif event.key == pygame.K_RIGHT:
                    clicked_col = (clicked_col + 1) % 9
                    i = 0
                elif event.key == pygame.K_UP:
                    clicked_row = (clicked_row - 1) % 9
                    i = 0
                elif event.key == pygame.K_DOWN:
                    clicked_row = (clicked_row + 1) % 9
                    i = 0

                if 0 <= clicked_row <= 8 and 0 <= clicked_col <= 8:
                    board.cells[clicked_row][clicked_col].selected = True
                    board.draw()

            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                clicked_row = int(event.pos[1] / SQUARE_SIZE)
                clicked_col = int(event.pos[0] / SQUARE_SIZE)
                i = 0
                if clicked_row == 9 and 1 <= clicked_col <= 2:
                    for i in range(9):
                        for j in range(9):
                            if not empty[i][j]:
                                board.board[i][j] = 0
                    board.draw()

                if clicked_row == 9 and 3 <= clicked_col <= 5:
                    option = draw_menu(screen)
                    if option == "easy":
                        difficulty = 30
                    elif option == 'medium':
                        difficulty = 40
                    elif option == 'hard':
                        difficulty = 50

                    board = Board(WIDTH, HEIGHT, screen, difficulty)
                    board.draw()
                    empty = board.find_preset_values(board.board)
                    board.update_display()

                if clicked_row == 9 and 6 <= clicked_col <= 7:
                    sys.exit()

                if 0 <= clicked_row <= 8 and 0 <= clicked_col <= 8:
                    board.cells[clicked_row][clicked_col].selected = True
                    board.draw()
                board.update_display()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    i = 1
                    chip_1_rect = chip_1_surf_1.get_rect(center=(clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                                                                 clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_1_surf_1, chip_1_rect)
                    pygame.display.update()

                elif event.key == pygame.K_2:
                    i = 2
                    chip_2_rect = chip_2_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_2_surf_1, chip_2_rect)
                    pygame.display.update()

                elif event.key == pygame.K_3:
                    i = 3
                    chip_3_rect = chip_3_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_3_surf_1, chip_3_rect)
                    pygame.display.update()

                elif event.key == pygame.K_4:
                    i = 4
                    chip_4_rect = chip_4_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_4_surf_1, chip_4_rect)
                    pygame.display.update()

                elif event.key == pygame.K_5:
                    i = 5
                    chip_5_rect = chip_5_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_5_surf_1, chip_5_rect)
                    pygame.display.update()

                elif event.key == pygame.K_5:
                    i = 5
                    chip_5_rect = chip_5_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_5_surf_1, chip_5_rect)
                    pygame.display.update()

                elif event.key == pygame.K_6:
                    i = 6
                    chip_6_rect = chip_6_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_6_surf_1, chip_6_rect)
                    pygame.display.update()

                elif event.key == pygame.K_7:
                    i = 7
                    chip_7_rect = chip_7_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_7_surf_1, chip_7_rect)
                    pygame.display.update()

                elif event.key == pygame.K_8:
                    i = 8
                    chip_8_rect = chip_8_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_8_surf_1, chip_8_rect)
                    pygame.display.update()

                elif event.key == pygame.K_9:
                    i = 9
                    chip_9_rect = chip_9_surf_1.get_rect(center=(
                        clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10,
                        clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2 + 3 - 10))
                    screen.blit(chip_9_surf_1, chip_9_rect)
                    pygame.display.update()

                elif event.key == pygame.K_BACKSPACE:
                    board.clear()
                    board.draw()
                    board.update_display()

                elif event.key == pygame.K_RETURN:
                    digit = i
                    if 0 <= clicked_row <= 8 and 0 <= clicked_col <= 8:
                        if not empty[clicked_row][str(clicked_col)]:
                            board.board[clicked_row][clicked_col] = digit
                            board.draw()
                        i = 0

                board.update_display()

                if board.is_full():
                    if board.check_board():
                        win = True
                        draw_game_over(screen)
                        pygame.display.update()
                    else:
                        draw_game_over(screen)
                        pygame.display.update()

