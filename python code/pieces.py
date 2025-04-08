# game logic for chess project
import pygame
import os 

pygame.init()

# creating the pieces super class
class chessPiece: 

    def __init__(self, color, piece_type, worth, image_path):
        self.color = color
        self.Type = piece_type
        self.worth = worth 

        try:
              self.image = pygame.image.load(image_path)
              print(f"{color}_{piece_type} loaded successfully")
        except pygame.error: 
              print(f"failed to load {piece_type}") 

    
# driver code that initialize the pieces of in both colors
list_of_pieces = ["Pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
colors = ["White", "Black"]

file_directory = os.path.dirname((os.path.abspath(__file__)))
folder = os.path.join(file_directory, "images/")

# dictionary to hold objects of Chesspiece class
created_piece_objects = {}
backrow = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
white_backrow = {}
black_backrow = {}
 # creating one object piece in both colors

def create_pieces():
    for color in colors:
         for piece in list_of_pieces:
             piece_type = f"{color}{piece}"
             image_path = os.path.join(folder, f"{color}_{piece}.png")

          # giving each piece their points
             if piece == "Pawn":
               worth = 1
             elif  piece == "Knight" or piece =="Bishop":
              worth = 3
             elif  piece == "Rook":
              worth = 5
             elif  piece == "Queen":
              worth = 9 
             else:  
              worth = 1000
              #creating the chesspiece objects
             piece_object = chessPiece(color, piece, worth, image_path)
           
           # updating the dictionary each time an object is created
             created_piece_objects[piece_type] = piece_object

    #updating the backrows of each color
    for i, piece in enumerate (backrow):
        white_backrow[i] = created_piece_objects[f"White{piece}"]
        black_backrow[i]=  created_piece_objects[f"Black{piece}"]

          
# calling function to create pieces
create_pieces()

