import pygame
from constants import *
from sudoku_generator import *
from board_cell import * 
import math

def start_menu(screen):
    screen.fill(BACKGROUND) #window background based on constants file

    #title text
    startscreen_title_font_big = pygame.font.Font(None, HEIGHT//10) #default font, large text that is 10% of window
    startscreen_title_text = startscreen_title_font_big.render("Welcome", True, TEXT) #welcome text with provided text color. true makes the letters more smooth
    startscreen_title_position = startscreen_title_text.get_rect(center=(WIDTH//2, HEIGHT//4)) #pick spot for title text, centered and top 
    screen.blit(startscreen_title_text, startscreen_title_position) #copies the text object to the canvas
    startscreen_title_font_big = pygame.font.Font(None, HEIGHT//10) #default font, large text that is 10% of window
    startscreen_title_text = startscreen_title_font_big.render("to Sudoku", True, TEXT) #welcome text with provided text color. true makes the letters more smooth
    startscreen_title_position = startscreen_title_text.get_rect(center=(WIDTH//2, HEIGHT//3)) #pick spot for title text, centered and top 
    screen.blit(startscreen_title_text, startscreen_title_position) #copies the text object to the canvas

    #instructions
    instruction_font = pygame.font.Font(None, HEIGHT//20) #default font, text that is 5% of window
    instruction_text = instruction_font.render("Select Game Mode:", True, TEXT) #instructions text
    instruction_position = instruction_text.get_rect(center=(WIDTH//2, HEIGHT//2)) #instrictions centered in middle
    screen.blit(instruction_text, instruction_position) #render instructions

    #difficulty buttons: e, m, h
    dif_butt_font = pygame.font.Font(None, HEIGHT//20)

    e_button_text = dif_butt_font.render("EASY", True, TEXT) #render text
    e_surface = pygame.Surface((e_button_text.get_size()[0] + BUTTON_PADDING, e_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    e_surface.fill(BUTTON_COLOR) #fill with given color
    e_surface.blit(e_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2)) #draw to screen, centered
    e_position = e_button_text.get_rect(center=(WIDTH // 2, HEIGHT * 7 // 10)) #1/3 from bottom and 3 evenly spaced boxes centered
    screen.blit(e_surface, e_position)

    m_button_text = dif_butt_font.render("MEDIUM", True, TEXT) #render text
    m_surface = pygame.Surface((m_button_text.get_size()[0] + BUTTON_PADDING, m_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    m_surface.fill(BUTTON_COLOR) #fill with given color
    m_surface.blit(m_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2)) #draw to screen, centered
    m_position = m_button_text.get_rect(center=(WIDTH // 2, HEIGHT * 8 // 10)) #1/3 from bottom and 3 evenly spaced boxes centered
    screen.blit(m_surface, m_position)

    h_button_text = dif_butt_font.render("HARD", True, TEXT) #render text
    h_surface = pygame.Surface((h_button_text.get_size()[0] + BUTTON_PADDING, h_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    h_surface.fill(BUTTON_COLOR) #fill with given color
    h_surface.blit(h_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2)) #draw to screen, centered
    h_position = h_button_text.get_rect(center=(WIDTH // 2, HEIGHT * 9 // 10)) #1/3 from bottom and 3 evenly spaced boxes centered
    screen.blit(h_surface, h_position)

    while True:
        for event in pygame.event.get(): #grab each pygame event
            if event.type == pygame.QUIT: #kill the game if x pressed
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: #check for clicks
                if e_position.collidepoint(event.pos): #check if it is on the easy button
                    return 30 #start game with easy settings
                elif m_position.collidepoint(event.pos):
                    return 40
                elif h_position.collidepoint(event.pos):
                    return 50
        pygame.display.update()

def draw_bottom_elements(screen):
    #draw menu options at bottom
    menu_butt_font = pygame.font.Font(None, HEIGHT//20)

    reset_button_text = menu_butt_font.render("RESET", True, TEXT) #render text
    reset_surface = pygame.Surface((reset_button_text.get_size()[0] + BUTTON_PADDING, reset_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    reset_surface.fill(BUTTON_COLOR) #fill with given color
    reset_surface.blit(reset_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2)) #draw to screen, centered
    reset_position = reset_button_text.get_rect(center=(WIDTH // 2, HEIGHT * 7 // 10)) #3 evenly spaced boxes centered, 1/10 from bottom
    screen.blit(reset_surface, reset_position)

    restart_button_text = menu_butt_font.render("RESTART", True, TEXT) #render text
    restart_surface = pygame.Surface((restart_button_text.get_size()[0] + BUTTON_PADDING, restart_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    restart_surface.fill(BUTTON_COLOR) #fill with given color
    restart_surface.blit(restart_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2)) #draw to screen, centered
    restart_position = restart_button_text.get_rect(center=(WIDTH // 2, HEIGHT * 8 // 10)) #3 evenly spaced boxes centered, 1/10 from bottom
    screen.blit(restart_surface, restart_position)

    exit_button_text = menu_butt_font.render("EXIT", True, TEXT) #render text
    exit_surface = pygame.Surface((exit_button_text.get_size()[0] + BUTTON_PADDING, exit_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    exit_surface.fill(BUTTON_COLOR) #fill with given color
    exit_surface.blit(exit_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2)) #draw to screen, centered
    exit_position = exit_button_text.get_rect(center=(WIDTH // 2, HEIGHT * 9 // 10)) #3 evenly spaced boxes centered, 1/10 from bottom
    screen.blit(exit_surface, exit_position)

    return exit_position, reset_position, restart_position

def win_screen(screen):
    screen.fill(WIN)
    win_font = pygame.font.Font(None, HEIGHT//10)
    win_text = win_font.render("Game won!", True, TEXT)
    win_position = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(win_text, win_position)

    menu_butt_font = pygame.font.Font(None, HEIGHT//20)
    restart_button_text = menu_butt_font.render("PLAY AGAIN", True, TEXT) #render text
    restart_surface = pygame.Surface((restart_button_text.get_size()[0] + BUTTON_PADDING, restart_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    restart_surface.fill(BUTTON_COLOR) #fill with given color
    restart_surface.blit(restart_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2))
    restart_position = restart_button_text.get_rect(center=(WIDTH //3, HEIGHT * 9 // 10))
    screen.blit(restart_surface, restart_position)

    exit_button_text = menu_butt_font.render("EXIT", True, TEXT) #render text
    exit_surface = pygame.Surface((exit_button_text.get_size()[0] + BUTTON_PADDING, exit_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    exit_surface.fill(BUTTON_COLOR) #fill with given color
    exit_surface.blit(exit_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2))
    exit_position = exit_button_text.get_rect(center=(WIDTH*2 //3, HEIGHT * 9 // 10))
    screen.blit(exit_surface, exit_position)

    pygame.display.update()

    while True:
        for event in pygame.event.get(): #grab each pygame event
            if event.type == pygame.QUIT: #kill the game if x pressed
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: #check for clicks
                if restart_position.collidepoint(event.pos): #check if it is on the easy button
                    return
                elif exit_position.collidepoint(event.pos): #check if it is on the easy button
                    quit()
        pygame.display.update()

def loss_screen(screen):
    screen.fill(LOSS)
    loss_font = pygame.font.Font(None, HEIGHT//10)
    loss_text = loss_font.render("Game over :(", True, TEXT)
    loss_position = loss_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(loss_text, loss_position)

    menu_butt_font = pygame.font.Font(None, HEIGHT//20)
    restart_button_text = menu_butt_font.render("PLAY AGAIN", True, TEXT) #render text
    restart_surface = pygame.Surface((restart_button_text.get_size()[0] + BUTTON_PADDING, restart_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    restart_surface.fill(BUTTON_COLOR) #fill with given color
    restart_surface.blit(restart_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2))
    restart_position = restart_button_text.get_rect(center=(WIDTH //3, HEIGHT * 9 // 10))
    screen.blit(restart_surface, restart_position)

    exit_button_text = menu_butt_font.render("EXIT", True, TEXT) #render text
    exit_surface = pygame.Surface((exit_button_text.get_size()[0] + BUTTON_PADDING, exit_button_text.get_size()[1] + BUTTON_PADDING)) #create background box around text
    exit_surface.fill(BUTTON_COLOR) #fill with given color
    exit_surface.blit(exit_button_text,(BUTTON_PADDING//2, BUTTON_PADDING//2))
    exit_position = exit_button_text.get_rect(center=(WIDTH*2 //3, HEIGHT * 9 // 10))
    screen.blit(exit_surface, exit_position)

    pygame.display.update()

    while True:
        for event in pygame.event.get(): #grab each pygame event
            if event.type == pygame.QUIT: #kill the game if x pressed
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: #check for clicks
                if restart_position.collidepoint(event.pos): #check if it is on the easy button
                    return
                elif exit_position.collidepoint(event.pos): #check if it is on the easy button
                    quit()
        pygame.display.update()


def main():
    pygame.init() #create pygame instance
    pygame.display.set_caption("Sudoku Game - CS1 Final Project") #window title
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set window dimensions
    cell_selected = False
    while True: #global game loop
        difficulty = start_menu(screen)
        gen = SudokuGenerator(9, difficulty)

        board_list = gen.get_board()
        gen.print_board()

        screen.fill(BACKGROUND) #wipe screen
        exit_position, reset_position, restart_position = draw_bottom_elements(screen) #draw menu options at bottom
        board = Board(WIDTH, WIDTH, screen, difficulty, board_list)
        
        board.draw()

        while True: #gameplay loop where cells are filled in
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #kill the game if x pressed
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: #check for clicks
                    if exit_position.collidepoint(event.pos): #check if it is exit button
                        quit() #exit
                    elif reset_position.collidepoint(event.pos):
                        board.reset_to_original() #test this
                        pass
                    elif restart_position.collidepoint(event.pos):
                        main()
                    else:
                        x, y = event.pos #grab cursor position
                        row, col = board.click(x, y) #grab cell xy index from click function
                        if (row is not None) and (col is not None):
                            print(row, col)
                            current_cell = board.select(row, col)
                            cell_selected = True
                            board.draw()
                pygame.display.update()
                #!!! add arrow key selection of cells
            while cell_selected:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #dict to map keyboard presses to numeric values
                        key_to_num = {
                            pygame.K_1: 1,
                            pygame.K_2: 2,
                            pygame.K_3: 3,
                            pygame.K_4: 4,
                            pygame.K_5: 5,
                            pygame.K_6: 6,
                            pygame.K_7: 7,
                            pygame.K_8: 8,
                            pygame.K_9: 9
                        }
                        if event.key in key_to_num: #check game event key in dict
                            num = key_to_num[event.key]
                            current_cell.set_cell_value(num)
                            current_cell.select = False
                            cell_selected = False
                            board.draw() #redraw updated part of board with new number, i think it keeps track of the current cell?
                        if event.key == pygame.K_BACKSPACE:
                            current_cell.set_cell_value(0)
                            current_cell.select = True
                            board.draw()
                            pygame.display.update()

                        if board.is_full():
                            if board.check_board():
                                win_screen(screen)
                                main()
                            else:
                                loss_screen(screen)
                                main()
                            cell_selected = False
                    pygame.display.update()
                pygame.display.update()
            pygame.display.update()


if __name__ == "__main__":
    main()
