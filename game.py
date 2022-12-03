import pygame
import os
import button
from constants import *

run = True
pygame.init()
pygame.display.set_caption("Soduku Game")
start_screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

def start_window():

  start_screen.blit(BACKGROUND_IMAGE, (0, -80))
  start_screen.blit(TITLE, (40, 425))
  # Drawing buttons on screen

  easy_button = button.Button(100, 600, EASY_BUTTON)
  medium_button = button.Button(205, 600, MEDIUM_BUTTON)
  hard_button = button.Button(348, 600, HARD_BUTTON)

  if easy_button.draw(start_screen):
    pass
  if medium_button.draw(start_screen):
    pass
  if hard_button.draw(start_screen):
    pass

  pygame.display.update()

def game_window():
  pass

def main():

  run = True

  while run:
    # event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        continue

    start_window()

if __name__ == "__main__":
  main()








