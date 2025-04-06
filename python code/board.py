import chess
import chess.engine
import pygame
#import pieces

pygame.init

#setting up the screen display

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60

# setting color options for the squares
black = (0,0,0)
white = (255,255,255)

class Square:
    def __init__(self, color, size, column, row,  piece = None):
       self.color = color
       self.size = size
       self.column = column 
       self.row = row    
       self.piece = piece
       self.size = size    

    def draw_square(self, surface):
        rectangle = pygame.Rect(self.column * self.size, self.row * self.size, self.size, self.size)
        pygame.draw.rect(surface, self.color, rectangle)

# function for drawing pieces
   # def draw_pieces:
   #   if self.piece == None:
         # Square.piece = piece_object{}

# creating the board 
class board(chess.Board):
     def __init__(self, surface, column = 8, Rows = 8):
         super().__init__()
         self.column = column
         self.Rows = Rows
         self.squares_coordinate = [ 
             [None for all in range(self.column)] for all in range(self.Rows)
             ]
         self.square_size = WIDTH // self.column
         self.create_squares(surface)

     def create_squares(self,surface):
         for column in range(self.column):
             for row in range(self.Rows):
               if ( column + row ) %2 == 0:
                   color = black
               else :
                    color = white 
               Square_object = Square(color, self.square_size, column, row,  piece = None)
               Square_object.draw_square(surface) # draw the square
                #assign it a coordinate and update the list
               self.squares_coordinate [column][row]= Square_object
            

def main():
    running = True
    chessboard = board(screen)

    while running: 
        for event in pygame.event.get(): 
        # Check for QUIT event       
            if event.type == pygame.QUIT: 
               running = False

        screen.fill((255,255,255))
        chessboard.create_squares(screen)
        #updating the screen
        pygame.display.flip()

        timer.tick(fps)
    pygame.quit()

if __name__ == "__main__":
  main()