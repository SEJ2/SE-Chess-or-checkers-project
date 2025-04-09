# game logic for chess project

import pygame
import os 
import chess
import chess.engine

# initialize pygame and setup display
pygame.init()
WIDTH, HEIGHT = 600, 600  
ROWS, COLS = 8, 8  #chess board 8x8
SQUARE_SIZE = WIDTH // COLS
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pygame Chess")
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
clock = pygame.time.Clock()
fps = 60

# create a class for chess pieces
class chesspiece: 
    def __init__(self, color, Letter_Type, worth, image_path):
        self.color = color  # "white" or "black"
        self.Letter_Type = Letter_Type  #"pawn" or "rook" etc
        self.worth = worth  #  value of the piece (For min/max)
        self.image = pygame.image.load(image_path)  # load image from file

# list of chess piece names to be loaded
types = ["pawn", "bishop", "knight", "rook", "queen", "king"]
colors = ["white", "black"]

# dictionary to hold the loaded pieces. Thought this would be easier
pieces_dict = {}

# function to create and load all pieces from images folder
def create_pieces():
    for color in colors:
        for piece_type in types:
            name = f"{color}_{piece_type}"
            image_path = os.path.join("images", f"{name}.png")
            try:
                piece_obj = chesspiece(color, piece_type, 1, image_path)  # worth is placeholder
                pieces_dict[name] = piece_obj
                print(f"Loaded {name} successfully from {image_path}")
            except Exception as e:
                print(f"Failed to load {name} from {image_path}: {e}") #image debug

# call the piece creation function
create_pieces()

# function to draw the chess board
def draw_board():
    colors = [(238, 238, 210), (118, 150, 86)]  # light and dark squares
    for row in range(ROWS):
        for col in range(COLS):
            color = colors[(row + col) % 2] #alternates colors of chess board
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    # layout of pieces in standard starting positions
    piece_layout = [
        ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"],
        ["pawn"] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        ["pawn"] * 8,
        ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
    ]

    for row in range(ROWS):
        for col in range(COLS):
            piece_type = piece_layout[row][col]  # get piece type from layout
            if piece_type:
                color = "black" if row < 2 else "white"  # decide piece color based on row
                piece_name = f"{color}_{piece_type}"
                piece = pieces_dict.get(piece_name)  # fetch piece from dictionary
                if piece:
                    x = col * SQUARE_SIZE  # x position for drawing
                    y = row * SQUARE_SIZE  # y position for drawing
                    image_scaled = pygame.transform.scale(piece.image, (SQUARE_SIZE, SQUARE_SIZE))  # scale image to fit square
                    screen.blit(image_scaled, (x, y))  # draw image on board

# main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # fill background with white before drawing board
    draw_board()  
    draw_pieces()  # draw all chess pieces in their starting positions

    # handle closing window (Hitting X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # exit the loop when the window is closed

        # TO DO Add piece movement logic here
        #This is where you'll handle selecting and moving pieces

    pygame.display.flip()  # updates display
    clock.tick(fps)  # controls frame rate

pygame.quit()

