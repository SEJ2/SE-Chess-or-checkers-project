# game logic for chess prject
import pygame
import os 

pygame.init()

WITDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode([WITDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 80


# creating the pieces super class
class chesspiece: 

    def __init__(self, color, Type, worth, image_path):
        self.color = color
        self.Type = Type
        self.worth = worth
        self.image = pygame.image.load(image_path)   
    
# driver code that initialize the pieces of in both colors
list_of_pieces = ["Pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
folder = "images/"
colors = ["White", "Black"]

types_of_subclasses = {}
 #creating subclasse for each piece
# function for creating the subclass 
def create_pieces_subclasses(self):
 for color in color:
      for piece in list_of_pieces:
         def __init__(chesspiece):
           class piece(chesspiece):
              super.__init_subclass__(f"{list_of_pieces}")
              types_of_subclasses = {}
              
# importing images files and dynamically assigning images      
 for types in types_of_subclasses:
     image_path = os.path.join(f"{folder},{colors}_{type}.png")
     try:
      hasattr(piece,"image_path")
      print("file loaded usccesfuly")
     except AttributeError: 
      print("failed to load piece image")
