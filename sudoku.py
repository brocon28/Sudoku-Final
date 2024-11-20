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

	def draw(self,gameboard):
		big_font = pygame.font.Font(None, 80)
		small_font = pygame.font.Font(None, 50)

		one_surf = small_font.render("1", 0, "black")
		two_surf = small_font.render("2", 0, "black")
		three_surf = small_font.render("3", 0, "black")
		four_surf = small_font.render("4", 0, "black")
		five_surf = small_font.render("5", 0, "black")
		six_surf = small_font.render("6", 0, "black")
		seven_surf = small_font.render("7", 0, "black")
		eight_surf = small_font.render("8", 0, "black")
		nine_surf = small_font.render("9", 0, "black")


		for i in range(10):
			pygame.draw.line(self.screen, "black", (0, i * 64), (576, i * 64))
			pygame.draw.line(self.screen, "black", (i * 64, 0), (i * 64, 576))
		for i in range(4):
			pygame.draw.line(self.screen,"black",(0,i*192),(576,i*192),3)
			pygame.draw.line(self.screen, "black", (i*192, 0), (i*192,576), 3)

		for row in range(9):
			for col in range(9):

				if gameboard.board[row][col] == 1:
					one_rect = one_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(one_surf, one_rect)

				if gameboard.board[row][col] == 2:
					two_rect = two_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(two_surf, two_rect)

				if gameboard.board[row][col] == 3:
					three_rect = three_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(three_surf, three_rect)

				if gameboard.board[row][col] == 4:
					four_rect = four_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(four_surf, four_rect)

				if gameboard.board[row][col] == 5:
					five_rect = five_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(five_surf, five_rect)

				if gameboard.board[row][col] == 6:
					six_rect = six_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(six_surf, six_rect)

				if gameboard.board[row][col] == 7:
					seven_rect = seven_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(seven_surf, seven_rect)

				if gameboard.board[row][col] == 8:
					eight_rect = eight_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(eight_surf, eight_rect)

				if gameboard.board[row][col] == 9:
					nine_rect = nine_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(nine_surf, nine_rect)

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
								screen.fill("white")
								board = Board((64 * 9), (64 * 10), screen)
								sudoku = SudokuGenerator()
								sudoku.fill_values()
								sudoku.remove_cells(difficulty)
								screen1 = False

			while screen2:
				# screen.fill("white")
				# board = Board((64 * 9), (64 * 10), screen)
				# sudoku = SudokuGenerator()
				# sudoku.fill_values()
				# sudoku.remove_cells(difficulty)
				board.draw(sudoku)
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