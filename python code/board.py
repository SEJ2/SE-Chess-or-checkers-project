import pygame
pygame.init()
from squares import *
from pieces import *
from game import *

# setting up the screen display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60


# creating the board class
class ChessBoard:
    def __init__(self, surface, column=8, Rows=8):
        self.column = column
        self.Rows = Rows
        self.squares = [[None for i in range(self.column)] for i in range(self.Rows)]
        self.square_size = WIDTH // self.column
        # functions for drawing squares and pieces
        self.create_squares(surface)
        self.pieces_starting_position(screen)
        self.piece_to_move = None
        self.initial_square = None
        self.final_square = None

    # setting color options for the squares
    # creating squares
    def create_squares(self, surface):
        dark = (125, 135, 150)
        light = (232, 235, 239)

        for column in range(self.column):
            for row in range(self.Rows):
                if (column + row) % 2 == 0:
                    color = dark
                else:
                    color = light
                square = Square(color, self.square_size, column, row, piece=None)
                # assign it a coordinate and update the list
                self.squares[column][row] = square
                square.draw_square(surface)  # draw the square

    # funtion to access squares on the board
    def get_square(self, col, row):
        if col >= 0 and col < self.column:
            if row >= 0 and row < self.Rows:
                return self.squares[col][row]

    # function for assigning pieces their initial posotion on the board
    def pieces_starting_position(self, surface):

        # assigning the White pieces in the backrow starting postion
        for col, piece in white_backrow.items():
            square = self.get_square(col, 7)
            square.piece = piece
            print(f"placing {piece.color}_{piece.piece_type} at {col},7")
        # assigning the Pawns starting postion
        for col in range(self.column):
            square = self.get_square(col, 6)
            square.piece = created_pieces["White_Pawn"]

        # assigning the Black pieces in the backrow starting postion
        for col, piece in black_backrow.items():
            square =  self.get_square(col, 0)
            square.piece = piece
            print(f"placing {piece.color}_{piece.piece_type} at {col}, 0")

        # assigning the the Pawns starting postion
        for col in range(self.column):
            square = self.get_square(col, 1)
            square.piece = created_pieces["Black_Pawn"]

    # assigning the valid moves to the pieces
    def assign_valid_moves(self, piece, col, row):

        #getting movement logic for Rooks, Bishop and Queen
        def valid_ranged_moves(valid_moves):
            for increment in valid_moves:
                col_increment, row_increment = increment
                possible_moves_col = col + col_increment
                possible_moves_row = row + row_increment

                while True:
                    if Square.in_range(possible_moves_col, possible_moves_row) and (possible_moves_col, possible_moves_row) != (col, row):
                            possible_square = self.get_square(possible_moves_col, possible_moves_row)
                            
                            if possible_square.is_empty():
                                #if (possible_moves_col, possible_moves_row) != (col, row):
                                    piece.valid_moves.append((possible_moves_col, possible_moves_row))

                            if possible_square.has_piece():
                                if possible_square.piece.color != piece.color:
                                    piece.valid_moves.append((possible_moves_col, possible_moves_row))
                                break                           
                    else: break

                    possible_moves_col += col_increment
                    possible_moves_row += row_increment

        def pawn_moves(possible_moves, pawn_diagonal_moves):
                 
            for possible_moves_col, possible_moves_row in possible_moves:
                    # it can move to any empty square or a square that has an enemy piece
                            if Square.in_range(possible_moves_row):
                                possible_square = self.get_square(possible_moves_col, possible_moves_row)

                                if possible_square.is_empty():
                                    piece.valid_moves.append((possible_moves_col, possible_moves_row))
                                    break
                                if possible_square.row == Pawn_start_row:
                                    possible_moves.extend([(col, row + direction * 2)])
                            
            for diag_col, diag_row in pawn_diagonal_moves:
                        valid_horizontal_square = self.get_square(diag_col, diag_row)
                        if (valid_horizontal_square and valid_horizontal_square.has_piece()):
                            if valid_horizontal_square.piece.color != piece.color:
                                piece.valid_moves.append((diag_col, diag_row))
             
        # initializing valid moves list as empty
        piece.valid_moves = []
        # bound checking to get the clicked square
        if 0 <= col < self.column and 0 <= row < self.Rows:

            # valid direction for Pawn moves
            if piece.piece_type == "Pawn":
                if piece.color == "White":
                    direction = -1
                    Pawn_start_row = 6
                    # getting diagonal sqaure
                    white_diagonal_squares = [(col - 1, row - 1), (col + 1, row - 1)]  
                    possible_moves = [(col, row + direction)] 
                    pawn_moves(possible_moves, white_diagonal_squares)
                # Black Pawn moves
                elif piece.color == "Black":
                    direction = 1
                    # getting diagonal sqaure
                    Black_diagonal_squares = [(col - 1, row + 1), 
                                              (col + 1, row + 1),] 
                    possible_moves = [(col, row + direction)] 
                    pawn_moves(possible_moves,  Black_diagonal_squares)           
            # valid moves for Knights
            if piece.piece_type == "Knight":
                possible_moves = [
                    (col + 2, row + 1),
                    (col + 2, row - 1),
                    (col - 2, row + 1),
                    (col - 2, row - 1),
                    (col + 1, row + 2),
                    (col - 1, row + 2),
                    (col - 1, row - 2),
                    (col + 1, row - 2),
                ]
                # checking that each square is legal and creating the pieces valid moves based on that
                for possible_moves_col, possible_moves_row in possible_moves:
                    # it can move to any empty square or a square thta has an enemy piece
                    if Square.in_range(possible_moves_col, possible_moves_row):
                        possible_square = self.get_square(possible_moves_col, possible_moves_row)
                        if possible_square.is_empty_or_has_enemy(piece.color):
                            piece.valid_moves.append((possible_moves_col, possible_moves_row))

            # valid moves for Bishops
            if piece.piece_type == "Bishop":
                    possible_moves = (
                        [
                            (-1,  1),  # up-right
                            (-1, -1),  # up-left
                            (1,   1),  # down-right
                            (1,  -1),  #down-left
                        ])
                    valid_ranged_moves(possible_moves)
                   
            # valid moves for Rooks
            if piece.piece_type == "Rook":
                    possible_moves = (
                        [
                            (-1, 0),  # up
                            (0,  1),  # left
                            (1,  0),  # down
                            (0, -1),  # right
                        ])
                    valid_ranged_moves(possible_moves)

            # valid moves for Queen is a combination of rooks and bishops
            if piece.piece_type == "Queen":
                    # queen is a combination of Rook and Bishop
                    possible_moves = (
                        [
                            (-1, 0),  # up
                            (0,  1),  # left
                            (1,  0),  # down
                            (0, -1),  # right
                           (-1,  1),  # up-right
                            (-1, -1),  # up-left
                            (1,   1),  # down-right
                            (1,  -1),  #down-left
                        ] )
                    valid_ranged_moves(possible_moves)

            # valid moves for King is one sqaure in each direction
            if piece.piece_type == "King":
                possible_moves = (
                    [
                        (col - 1, row - 1),  # move to top left
                        (col, row - 1),  # move to one square above
                        (col + 1, row - 1),  # move to top right diagonal square
                        (col - 1, row),  # move to the left
                        (col + 1, row),  # move to the right
                        (col - 1, row + 1),  # move to botom left
                        (col, row + 1),  # move to bottom
                        (col + 1, row + 1),  # move tobotom right
                    ]
                )
                for possible_moves_col, possible_moves_row in possible_moves:
                    # it can move to any empty square or a square that has an enemy piece
                            if Square.in_range(possible_moves_col, possible_moves_row):
                                possible_square = self.get_square(possible_moves_col, possible_moves_row)
                                
                                if possible_square.is_empty():
                                    piece.valid_moves.append((possible_moves_col, possible_moves_row))
                                    
                                if possible_square.has_enemy(piece.color):
                                     piece.valid_moves.append((possible_moves_col, possible_moves_row))
                 
    def move_piece(self, initial_square):

        col = initial_square[0] // self.square_size
        row = initial_square[1]  // self.square_size

    #bound checking to get the clicked square
        if  0 <= col < self.column and 0 <= row < self.Rows:
 
            initial_square = self.get_square(col, row)

         #first click for selecting or reselecting a piece
            if initial_square.has_piece() and not self.piece_to_move:
                self.initial_square = initial_square
                self.piece_to_move = self.initial_square.piece
                self.assign_valid_moves(self.piece_to_move, col, row)
                print(f"selected piece {self.piece_to_move.color}_{self.piece_to_move.piece_type}")
                # reselecting a piece
            elif  initial_square.has_piece() and self.piece_to_move and  initial_square.piece.color == self.piece_to_move.color:
                    self.initial_square = initial_square
                    self.piece_to_move = self.initial_square.piece
                    self.assign_valid_moves(self.piece_to_move, col, row)
                    print(f"selected new {self.piece_to_move.piece_type}")

                #moving the piece
            elif self.piece_to_move and (col, row) in self.piece_to_move.valid_moves:
                    
                    self.final_square = self.get_square(col, row)
                    self.final_square.piece = self.initial_square.piece
                    
                    Game.log_move(self.initial_square, self.final_square)
                    self.piece_to_move = None
                    self.initial_square.piece = None

                    #logging the move
                    

            else:
                #if you clicke on an empty square you desselect everything
                print(" empty square")
                self.piece_to_move = None
                self.initial_square = None
            
 







