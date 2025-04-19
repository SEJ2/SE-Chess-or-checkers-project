import board
import pieces
import pygame

pygame.init()

class Game:
    def __init__(self, turn, active_player, boardstate):

             #setting up oto capture the board state at any turn
             self.turn = turn
             self.active_player = active_player
             self.boardstate = boardstate
             
             #initialize on turn 1
             turn = 1
             #self.move_pattern(self,piece)
            
#creating a function that assign the active player
    def assign_active_player(self,piece):
            
            White_player = board.pieces.color.White
            black_player = board.pieces.color.Black

            White_player_active = False
            Black_player = False

            if self.turn == 1:
                   # on first turn white move first
                   self.active_player == White_player

            else:
                   self.active_player == White_player
                   # only active player can move its pieces
            if self.active_player:
                #get that players pieces color
                board.pieces.color = self.active_player
                #allow them to move
                           
                   # switch to other player after every active player move its pieces
      