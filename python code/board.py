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

        self.piece_selected_to_move = None
        self.initial_square = None

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

        #debugging placement
        black_debuging_square = self.get_square(4,3)
        black_debuging_square.piece = black_backrow.__getitem__(0)

        white_debug_square = self.get_square(3,3)
        white_debug_square.piece = white_backrow.__getitem__(2)

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
            for valid_squares in valid_moves:
                col_increment, row_increment = valid_squares
                possible_moves_col = col + col_increment
                possible_moves_row = row + row_increment

                while True:
                    if Square.in_range(possible_moves_col, possible_moves_row):
                            possible_square = self.get_square(possible_moves_col, possible_moves_row)
                            if possible_square.is_empty:
                                self.piece_selected_to_move.valid_moves.append((possible_moves_col, possible_moves_row))
                               
                            if possible_square.has_enemy(self.piece_selected_to_move.color):
                                self.piece_selected_to_move.valid_moves.append((possible_moves_col, possible_moves_row))
                                break

                            if possible_square.has_ally(self.piece_selected_to_move.color):
                                break
                    else: break

                    possible_moves_col = col + col_increment
                    possible_moves_row = row + row_increment 

        # initializing valid moves list as empty
        piece.valid_moves = []
        # bound checking to get the clicked square
        if 0 <= col < self.column and 0 <= row < self.Rows:

            # valid direction for Pawn moves
            # White Pawn moves
            if piece.piece_type == "Pawn":
                if piece.color == "White":
                    direction = -1
                    Pawn_start_row = 6

                    # getting diagonal sqaure
                    white_diagonal_squares = [
                        (col - 1, row - 1),  # left diagonal square,
                        (col + 1, row - 1),  # right diagonal square
                    ]

                    if row == Pawn_start_row:
                        piece.valid_moves.extend([(col, row + direction)])
                        piece.valid_moves.extend([(col, row + direction * 2)])
                        
                    else:
                        piece.valid_moves.extend([(col, row + direction)])
                        

                    # adding diagonal pawn move if it is diagonal to it and has an enemy
                    for diag_col, diag_row in white_diagonal_squares:
                        valid_horizaontal_square = self.get_square(diag_col, diag_row)

                        if (valid_horizaontal_square and valid_horizaontal_square.has_piece()):
                            if valid_horizaontal_square.piece.color != piece.color:
                                piece.valid_moves.append((diag_col, diag_row))

                # Black Pawn moves
                elif piece.color == "Black":
                    direction = 1
                    Pawn_start_row = 1
                    # getting diagonal sqaure
                    Black_diagonal_squares = [(col - 1, row + 1), (col + 1, row + 1)]
                    if row == Pawn_start_row:
                        # setting the pawn to move only one direction but optionally two if its on its first row
                        
                        piece.valid_moves.extend([(col, row + direction)])
                        piece.valid_moves.extend([(col, row + direction * 2)])

                    else:
                        piece.valid_moves.extend([(col, row + direction)])
                        

                    # adding diagonal pawn move if it enemy is diagonal to it
                    for diag_col, diag_row in Black_diagonal_squares:
                        valid_horizaontal_square = self.get_square(diag_col, diag_row)
                        if valid_horizaontal_square and valid_horizaontal_square.has_piece():
                            if valid_horizaontal_square.piece.color != piece.color:
                                piece.valid_moves.append((diag_col, diag_row))
            pass
            # valid moves for Knights
            if self.piece_selected_to_move.piece_type == "Knight":
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
                        if possible_square.is_empty_or_has_enemy(self.piece_selected_to_move.color):
                            self.piece_selected_to_move.valid_moves.append((possible_moves_col, possible_moves_row))


            # valid moves for Bishops
            elif piece.piece_type == "Bishop":
                    possible_moves = (
                        [
                            (col - 1, row - 1),  # getting all top left diagonal sqaures
                            (col + 1, row - 1),  # getting all top right diagonal sqaures
                            (col - 1, row + 1),  # getting all bottom left diagonal sqaures
                            (col + 1, row + 1),  # getting all botoom right diagonal sqaures
                        ]
                    )
                    valid_ranged_moves(possible_moves)
                   
            # valid moves for Rooks
            elif piece.piece_type == "Rook":
                    possible_moves = (
                        [
                            (col - 1, row),  # getting all squares left  of it
                            (col + 1, row),  # getting all squares right of it
                            (col, row + 1),  # getting all squares above of it
                            (col, row - 1),  # getting all squares below of it
                        ])

            # valid moves for Queen is a combination of rooks and bishops
            elif piece.piece_type == "Queen":
                    # queen is a combination of Rook and Bishop
                    possible_moves = (
                        [
                            (col - 1, row),  # getting all squares left  of it
                            (col + 1, row),  # getting all squares right of it
                            (col, row + 1),  # getting all squares above of it
                            (col, row - 1),  # getting all squares below of it
                            (col - 1, row - 1),  # getting all top left diagonal sqaures
                            (col + 1, row - 1),  # getting all top right diagonal sqaures
                            (col - 1, row + 1),  # getting all bottom left diagonal sqaures
                            (col + 1, row + 1),  # getting all botoom right diagonal sqaures
                        ] )

            # valid moves for King is one sqaure in each direction
            elif piece.piece_type == "King":
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
                    # it can move to any empty square or a square thta has an enemy piece
                        if Square.in_range(possible_moves_col, possible_moves_row):
                            possible_square = self.get_square(possible_moves_col, possible_moves_row)
                            if possible_square.is_empty_or_has_enemy(self.piece_selected_to_move.color):
                                self.piece_selected_to_move.valid_moves.append((possible_moves_col, possible_moves_row))
                            elif possible_square.has_ally(piece.color):
                                print("{self.piece} is blocked") 
                                break
                        break 

    def move_piece(self, position):#(self, piece, initial_square, destination sqaure)

        clicked_col = position[0] // self.square_size
        clicked_row = position[1] // self.square_size

        # bound checking to get the clicked square
        if 0 <= clicked_col < self.column and 0 <= clicked_row < self.Rows:

            # 1st click on your piece it gets selected and highlights possible moves
            initial_square = self.get_square(clicked_col, clicked_row)#(clicked_col, clicked_row)
            
            # check if a square has a piece of it
            # select the piece on the square
            if initial_square.has_piece:
                self.initial_square = initial_square
                self.piece_selected_to_move = initial_square.get_piece()

                if self.piece_selected_to_move is not None:
                    self.assign_valid_moves(self.piece_selected_to_move, self.initial_square.column, self.initial_square.row,)
                    # this square become the initial square where we assign legal moves for the piece from
                    print( f"{self.piece_selected_to_move.piece_type} valid moves: {self.piece_selected_to_move.valid_moves}")

            elif self.piece_selected_to_move is not None:
                    for i in self.piece_selected_to_move.valid_moves:
                        destination_square = self.get_square(clicked_col, clicked_row)
                        if  destination_square ==  i:
                    # the piece moves to the next square we click if it is in the pieces valid moves list
                    # Swap the values of variable to make the move
                            self.initial_square.piece, destination_square.piece = destination_square.piece, self.initial_square.piece
                        #clearing movement managment variables
                            self.piece_selected_to_move = None
                            self.initial_square = None
                            self.initial_square.piece = None
                            print(f"Moved {self.piece_selected_to_move.piece_type} to ({clicked_col})({clicked_row})" )

                        else:
                            print(f"invalid move")
            else:
                print( "clicked on empty square no piece selected, click on  a sqaure with a piece to select it")