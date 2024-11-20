#main file
import pygame
from sudoku_generator import *
import sys

def main():

	try:
		pygame.init()
		screen = pygame.display.set_mode((576, 640))
		clock = pygame.time.Clock()
		running = True
		screen1 = True
		difficulty = None
		buttons = game_over(screen)
		pygame.display.flip()
		board = SudokuGenerator()

		while running:
			while screen1:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
						pygame.quit()
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						x,y = event.pos
						for button_rect, mode in buttons:
							if button_rect.collidepoint(x,y):
								screen1 = False
								board.draw()
								
								
								difficulty = mode
								print(f"Difficulty selected: {mode}")

								sudoku = SudokuGenerator()
								sudoku.remove_cells(difficulty)

								
					

					# setting up button presses for screen 1
				pygame.display.flip()
				clock.tick(60)
				

	finally:
		pygame.quit()

#variables


if __name__ == "__main__":
	main()