# game logic for chess prject
import pygame
import os 

pygame.init()


# creating the pieces super class
class chessPiece: 

    def __init__(self, color, Type, worth, image_path):
        self.color = color
        self.Type = Type
        self.worth = worth 
        try:
              self.image = pygame.image.load(image_path)
              print(f"{color}_{Type} loaded successfuly")
        except pygame.error: 
              print(f"failed to load {Type}_{image_path}")  

    
# driver code that initialize the pieces of in both colors
list_of_pieces = ["Pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
colors = ["White", "Black"]

file_directory = os.path.dirname((os.path.abspath(__file__)))
folder = os.path.join(file_directory, "images/")

# dictionary to hold objects of chesspice class
types_of_object = {}

 # creating one object piece in both colors


def create_pieces():
 for color in colors:
      for piece in list_of_pieces:
          piece_type = f"{color}{piece}"
          image_path = os.path.join(folder, f"{color}_{piece}.png")
          piece_object = chessPiece(color, piece, 0, image_path)
           
           # updating the dictionary each time an object is created
          types_of_object[piece_type] = piece_object

              
# calling function to create pieces
create_pieces() 
