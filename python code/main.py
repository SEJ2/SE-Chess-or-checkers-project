from board import *
from squares import *
from pieces import *
from game import *
import pygame


def main():
    running = True
    chessboard = ChessBoard(screen)
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

        screen.fill((255, 255, 255))

        # displaying pieces
        for col in range(chessboard.column):
            for row in range(chessboard.Rows):
                square = chessboard.squares[col][row]
                square.draw_square(screen)
                square.draw_pieces(screen)

                # highlighting square
                if square == chessboard.initial_square:
                    pygame.draw.rect(
                        screen,
                        (0, 255, 0),
                        (
                            col * square.size,
                            row * square.size,
                            square.size,
                            square.size,
                        ),
                        4,
                    )
                # highlight moves
                
                if chessboard.piece_to_move:
                    if (col, row) in chessboard.piece_to_move.valid_moves:
                        pygame.draw.rect( screen, (255, 0, 0), ( col * square.size,row * square.size,square.size, square.size, ), 4,)

        # updating the screen
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
