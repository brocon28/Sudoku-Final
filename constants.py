import pygame
import os

WIDTH = 550
HEIGHT = 700
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_HEIGHT = 25
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)
CIRCLE_COLOR = (155, 155, 155)
CROSS_COLOR = (66, 66, 66)

BACKGROUND_IMAGE = pygame.image.load(os.path.join('images', 'background.jpg'))
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (550, 900))
TITLE = pygame.image.load(os.path.join('images', 'sudoku.jpg'))
TITLE = pygame.transform.scale(TITLE, (475, 90))


EASY_BUTTON = pygame.image.load(os.path.join('images', 'easy.png'))
MEDIUM_BUTTON = pygame.image.load(os.path.join('images', 'medium.png'))
HARD_BUTTON = pygame.image.load(os.path.join('images', 'hard.png'))