import pygame
import sys
from board import Board
from cell import *
from constants import *
from sudoku_generator import *


def game_start_screen(screen):
    game_over = False
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
    #EASY BUTTON:
    button_font = pygame.font.Font(None, 32)
    easy_button = button_font.render("Easy", True, BLACK)
    easy_surface=pygame.Surface((easy_button.get_size()[0]+20, easy_button.get_size()[1]+20))
    easy_surface.fill((255,100,180))
    easy_surface.blit(easy_button,(10,10))
    easy_rect = easy_button.get_rect(center=(WIDTH // 4, HEIGHT * 3 // 4))
    screen.blit(easy_surface, easy_rect)
    #MEDIUM BUTTON:
    medium_button = button_font.render("Medium", True, BLACK)
    medium_surface=pygame.Surface((medium_button.get_size()[0]+20, medium_button.get_size()[1]+20))
    medium_surface.fill((255,0,230))
    medium_surface.blit(medium_button,(10,10))
    medium_rect = medium_button.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(medium_surface, medium_rect)
    #HARD BUTTON:
    hard_button = button_font.render("Hard", True, BLACK)
    hard_surface=pygame.Surface((hard_button.get_size()[0]+20, hard_button.get_size()[1]+20))
    hard_surface.fill((220,0,255))
    hard_surface.blit(hard_button,(10,10))
    hard_rect = hard_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 3 // 4))
    screen.blit(hard_surface, hard_rect)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    return 30
                if medium_rect.collidepoint(event.pos):
                    return 40
                if hard_rect.collidepoint(event.pos):
                    return 50
        pygame.display.update()
#     game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

def main():#main menu screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    game_over = False

    rem = game_start_screen(screen)
    z = generate_sudoku(9, rem)

    #Creates instance of board class in order to call board methods.
    b = Board(2, 2, screen, rem)
    screen.fill(BG_COLOR)
    reset_rect, restart_rect, exit_rect = b.draw(screen)


    #Creates instance of cell class in order to call cell methods
    # c = Cell(1, 8, 0, screen)
    #Start screen where the Easy, Medium and Hard buttons are placed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row = int(y//67.5)
                col = int(x//67.5)


                if restart_rect.collidepoint(event.pos):
                    main()
                if exit_rect.collidepoint(event.pos):
                    sys.exit()


                if 0 <= row <= 8 and 0 <= col <= 8:
                    if b.board[int(row)][int(col)] == 0:
                        current_cell = b.select(row, col)
                        current_cell.touch = True
                        b.draw(screen)
                        print(current_cell.touch)
                # if 0<=row <=8 and 0<=col<=8:

                    # if b.board[row][col] == 0:
                    #     cur_cel = b.select(row, col)
                    #
                    #     cur_cel.touch = True
                    #
                    #     #print(b.cells[0])
                    #     b.draw(screen)
                    #     print(cur_cel.touch)

                if restart_rect.collidepoint(event.pos):
                    game_start_screen()
                if exit_rect.collidepoint(event.pos):
                    sys.exit()

                pygame.display.update()

                pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()



        pygame.display.update()

    #
    # while True:
    #     for event in pygame.event.get():
    #
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             c.touch = True
    #             x, y = event.pos
    #             row = y // SQUARE_SIZE
    #             col = x // SQUARE_SIZE
    #             print(event)
    #             screen.fill(BG_COLOR)
    #             b = Board(2, 2, screen, 1)
    #             b.draw()
    #             screen.blit(reset_surface, reset_rect)
    #             screen.blit(restart_surface, restart_rect)
    #             screen.blit(exit_surface, exit_rect)
    #
    #             for j in range(9):
    #                 for i in range(9):
    #                     value = z[i][j]
    #
    #                     c = Cell(value, i, j, screen)
    #                     c.draw()
    #             pygame.draw.rect(c.screen, BLUE,
    #                              pygame.Rect(x, y,
    #                                          SQUARE_SIZE // 3, SQUARE_SIZE // 3), 2)
    #
    #             # pygame.draw.line(screen, (0,0,255), (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), LINE_WIDTH // 3)
    #             # column, row, width, height
    #
    #             pygame.display.update()
    #
    #
    #             c.touch=False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #Initialize pygame, set the screen, and go to the start page