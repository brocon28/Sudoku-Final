import pygame
import sys

from pygame import Surface, SurfaceType

import board
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator
pygame.init()
#screen: Surface | SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUDOKU")

"""board = Board.draw(Board)
board[1][2]="1"
board[2][2]="2"
player = 1
chip = "1"
game_over=False
winner=0"""
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BG_COLOR)

#cell1 = Cell(4, WIDTH//2, HEIGHT//2, window)
#cell1.draw(window)

game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
game_over = False



"""

def draw_grid():
    pygame.draw.line(screen, LINE_COLOR, (0, 575), (500 * SQUARE_SIZE, HEIGHT), LINE_WIDTH // 2)
    pygame.draw.line(screen, LINE_COLOR, (0, 0), (800 * SQUARE_SIZE, HEIGHT), LINE_WIDTH // 2)

    #Draw horizontal ine
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0,i*SQUARE_SIZE), (WIDTH, i*SQUARE_SIZE), LINE_WIDTH//2)

    #draw vertical line:
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (i*SQUARE_SIZE, 0), (i*SQUARE_SIZE, HEIGHT-125), LINE_WIDTH//2)


"""

screen.fill(BG_COLOR)
c = Cell(1, 1, 1, screen)
c.draw()
b = Board(2, 2, screen, 1)
b.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x,y=event.pops
            row = y//SQUARE_SIZE
            col = (x//SQUARE_SIZE)

    pygame.display.update()



"""            if available_square(board, row, col):
                mark_square(board, rowl, col, chip)
                if check_if_winner(board, num):
                    game_over = True
                    winner = player

                else:
                    if board_is_full(board):
                        game_over = True
                        winner =0 #indicates a tie

            player = 2 if player==1 else 1"""





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
