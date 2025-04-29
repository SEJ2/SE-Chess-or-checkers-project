import pygame


class Square:
    def __init__(self, color, size, column, row, piece):
        self.color = color
        self.size = size
        self.column = column
        self.row = row
        self.piece = piece

    def draw_square(self, surface):
        rectangle = pygame.Rect(
            self.column * self.size, self.row * self.size, self.size, self.size
        )
        pygame.draw.rect(surface, self.color, rectangle)

    # functions of square class

    def has_piece(self):
            return self.piece != None
    
    def is_empty(self):
        return not self.has_piece()

    def get_piece(self):
        return self.piece

    def has_ally(self, color):
       return self.piece != None and self.piece.color == color
    
    def has_enemy(self, color):
         return self.piece != None and self.piece.color != color

    def is_empty_or_has_enemy(self, color):
        return  self.has_enemy(color) or self.is_empty()

    # function for drawing pieces on the board
    def draw_pieces(self, surface):
        if self.piece and hasattr(self.piece, "image"):
            resized_image = pygame.transform.scale(
                self.piece.image, (self.size, self.size)
            )
            surface.blit(resized_image, (self.column * self.size, self.row * self.size))

    @staticmethod  # for getting sqaures that are with the valid moves of a selected piece
    def in_range(*args):
        for arg in args:
            if not (0 <= arg <= 7):
                return False
        return True
