
import pygame
from pieces import *
from game import *

pygame.init()

#setting up the screen display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60

# setting color options for the squares
dark = (125, 135, 150)
light = (232,235,239)

class Square:
    def __init__(self, color, size, column, row,  piece):
       self.color = color
       self.size = size
       self.column = column 
       self.row = row    
       self.piece = piece  

    def draw_square(self, surface):
        rectangle = pygame.Rect(self.column * self.size, self.row * self.size, self.size, self.size)
        pygame.draw.rect(surface, self.color, rectangle)
        
    def has_piece(self):
        if self.piece != None:
            return self.piece
        
    def get_piece(self):
        return self.piece
        
    #function for drawing pieces on the board
    def draw_pieces(self, surface):
        if self.piece and hasattr(self.piece, "image"):
           resized_image = pygame.transform.scale(self.piece.image, (self.size, self.size))
           surface.blit(resized_image, (self.column * self.size, self.row *self.size))

# creating the board 
class ChessBoard:
    def __init__(self, surface, column = 8, Rows = 8):
         self.column = column
         self.Rows = Rows
         self.square_objects = [[None for i in range(self.column)] for i in range(self.Rows)]
         self.square_size = WIDTH // self.column
         #functions for drawing
         self.create_squares(surface)
         self.pieces_starting_position(surface)
         #variables for moving piece
         #self.piece_valid_moves = pieces.
         self.start_move_square = None
         self.end_move_square = None 
         self.piece_selected_to_move = None  #switch to self.piece_selected_to_move 
         self.destination_square = None 
         pieces.create_pieces()
         
#creating squares
    def create_squares(self,surface):
         for column in range(self.column):
             for row in range(self.Rows):
               if ( column + row ) %2 == 0:
                   color = dark
               else:
                    color = light 
               square = Square(color, self.square_size, column, row,  piece = None)
               #assign it a coordinate and update the list
               self.square_objects [row][column]= square
               square.draw_square(surface) # draw the square

      # funtion to access squares on the board        
    def get_square(self, col, row):
        if col >= 0 and col < self.column:
            if row >= 0 and row < self.Rows:
                return self.square_objects[row][col]

    #function for assigning pieces their initial posotion on the board
    def pieces_starting_position(self,surface):
        pieces.create_pieces() 
        
        #assigning the White pieces in the backrow starting postion
        for col, piece_object in enumerate(pieces.white_backrow):
            piece = pieces.white_backrow[piece_object]
            print(f"placing {piece.piece_type} at col {col}, row 7")
            square = square = self.get_square(col, 7)
            square.piece = piece
                     
           #assigning the Pawns starting postion
        for col in range(self.column):
            square = square = self.get_square(col, 6)
            square.piece = pieces.created_piece_objects["WhitePawn"]

         #assigning the Black pieces in the backrow starting postion
        for col, piece_object in enumerate(pieces.black_backrow):
            piece = pieces.black_backrow[piece_object]
            square = square = self.get_square(col, 0)
            square.piece = piece
                     
           #assigning the the Pawns starting postion
        for col in range(self.column):
            square = square = self.get_square(col, 1)
            square.piece = pieces.created_piece_objects["BlackPawn"]  


            # assigning the valid moves to the pieces
    def assign_valid_moves(self, piece, col, row):
        self.piece = piece
