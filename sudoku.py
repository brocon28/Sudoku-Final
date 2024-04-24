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

def game_over_screen():
    pass

def check_if_win(screen):
    win_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(BG_COLOR)

    win_surface = win_title_font.render("Game Won!", True, LINE_COLOR)
    win_rectangle = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(win_surface, win_rectangle)
    # Creates exit button and creates its space on the screen
    exit_text = button_font.render("Exit", True, BG_COLOR)

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(exit_surface, exit_rectangle)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
        pygame.display.update()

def main():#main menu screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    game_over = False

    rem = game_start_screen(screen)

    #Creates instance of board class in order to call board methods.

    cb = Board(2, 2, screen, rem)
    screen.fill(BG_COLOR)

    reset_rect, restart_rect, exit_rect = cb.draw(screen)

    #Creates instance of cell class in order to call cell methods
    # c = Cell(1, 8, 0, screen)
    #Start screen where the Easy, Medium and Hard buttons are placed
    e=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col, row = cb.click(x, y)
                # This if statement accounts for the reset, restart, and quit implementations
                if reset_rect.collidepoint(x, y):
                    cb.reset_to_original()
                if exit_rect.collidepoint(x, y):
                    pygame.quit()
                if restart_rect.collidepoint(x, y):
                    main()



                if 0 <= row <= 8 and 0 <= col <= 8:
                    if cb.original[int(row)][int(col)] == 0:
                        current_cell = cb.select(row, col)
                        selected = True
                        cb.draw(screen)
            # if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            #     e=1
            #     x, y = event.pos
            #     row = int(y//67.5)
            #     col = int(x//67.5)
            #     screen.fill(BG_COLOR)

                # current_cell=b.select(x,y)
                # reset_rect, restart_rect, exit_rect = b.draw(screen)

                for j in range(9):
                    for i in range(9):
                        value = cb.original[i][j]
                        c = Cell(value, i, j, screen)
                        cb.draw(screen)


                if row<9 and col<9:
                    pygame.draw.rect(screen, BLUE, pygame.Rect(col*67,row*67,SQUARE_SIZE//3,SQUARE_SIZE//3),5)
            pygame.display.update()


                #
                # if restart_rect.collidepoint(event.pos):
                #     main()
                # if exit_rect.collidepoint(event.pos):
                #     sys.exit()
                #
                # if restart_rect.collidepoint(event.pos):
                #     game_start_screen()
                # if exit_rect.collidepoint(event.pos):
                #     sys.exit()


            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 and e==1:
                        print('m')
                        if row < 9 and col < 9:
                            if current_cell == 0:
                                cb.select(row, col).set_value(1)

                                d = Cell(1, row, col, screen)
                                d.draw(screen)
                                print(1)
                    #current_cell.set_sketched_value(1)

                # if event.key == pygame.K_2 and e == 1:
                #     current_cell.set_sketched_value(2)
                # if event.key == pygame.K_3 and e == 1:
                #     current_cell.set_sketched_value(3)
                # if event.key == pygame.K_4 and e == 1:
                #     current_cell.set_sketched_value(4)
                # if event.key == pygame.K_5 and e == 1:
                #     current_cell.set_sketched_value(5)
                # if event.key == pygame.K_6 and e == 1:
                #     current_cell.set_sketched_value(6)
                # if event.key == pygame.K_7 and e == 1:
                #     current_cell.set_sketched_value(7)
                # if event.key == pygame.K_8 and e == 1:
                #     current_cell.set_sketched_value(8)
                # if event.key == pygame.K_9 and e == 1:
                #     current_cell.set_sketched_value(9)

                        # This statement checks for the win condition if the board is full
                if cb.is_full():
                    if cb.check_board():
                        check_if_win(screen)
                    else:
                        game_over_screen(screen)
                    game_over = True
                    selected = False







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