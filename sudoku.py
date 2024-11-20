#main file
import pygame
from sudoku_generator import *
import sys

class Board:
	def __init__(self, width, height, screen):
		self.width = 64 * 9
		self.height = 64 * 10
		self.screen = screen
# Constructor for the Board class.
# screen is a window from PyGame.
# difficulty is a variable to indicate if the user chose easy medium, or hard.

	def draw(self):
		for i in range(10):
			pygame.draw.line(self.screen, "black", (0, i * 64), (576, i * 64))
			pygame.draw.line(self.screen, "black", (i * 64, 0), (i * 64, 576))
		for i in range(4):
			pygame.draw.line(self.screen,"black",(0,i*192),(576,i*192),3)
			pygame.draw.line(self.screen, "black", (i*192, 0), (i*192,576), 3)
	# Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	# Draws every cell on this board.


def main():

	try:
		pygame.init()
		screen = pygame.display.set_mode((576, 640))
		clock = pygame.time.Clock()
		running = True
		screen1 = True
		screen2 = True
		difficulty = None
		board = Board((64 * 9), (64 * 10), screen)
		buttons = display_start(screen)
		pygame.display.flip()

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

								
								
								difficulty = mode
								print(f"Difficulty selected: {mode}")

								sudoku = SudokuGenerator()
								sudoku.remove_cells(difficulty)
								#sudoku.print_board()
								screen1 = False

			while screen2:
				screen.fill("white")
				board = Board((64 * 9), (64 * 10), screen)
				sudoku = SudokuGenerator()
				sudoku.remove_cells(difficulty)
				board.draw()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
						pygame.quit()
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						x, y = event.pos


				pygame.display.flip()
				clock.tick(60)
				

	finally:
		pygame.quit()

#variables


if __name__ == "__main__":
	main()