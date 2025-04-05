import chess
import chess.engine
from pieces import pygame

pygame.init

#setting up the screen display

WITDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode([WITDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 80


class Square:
    
    def __init__(self, color, row, collumn, piece = None):
       self.color = color
       self.row = row
       self.collumn = collumn
       self.piece = piece



# creating the board 
class board:
     def __init__(self, size = 8):
         (self)

pygame.display(board)