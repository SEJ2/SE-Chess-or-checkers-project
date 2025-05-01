import board
import pieces
import pygame

pygame.init()


class Game:
    def __init__(self, active_player, boardstate):
        # setting up to capture the board state at any turn
        self.boardstate = boardstate

        self.active_player = active_player
        self.White_player = board.pieces.color.White
        self.black_player = board.pieces.color.Black
        self.move_log = []
        self.White_player_active = True
        self.Black_player = False

        # initialize on turn 1
        self.turn = 1

    def log_move(self, initial_square, final_square):
        if board.move_piece():
            initial_square = board.initial_square
            final_square = board.final_square
            self.move_log.append(initial_square,final_square)


    def get_active_player(self, color):
        if board.piece.valid_moves is not []:
            return board.piece.color

    # creating a function that assign the active player
    def assign_active_player(self, piece):

        if self.turn == 1:
            # on first turn white move first
            self.active_player == self.White_player

        else:
            self.get_active_player()

            # only active player can move its pieces
        if not self.active_player:
            if board.pieces.color != self.active_player.color:
                piece.valid_moves = []
