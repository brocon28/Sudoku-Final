import pygame
import sudoku_generator
from tkinter import *

pygame.init()

# Screen constants
WIDTH = 500
HEIGHT = 600
SCREEN = pygame.display.set_mode([HEIGHT,WIDTH])

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (192,192,192)
RED = (250,160,160)

DIFFICULTY = None

# Game initializer
DB = False
menu_showed = False
clock = pygame.time.Clock()

# Window caption
pygame.display.set_caption("Sudoku")

# Fonts
start_title_font = pygame.font.Font(None, 70)
select_title_font = pygame.font.Font(None, 55)
button_font = pygame.font.Font(None, 40)

difficulty_chart = {
    "Easy" : 30,
    "Medium" : 40,
    "Hard" : 50
}

if __name__ == "__main__":
    SCREEN.fill(GREY)

    title_surf = start_title_font.render("Welcome to Sudoku", 1, BLACK)
    title_rect = title_surf.get_rect(center=(WIDTH // 2 + 35, HEIGHT // 2 - 150))
    SCREEN.blit(title_surf, title_rect)

    select_title_surf = select_title_font.render("Select Game Mode:", 1, BLACK)
    select_title_rect = select_title_surf.get_rect(center=(WIDTH // 2 + 35, HEIGHT // 2 - 50))
    SCREEN.blit(select_title_surf, select_title_rect)

    easy = button_font.render("Easy", 0, (255, 255, 255))
    medium = button_font.render("Medium", 0, (255, 255, 255))
    hard = button_font.render("Hard", 0, (255, 255, 255))

    easy_surf = pygame.Surface((easy.get_size()[0] + 20, easy.get_size()[1] + 20))
    easy_surf.fill(BLACK)
    easy_surf.blit(easy, (10, 10))
    med_surf = pygame.Surface((medium.get_size()[0] + 20, medium.get_size()[1] + 20))
    med_surf.fill(BLACK)
    med_surf.blit(medium, (10, 10))
    hard_surf = pygame.Surface((hard.get_size()[0] + 20, hard.get_size()[1] + 20))
    hard_surf.fill(BLACK)
    hard_surf.blit(hard, (10, 10))

    easy_rect = easy.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 25))
    med_rect = medium.get_rect(center=(WIDTH // 2 + 25, HEIGHT // 2 + 25))
    hard_rect = hard.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2 + 25))

    SCREEN.blit(easy_surf, easy_rect)
    SCREEN.blit(med_surf, med_rect)
    SCREEN.blit(hard_surf, hard_rect)

    while DB == False:
        clock.tick(60)

        mpos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DB = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_showed == False:
                    if easy_rect.collidepoint(mpos):
                        DIFFICULTY = "Easy"
                        SCREEN.fill(GREY)

                        board_list = sudoku_generator.generate_sudoku(9, difficulty_chart["Easy"])
                        board = sudoku_generator.Board(SCREEN, board_list)
                        board.draw()

                        menu_showed = True
                    elif med_rect.collidepoint(mpos):
                        DIFFICULTY = "Medium"
                        SCREEN.fill(GREY)

                        board_list = sudoku_generator.generate_sudoku(9, difficulty_chart["Medium"])
                        board = sudoku_generator.Board(SCREEN, board_list)
                        board.draw()

                        menu_showed = True
                    elif hard_rect.collidepoint(mpos):
                        DIFFICULTY = "Hard"
                        SCREEN.fill(GREY)

                        board_list = sudoku_generator.generate_sudoku(9, difficulty_chart["Hard"])
                        board = sudoku_generator.Board(SCREEN, board_list)
                        board.draw()

                        menu_showed = True
                else:

                    for index in range(0, len(sudoku_generator.empty_locations), 2):
                        x = pygame.Rect(sudoku_generator.empty_locations[index])

                        if x.collidepoint(mpos):

                            root = Tk()
                            root.geometry("60x60")

                            def save_input():
                                INPUT = inputtxt.get("1.0", "end-1c")

                                if sudoku_generator.empty_locations[index + 1][2] == True:
                                    print(f"This cell can be edited. Changing the value to {INPUT}")

                                    pygame.draw.rect(SCREEN, RED, x)

                                    r,c = sudoku_generator.empty_locations[index + 1][0], sudoku_generator.empty_locations[index + 1][1]

                                    board.board[r][c] = int(INPUT)
                                else:
                                    print("This cell cannot be edited!")

                                root.destroy()

                            l =  Label(root, text="Input #")

                            inputtxt = Text(root, height=1, width=10, bg="Grey")

                            submit_button = Button(root, height=3, width=5, text="Submit", command=lambda:save_input())

                            l.pack()
                            inputtxt.pack()
                            submit_button.pack()

                            root.mainloop()

                            board.draw()

        pygame.display.flip()