import pygame
from Button import Button

# Basic Settings
pygame.init()

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.image.load("backgroundimage.jpg")
screen.blit(bg, (0, 0))
pygame.display.set_caption("Sudoku game")

game_state = "start_menu"

easy_img = pygame.image.load("easy.png").convert_alpha()
medium_img = pygame.image.load("medium.png").convert_alpha()
hard_img = pygame.image.load("hard.png").convert_alpha()
exit_img = pygame.image.load("exit.png").convert_alpha()
reset_img = pygame.image.load("reset.png").convert_alpha()
restart_img = pygame.image.load("restart.png").convert_alpha()

easy_button = Button(75, 360, easy_img, 0.2)
medium_button = Button(225, 360, medium_img, 0.2)
hard_button = Button(375, 360, hard_img, 0.2)
reset_button = Button(80, 510, reset_img, 0.15)
restart_button = Button(235, 510, restart_img, 0.15)
exit_button = Button(390, 510, exit_img, 0.15)



def draw_start_menu():
    font = pygame.font.SysFont('arial', 60)
    title = font.render('SUDOKU', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_WIDTH / 2 - title.get_height()))
    pygame.display.update()


def draw_game_over_screen():
    screen.blit(bg, (0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    quit_button = font.render('Q-Quit', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_WIDTH / 2 - title.get_height() / 3))
    screen.blit(quit_button,
                (SCREEN_WIDTH / 2 - quit_button.get_width() / 2, SCREEN_WIDTH / 2 + quit_button.get_height() / 2))
    pygame.display.update()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if game_state == "start_menu":
        draw_start_menu()
        if easy_button.draw(screen):
            game_state = 'game'
        if medium_button.draw(screen):
            game_state = 'game'
        if hard_button.draw(screen):
            game_state = 'game'
        game_over = False

    elif game_state == "game_over":
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    elif game_state == "game":
        screen.fill((251, 247, 245))
        keys = pygame.key.get_pressed()

        if reset_button.draw(screen):
            game_state = 'game'

        if restart_button.draw(screen):
            game_state = 'start_menu'

        if exit_button.draw(screen):
            quit()

        if keys[pygame.K_j]:
            game_state = "game_over"

        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
        pygame.display.update()
