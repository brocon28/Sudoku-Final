import pygame
import sys
from constants import *
from board import Board
import cell
import constants
from sudoku_generator import SudokuGenerator
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUDOKU")
window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
window.fill(BG_COLOR)

cell1 = cell.Cell(4, WIDTH//2, HEIGHT//2, window)
cell1.draw(window)

game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
