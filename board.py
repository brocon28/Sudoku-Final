from sudoku_generator import *
from sudoku_generator import SudokuGenerator as SG
from constants import *
import pygame
from cell import Cell
import cell
class Board:
    def __init__(self, width,height,screen,difficulty):
        self.width = width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.board = generate_sudoku(9,difficulty)
        self.cells=[
            [Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)
        ]


    def draw(self,screen):

#This is the thicker lines dividing the 9x9 rows and columns for the 81x81 board
        for i in range (1,BOARD_ROWS):
            pygame.draw.line(self.screen,LINE_COLOR,(0,i*SQUARE_SIZE),(WIDTH,i*SQUARE_SIZE),LINE_WIDTH//3)
        for i in range (1,BOARD_COLS):
            pygame.draw.line(self.screen,LINE_COLOR,(i*SQUARE_SIZE,0),(i*SQUARE_SIZE,HEIGHT-100),LINE_WIDTH//3)

        pygame.draw.line(self.screen,LINE_COLOR,(0,HEIGHT-100),(WIDTH,HEIGHT-100),LINE_WIDTH//3)

#This is the thinner lines dividing the cells in the 9x9 bigger cells

        for i in range(1,10):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE//3), (WIDTH, i * SQUARE_SIZE//3), LINE_WIDTH // 6)
        for i in range(1, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE//3, 0), (i * SQUARE_SIZE//3, HEIGHT - 100),
                         LINE_WIDTH // 6)

            reset_font = pygame.font.Font(None, 32)
            reset_button = reset_font.render("Reset", True, BLACK)
            reset_surface = pygame.Surface((reset_button.get_size()[0] + 20, reset_button.get_size()[1] + 20))
            reset_surface.fill(EASY_COLOR)
            reset_surface.blit(reset_button, (10, 10))
            reset_rect = reset_button.get_rect(center=(WIDTH // 4, HEIGHT * 2.55 // 2.8))
            screen.blit(reset_surface, reset_rect)

            restart_font = pygame.font.Font(None, 32)
            restart_button = restart_font.render("Restart", True, BLACK)
            restart_surface = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
            restart_surface.fill(EASY_COLOR)
            restart_surface.blit(restart_button, (10, 10))
            restart_rect = restart_button.get_rect(center=(WIDTH // 2, HEIGHT * 2.55 // 2.8))
            screen.blit(restart_surface, restart_rect)

            exit_button = reset_font.render("Exit", True, BLACK)
            exit_surface = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
            exit_surface.fill(EASY_COLOR)
            exit_surface.blit(exit_button, (10, 10))
            exit_rect = exit_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 2.55 // 2.8))
            screen.blit(exit_surface, exit_rect)

        for i in self.cells:
            for j in i:
                j.draw(self.screen)

        return reset_rect, restart_rect, exit_rect



    def select(self, row, col):
            for i in self.cells:
                for j in i:
                    if j.row == row and j.column == col:
                        j.selected = True
                        return j

    def click(self, x, y):
        row = x//SQUARE_SIZE
        col = y//SQUARE_SIZE
        return row, col

    def clear(self):
        pass
    #we might not need this (logically)

    def sketch(self, value):
        pass
    #do later

    def place_number(self, value):
        pass
    #do later

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j]=self.original[i][j](self.cells[i][j]).value = self.board[i][j]
                self.update.board()
                self.draw()

    def is_full(self):
        total = 0
        for i in range (0, 9, 1):
            for j in range (0, 9, 1):
                if SG.print_board()[i][j] > 0:
                    total += 1
        if total == 81:
            return True
        else:
            return False

    def update_board(self):
        for i in self.cells:
            for j in i:
                self.board[j.row][j.col] = j.value
    def find_empty(self):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if SG.print_board()[i][j] == 0:
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
