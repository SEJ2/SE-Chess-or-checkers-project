# game logic for chess project
import pygame
import os

pygame.init()


# creating the pieces super class
class chessPiece:

    def __init__(self, color, piece_type, worth, image_path):
        self.color = color
        self.piece_type = piece_type
        self.worth = worth
        self.captured = False
        self.valid_moves = []
        try:
            self.image = pygame.image.load(image_path)
            print(f"{color}_{piece_type} loaded successfully")
        except pygame.error:
            print(f"failed to load {piece_type}")
     

# driver code that initialize the pieces of in both colors
types_of_pieces = ["Pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
colors = ["White", "Black"]

file_directory = os.path.dirname((os.path.abspath(__file__)))
folder = os.path.join(file_directory, "images/")

# dictionary to hold objects of Chesspiece class
created_pieces = {}
backrow = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
white_backrow = {}
black_backrow = {}

# creating one object piece in both colors
def create_pieces():
    for color in colors:
        for type in types_of_pieces:
            image_path = os.path.join(folder, f"{color}_{type}.png")

            # giving each piece their points
            if type == "Pawn":
                worth = 1
            elif type == "Knight" or type == "Bishop":
                worth = 3
            elif type == "Rook":
                worth = 5
            elif type == "Queen":
                worth = 9
            else:
                worth = 1000

            # creating the chesspiece objects
            piece = chessPiece(color, type, worth, image_path)

           # if piece:
              #  valid_moves = piece.valid_moves

            # updating the dictionary each time an object is created
            created_pieces[f"{color}_{type}"] = piece

    # updating the backrows of each color
    for i, piece in enumerate(backrow):
        white_backrow[i] = created_pieces[f"White_{piece}"]
        black_backrow[i] = created_pieces[f"Black_{piece}"] 

def promotion(self, old_piece, new_piece):
    White_promotion_row = white_backrow
    Black_promotion_row = black_backrow

    if old_piece.color == "White":
        new_piece.color == "White"
    else:
        new_piece.color == "Black"
    pass
create_pieces()
