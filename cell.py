import constants
import pygame
from constants import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen #maybe something else, not so sure yet?
        self.touch = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        self.value = value

    def draw(self):
        BLACK=(0,0,0)
        WHITE=(255,255,255)
        RED=(255,0,0)
        GREEN=(0,255,0)
        BLUE=(0,0,255)
        num_font = pygame.font.SysFont('arial', 12)
        #drawing the surface of each number
        n1_num=num_font.render("1", True, WHITE)
        n2_num=num_font.render("2", True, WHITE)
        n3_num=num_font.render("3", True, WHITE)
        n4_num=num_font.render("4", True, WHITE)
        n5_num=num_font.render("5", True, WHITE)
        n6_num=num_font.render("6", True, WHITE)
        n7_num=num_font.render("7", True, WHITE)
        n8_num=num_font.render("8", True, WHITE)
        n9_num=num_font.render("9", True, WHITE)

        #if self.touch==True:
        #    pygame.draw.rect(self.screen, BLUE,pygame.Rect(self.column * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),2)

        if self.value==1:
            num_rect=n1_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n1_num, num_rect)
        if self.value==2:
            num_rect=n2_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n2_num, num_rect)

        if self.value==3:
            num_rect=n3_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n3_num, num_rect)

        if self.value==4:
            num_rect=n4_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n4_num, num_rect)

        if self.value==5:
            num_rect=n5_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n5_num, num_rect)

        if self.value==6:
            num_rect=n6_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n6_num, num_rect)

        if self.value==7:
            num_rect=n7_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n7_num, num_rect)


        if self.value==8:
            num_rect=n8_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n8_num, num_rect)


        if self.value==9:
            num_rect=n9_num.get_rect(
                center=(SQUARE_SIZE * self.column + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2))
            self.screen.blit(n9_num, num_rect)








