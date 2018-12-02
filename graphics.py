import pygame


class Graphics:
    def __init__(self, caption="Checkers", frame_rate=60):
        self.caption = caption
        self.frame_rate = frame_rate
        self.fps = 60

        self.window_height = 800
        self.window_width = 800
        self.square_size = int(min(self.window_height, self.window_width) / 8)
        self.circle_radius = int(self.square_size * 0.4)
        self.half_square_size = int(self.square_size / 2)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        self.clock = pygame.time.Clock()

        self.x_off = max(0, int((self.window_width - (self.square_size * 8)) / 2))
        self.y_off = max(0, int((self.window_height - (self.square_size * 8)) / 2))

    def show_window(self):
        pygame.init()
        pygame.display.set_caption(self.caption)

    def draw_board(self, board):
        # Remind the game to run at the indicated framerate
        #  The output of this can be stored in delta_t to get the amount of time that has passed since the last call
        self.clock.tick(self.frame_rate)

        # Clear the board before starting
        self.screen.fill((25, 25, 25))

        for x in range(len(board.squares)):
            for y in range(len(board.squares[x])):
                # Draw Square
                pix_x = x * self.square_size + self.x_off
                pix_y = y * self.square_size + self.y_off
                pygame.draw.rect(self.screen, board.squares[x][y].color, (pix_x, pix_y, self.square_size, self.square_size))

                # Draw Piece
                piece = board.squares[x][y].piece
                if piece is not None:
                    pygame.draw.circle(self.screen, piece.color, (pix_x + self.half_square_size, pix_y + self.half_square_size), self.circle_radius)

        # Make sure we push our updates to the screen!
        pygame.display.update()
