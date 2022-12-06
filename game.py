import pygame
import os
from cell import Cell
from board import Board
import button
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku Game")

def main_menu():
  # Sets screen resolution
  start_screen = pygame.display.set_mode((550, 700))

  # Draws the background iimage for the main screen
  start_screen.blit(BACKGROUND_IMAGE, (0, -80))
  start_screen.blit(TITLE, (40, 425))

  # Initializes button class with position
  easy_button = button.Button(100, 600, EASY_BUTTON)
  medium_button = button.Button(205, 600, MEDIUM_BUTTON)
  hard_button = button.Button(348, 600, HARD_BUTTON)

  # Puts/draws the buttons on the main_menu
  easy_button.draw(start_screen)
  medium_button.draw(start_screen)
  hard_button.draw(start_screen)

  while True:
    # event loop for each click or action done in the main menu
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if easy_button.draw(start_screen):
          game_screen()
        if medium_button.draw(start_screen):
          game_screen()
        if hard_button.draw(start_screen):
          game_screen()

    # Updates the display of the main screen
    pygame.display.update()

def game_screen():
  game_screen = pygame.display.set_mode((540, 600))
  game_screen.fill((255, 144, 109))

  # Initializes button class with position
  reset_button = button.Button(110, 550, RESET_BUTTON)
  restart_button = button.Button(215, 550, RESTART_BUTTON)
  exit_button = button.Button(348, 550, EXIT_BUTTON)

  # Puts/draws the buttons on the main_menu
  reset_button.draw(game_screen)
  restart_button.draw(game_screen)
  exit_button.draw(game_screen)

  while True:
    # event loop for each click or action done in the game
    testBoard = Board(540, 540, game_screen, "easy")
    testBoard.draw()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      # Checks if a cell is clicked
      if event.type == pygame.MOUSEBUTTONDOWN:
        if reset_button.draw(game_screen):
          pass
        if restart_button.draw(game_screen):
          pass
        if exit_button.draw(game_screen):
          pygame.quit()

    pygame.display.update()

if __name__ == "__main__":
  main_menu()








