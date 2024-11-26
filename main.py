import pygame
from board import Board
from sudoku_generator import generate_sudoku

def find_selected_cell(board, mouse_pos):
    x, y = mouse_pos
    row = y // (board.height // 9)
    col = x // (board.width // 9)
    if 0 <= row < 9 and 0 <= col < 9:
        return board.board[row][col]
    return None


def display_difficulty_screen(screen):
    font = pygame.font.Font(None, 48)
    easy_button = pygame.Rect(200, 150, 200, 50)
    medium_button = pygame.Rect(200, 250, 200, 50)
    hard_button = pygame.Rect(200, 350, 200, 50)

    # Draw buttons
    pygame.draw.rect(screen, (200, 200, 255), easy_button)
    pygame.draw.rect(screen, (200, 200, 255), medium_button)
    pygame.draw.rect(screen, (200, 200, 255), hard_button)

    # Draw text on buttons
    easy_text = font.render('Easy', True, (0, 0, 0))
    screen.blit(easy_text,
                (easy_button.centerx - easy_text.get_width() // 2, easy_button.centery - easy_text.get_height() // 2))

    medium_text = font.render('Medium', True, (0, 0, 0))
    screen.blit(medium_text, (
    medium_button.centerx - medium_text.get_width() // 2, medium_button.centery - medium_text.get_height() // 2))

    hard_text = font.render('Hard', True, (0, 0, 0))
    screen.blit(hard_text,
                (hard_button.centerx - hard_text.get_width() // 2, hard_button.centery - hard_text.get_height() // 2))

    pygame.display.update()

    # Wait for user to click one of the buttons
    selecting = True
    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return 30  # Easy difficulty
                elif medium_button.collidepoint(event.pos):
                    return 40  # Medium difficulty
                elif hard_button.collidepoint(event.pos):
                    return 50  # Hard difficulty


def draw_buttons(screen):
    font = pygame.font.Font(None, 36)

    # Define button positions
    reset_button = pygame.Rect(50, 620, 150, 50)
    restart_button = pygame.Rect(225, 620, 150, 50)
    exit_button = pygame.Rect(400, 620, 150, 50)

    # Draw buttons
    pygame.draw.rect(screen, (200, 200, 255), reset_button)
    pygame.draw.rect(screen, (200, 200, 255), restart_button)
    pygame.draw.rect(screen, (200, 200, 255), exit_button)

    # Draw text on buttons
    reset_text = font.render('Reset', True, (0, 0, 0))
    screen.blit(reset_text, (
    reset_button.centerx - reset_text.get_width() // 2, reset_button.centery - reset_text.get_height() // 2))

    restart_text = font.render('Restart', True, (0, 0, 0))
    screen.blit(restart_text, (
    restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))

    exit_text = font.render('Exit', True, (0, 0, 0))
    screen.blit(exit_text,
                (exit_button.centerx - exit_text.get_width() // 2, exit_button.centery - exit_text.get_height() // 2))

    pygame.display.update()

    return reset_button, restart_button, exit_button


# Function to check if the Sudoku is valid (completed and correct)
def check_sudoku_win(board):
    # Check rows
    for row in range(9):
        # Extract the values from the cells in the row
        row_values = [cell.value for cell in board[row]]
        if sorted(row_values) != list(range(1, 10)):
            return False  # If a row is invalid, return False

    # Check columns
    for col in range(9):
        column = [board[row][col].value for row in range(9)]  # Extract values from column
        if sorted(column) != list(range(1, 10)):
            return False  # If a column is invalid, return False

    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[row + i][col + j].value)  # Extract values from subgrid
            if sorted(subgrid) != list(range(1, 10)):
                return False  # If a subgrid is invalid, return False

    return True


# Function to display the win screen with exit button
def display_win_screen(screen):
    font = pygame.font.Font(None, 72)
    win_text = font.render("You Win!", True, (0, 255, 0))
    exit_button = pygame.Rect(200, 500, 200, 50)

    # Draw the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(win_text, (screen.get_width() // 2 - win_text.get_width() // 2, screen.get_height() // 2 - win_text.get_height() // 2))

    # Draw Exit button
    pygame.draw.rect(screen, (200, 200, 255), exit_button)
    exit_text = font.render('Exit', True, (0, 0, 0))
    screen.blit(exit_text,
                (exit_button.centerx - exit_text.get_width() // 2, exit_button.centery - exit_text.get_height() // 2))

    pygame.display.update()

    # Wait for exit button click or a quit event
    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()  # Exit the game

    pygame.quit()
def display_lose_screen(screen):
    font = pygame.font.Font(None, 72)
    lose_text = font.render("You Lose!", True, (255, 0, 0))  # Red color for "You Lose!"
    restart_button = pygame.Rect(200, 500, 200, 50)

    # Draw the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(lose_text, (screen.get_width() // 2 - lose_text.get_width() // 2, screen.get_height() // 2 - lose_text.get_height() // 2))

    # Draw Restart button
    pygame.draw.rect(screen, (200, 200, 255), restart_button)
    restart_text = font.render('Restart', True, (0, 0, 0))
    screen.blit(restart_text,
                (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))

    pygame.display.update()

    # Wait for restart button click or a quit event
    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Exit the game

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    main()  # Restart the game by calling main() again
                    waiting_for_restart = False  # Exit the loop to restart the game
                    return  # Exit the function and restart the game

    pygame.quit()




def main():
    pygame.init()
    screen_width, screen_height = 600, 700  # 700px for full screen, 600px for board
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sudoku")

    # Show difficulty selection screen
    difficulty = display_difficulty_screen(screen)

    # Generate the Sudoku puzzle based on difficulty
    board_data = generate_sudoku(9, difficulty)

    # Create the board with the generated puzzle
    board = Board(screen_width, screen_height, screen, board_data)

    running = True
    selected_cell = None

    # Draw buttons
    reset_button, restart_button, exit_button = draw_buttons(screen)
    board.reset()

    while running:
        screen.fill((255, 255, 255))  # Fill the screen with white
        board.draw()  # Draw the Sudoku board (600px tall)
        draw_buttons(screen)  # Draw buttons at the bottom (from y=520)

        # Check if the board is full and validate
        if all(cell.value != 0 for row in board.board for cell in row):
            if check_sudoku_win(board.board):  # Check if the board is correctly filled
                display_win_screen(screen)
                return  # End the game after showing the win screen
            else:
                display_lose_screen(screen)
                return



        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_cell = find_selected_cell(board, event.pos)
                for row in board.board:
                    for cell in row:
                        cell.selected = False
                if selected_cell:
                    selected_cell.selected = True

                # Check if any button is clicked
                if reset_button.collidepoint(event.pos):
                    board.reset()  # Reset the board to its initial state
                elif restart_button.collidepoint(event.pos):
                    main()  # Restart the game by calling main() again
                    running = False  # End the current loop to restart
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()  # Exit the game

            elif event.type == pygame.KEYDOWN:
                if selected_cell and not selected_cell.is_fixed:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        selected_cell.set_sketched_value(event.key - pygame.K_0)
                    elif event.key == pygame.K_BACKSPACE:
                        selected_cell.set_sketched_value(0)
                    elif event.key == pygame.K_RETURN:
                        selected_cell.value = selected_cell.sketched_value
                        selected_cell.sketched_value = 0  # Reset sketched value after confirming it

    pygame.quit()


if __name__ == "__main__":
    main()
