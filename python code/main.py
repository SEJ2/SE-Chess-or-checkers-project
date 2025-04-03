# game logic for chess prject

import pygame
import os 
import chess
import chess.engine


pygame.init()

WITDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode([WITDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.clock()
fps = 80
  

# creating the pieces class
class chesspiece: 

    def __init__(self, color, Letter_Type, worth, image_path):
        self.color = color
        self.Letter_Type = Letter_Type
        self.worth = worth
        self.image = pygame.image.load(image_path)
               
    
# driver code that initialize the pieces of in both colors
list_of_pieces = { 
"Black_Pawn" , "White_Pawn", 
"Black_Bishop", "White_Bishop",
"Black_Knight", "White_Knight",
"Black_Rook", "White_Rook",
"Black_Queen", "White_Queen",
"Black_King", "White_King"
}
    
    
    
# importing images files and dynamically assigning images
              
                 
def creating_pieces(self, list_of_pieces):
    for piece in list_of_pieces:
     image_path = os.path.join("images, ")



def image_load_debug (self, piece):
            try:
                 hasattr(piece,"image_path")
                 print("file loaded usccesfuly")
            except AttributeError: 
                 print("failed to load piece image")