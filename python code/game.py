import board
import pieces
import pygame

pygame.init()

class Move:
    def __init__(self, piece, events, col, row, move_pattern):
             self.piece = piece 
             self.events = pygame.event.get()
             #setting up origin and destination
             self.current_sqaure = board.ChessBoard.squares_coordinate[[col][row]]
             self.destination = None
             #self.move_pattern(self,piece)
            
#creating a function that assign the specific move patter to each piece that exist
    def assign_move_pattern(self,piece):
            if piece == "king":
               move_pattern = 1

            elif  piece == "Knight":
              move_pattern = 3

            elif  piece == "Bishop":
              move_pattern = 5  

            elif  piece == "Rook":
              move_pattern = 5

            elif  piece == "Queen":
                move_pattern = 7 

            else:  
              move_pattern = 1
            
             
#actually isueing a move order to the piece
    def move_piece(self, piece):
         #get the destination sqaure
         #check if a piece exist at destination

         # move the piece if sqaure is empty or has oposite color

         # do not move to destination if it has same color piece
         
          pass 