# bound checking to get the clicked square
        for sqr in self.square_objects:
            if  0 <= col < self.column and 0 <= row < self.Rows:

                #valid moves for 
                if piece.piece_type == "Pawn" :
                    if piece.color == "White":
                     #setting the pawn to moves only one direction 
                        piece.valid_moves = [(col, row -1)]
                     
                    elif piece.color == "Black":
                        piece.valid_moves = [(col, row + 1)]
                        
                #valid moves for Knights
                elif piece.piece_type == "Knight":
                    
                    piece.valid_moves = [
                            (col + 2, row + 1),
                            (col + 2, row - 1),
                            (col - 2, row + 1), 
                            (col - 2, row - 1),
                            (col + 1, row + 2),
                            (col - 1, row + 2),
                            (col - 1, row - 2),
                            (col - 1, row + 2)
                                            ]
                    
                     #valid moves for Bishops
                elif piece.piece_type == "Bishop":
                    for i, in range(self.square_objects):
                        piece.valid_moves = [ 
                            (col - i, row - i), #getting all top left diagonal sqaures
                            (col + i, row - 1), #getting all top right diagonal sqaures
                            (col - i, row + i), #getting all bottom left diagonal sqaures
                            (col + i, row + i) #getting all botoom right diagonal sqaures
                                                ]
                    
                 #valid moves for Rooks        
                elif piece.piece_type == "Rook":
                    for i, in range(self.square_objects):
                        piece.valid_moves = [
                            (col - i, row), #getting all squares left  of it
                            (col + i, row), #getting all squares right of it
                            (col, row + i), #getting all squares above of it
                            (col, row - i) #getting all squares below of it
                                            ]
                        
                  #valid moves for Queen is a combination of rooks and bishops    
                elif piece.piece_type == "Queen":
                     # queen is a combination of Rook and Bishop
                    piece.valid_moves = piece.type.Rook.valid_moves + piece.type.Bishop.valid_moves
                 #valid moves for King is one sqaure in each direction
                elif piece.piece_type == "King":
                        piece.valid_moves = [ 
                            (col - 1, row - 1), #move to top left diagonal square #getting one square to the left 
                            (col, row - 1), #move to one square above
                            (col + 1, row - 1), #move to top right diagonal square
                            (col - 1, row),#move to the left
                            (col + 1, row),  #move to the right
                            (col - 1, row + 1),  #move to botom left
                            (col, row + 1), #move to bottom
                            (col + 1, row + 1) #move tobotom right
                                            ]


#moving the pieces to tiles in its list of valid move       
    def move_piece(self, position):
        col = position[0] //self.square_size
        row = position[1] //self.square_size
         
        # bound checking to get the clicked square
        if  0 <= col < self.column and 0 <= row < self.Rows: 
            self.start_move_square = self.get_square(col, row) 

            if self.start_move_square.has_piece():
                print(f"clicked on square with piece: {self.start_move_square.piece.piece_type}")  
            else:
                print("clicked on empty square")


                 #checking to see if there is selected piece
        if self.piece_selected_to_move:
                   #selecting the another piece if one is already selected
                   if self.start_move_square.piece and self.start_move_square.piece.color == self.piece_selected_to_move.color:
                    self.end_move_square = self.start_move_square
                    self.piece_selected_to_move  = self.start_move_square.piece

                   else:
                    # updating piece position and resetting selction variables
                     self.start_move_square.piece = self.piece_selected_to_move
                     print(f"Moved {self.start_move_square.piece.piece_type} to ({col})({row})")
                     self.end_move_square.piece = None
                     self.piece_selected_to_move  = None
                     self.end_move_square = None
                     

        else: 
            if self.start_move_square.piece: # selecting a piece
                self.piece_selected_to_move  = self.start_move_square.piece
                self.end_move_square = self.start_move_square
        
            






def promotion(self, color, old_piece, new_piece):
    White_promotion_row = self.square_object.Row[0]
    Black_promotion_row = self.square_object.Row[7]
    
    old_piece = pieces.Type.Pawn 
    new_piece = pieces.Type.Queen

    if old_piece.color == "White":
        new_piece. color == "White"
    else:
        new_piece. color == "Black"
    pass     
            
def main():
    running = True
    chessboard = ChessBoard(screen)
    selected_piece = None
    mouse_x = None
    mouse_y = None

    while running: 
        for event in pygame.event.get(): 
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
               running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                chessboard.move_piece((mouse_x, mouse_y))
        
        screen.fill((255,255,255))
        
        # displaying pieces
        for col in range(chessboard.column):
            for row in range(chessboard.Rows):
                square = chessboard.square_objects[row][col]
                square.draw_square(screen)
                square.draw_pieces(screen)

                #highlighting square
                if square == chessboard.start_move_square :
                    pygame.draw.rect( screen, (0,255,0), (col * square.size, row * square.size, square.size, square.size), 4)
                
                if square == chessboard.destination_square:
                    pygame.draw.rect( screen, (255,0,0), (col * square.size, row * square.size, square.size, square.size), 4)
            
                

        #updating the screen
        pygame.display.flip()
        timer.tick(fps)
        
    pygame.quit()

if __name__ == "__main__":
  main()
