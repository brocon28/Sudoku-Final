import pygame
import sys
from board import Board
from cell import *
from constants import *
from sudoku_generator import SudokuGenerator


def game_start_screen(screen):
    # Sets the background to white
    screen.fill(WHITE)

    # Title
    title_font = pygame.font.Font(None, 64)
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Displays "Select Game Mode:"
    mode_font = pygame.font.Font(None, 32)
    mode_text = mode_font.render("Select Game Mode:", True, BLACK)
    mode_rect = mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mode_text, mode_rect)

    # Creates easy, medium, and hard buttons
    button_font = pygame.font.Font(None, 32)
    easy_button = button_font.render("Easy", True, BLACK)
    easy_rect = easy_button.get_rect(center=(WIDTH // 4, HEIGHT * 3 // 4))
    screen.blit(easy_button, easy_rect)

    medium_button = button_font.render("Medium", True, BLACK)
    medium_rect = medium_button.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(medium_button, medium_rect)

    hard_button = button_font.render("Hard", True, BLACK)
    hard_rect = hard_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 3 // 4))
    screen.blit(hard_button, hard_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    game_over = False

    screen.fill(BG_COLOR)
    c = Cell(1, 1, 1, screen)
    c.draw()
    b = Board(2, 2, screen, 1)
    b.draw()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x, y = event.pops
                row = y // SQUARE_SIZE
                col = (x // SQUARE_SIZE)
        # Clear the screen
        screen.fill((0, 0, 0))
        game_start_screen(screen)

        pygame.display.update()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
