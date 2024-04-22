import pygame
import sudoku_generator

pygame.init()

# Screen constants
WIDTH = 500
HEIGHT = 600
SCREEN = pygame.display.set_mode([HEIGHT,WIDTH])

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (192,192,192)

DIFFICULTY = None

# Game initializer
DB = False
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
                if easy_rect.collidepoint(mpos):
                    DIFFICULTY = "Easy"
                    SCREEN.fill(GREY)
                    board = sudoku_generator.Board(50, 40, SCREEN, difficulty_chart["Easy"])
                    board.draw()
                elif med_rect.collidepoint(mpos):
                    DIFFICULTY = "Medium"
                    SCREEN.fill(GREY)
                    board = sudoku_generator.Board(50, 40, SCREEN, difficulty_chart["Medium"])
                    board.draw()
                elif hard_rect.collidepoint(mpos):
                    DIFFICULTY = "Hard"
                    SCREEN.fill(GREY)
                    board = sudoku_generator.Board(50, 40, SCREEN, difficulty_chart["Hard"])
                    board.draw()
                else:
                    DIFFICULTY = None

        pygame.display.flip()
