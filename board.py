import pygame
from cell import Cell
from sudoku_generator import *

class Board():
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.gap = self.width / 9

        if self.difficulty == "easy" or "Easy":
            self.board = generate_sudoku(9, 30)

        if self.difficulty == "medium" or "Medium":
            self.board = generate_sudoku(9, 40)

        if self.difficulty == "hard" or "Hard":
            self.board = generate_sudoku(9, 50)

        self.cubes = []
        for i in range(9):
            for j in range(9):
                self.cubes.append(Cell(self.board[i][j], i, j, width, height))

    def draw(self):
        # Draws The Grid Lines on the Screen
        for i in range(10):
            if i != 0 and i % 3 == 0:
                thick = 4
            else:
                thick = 1
                pygame.draw.line(self.screen, (0,0,0), (0, i*self.gap), (self.width, i*self.gap), thick)
                pygame.draw.line(self.screen, (0, 0, 0), (i * self.gap, 0), (i * self.gap, self.height), thick)
        for i in range(10):
            for j in range(10):



    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
