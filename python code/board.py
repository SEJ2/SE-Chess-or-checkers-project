
import pygame
import pieces

pygame.init()

#setting up the screen display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60

# setting color options for the squares
black = (125, 135, 150)
white = (232,235,239)

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

    #function for drawing pieces on the board
    def draw_pieces(self, surface):
        if self.piece and hasattr(self.piece, "image"):
           resized_image = pygame.transform.scale(self.piece.image, (self.size, self.size))
           surface.blit(resized_image, (self.column * self.size, self.row *self.size))

# creating the board 
class ChessBoard:
     def __init__(self, surface, column = 8, Rows = 8):
         super().__init__()
         self.column = column
         self.Rows = Rows
         self.squares_coordinate = [[None for i in range(self.column)] for i in range(self.Rows)]
         self.square_size = WIDTH // self.column
         self.create_squares(surface)
         self.pieces_starting_position(surface)
         

     def create_squares(self,surface):
         for column in range(self.column):
             for row in range(self.Rows):
               if ( column + row ) %2 == 0:
                   color = black
               else:
                    color = white 
               Square_object = Square(color, self.square_size, column, row,  piece = None)
               #assign it a coordinate and update the list
               self.squares_coordinate [column][row]= Square_object
               Square_object.draw_square(surface) # draw the square
                
    #function for assigning pieces their initial posotion on the board
     def pieces_starting_position(self,surface):
        pieces.create_pieces() 

        #assigning the White pieces in the backrow starting postion
        for col, piece_object in enumerate(pieces.white_backrow):
            piece = pieces.white_backrow[piece_object]
            square = self.squares_coordinate[col][7]
            square.piece = piece
                     
           #assigning the Pawns starting postion
        for col in range(self.column):
            square = self.squares_coordinate[col][6]
            square.piece = pieces.created_piece_objects["WhitePawn"]

         #assigning the Black pieces in the backrow starting postion
        for col, piece_object in enumerate(pieces.black_backrow):
            piece = pieces.black_backrow[piece_object]
            square = self.squares_coordinate[col][0]
            square.piece = piece
                     
           #assigning the the Pawns starting postion
        for col in range(self.column):
            square = self.squares_coordinate[col][1]
            square.piece = pieces.created_piece_objects["BlackPawn"]    
                                 
            

def main():
    running = True
    chessboard = ChessBoard(screen)

    while running: 
        for event in pygame.event.get(): 
        # Check for QUIT event       
            if event.type == pygame.QUIT: 
               running = False

        screen.fill((255,255,255))
        
        # displaying pieces
        for col in range(chessboard.column):
            for row in range(chessboard.Rows):
                square = chessboard.squares_coordinate[col][row]
                square.draw_square(screen)
                square.draw_pieces(screen)

        #updating the screen
        pygame.display.flip()
        timer.tick(fps)
        
    pygame.quit()

if __name__ == "__main__":
  main()
