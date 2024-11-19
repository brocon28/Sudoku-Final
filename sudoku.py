#main file
import pygame
from sudoku_generator import *

def main():

	try:
		pygame.init()
		screen = pygame.display.set_mode((576, 640))
		clock = pygame.time.Clock()
		running = True
		screen1 = True
		display_start(screen)

		while running:
			while screen1:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						x,y = event.pos

					# setting up button presses for screen 1

				pygame.display.flip()
				clock.tick(60)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

	finally:
		pygame.quit()

#variables


if __name__ == "__main__":
	main()