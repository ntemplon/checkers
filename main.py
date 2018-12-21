import sys

import pygame
from pygame.locals import *

from game import Game
from graphics import Graphics

game = Game()

graphics = Graphics()
graphics.show_window()

moves = Game.ALL_MOVES
print(len(moves))

# Event Loop
stopped = False
while not stopped:
    for event in pygame.event.get():
        if event.type == QUIT:
            stopped = True
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos, graphics.pixel_to_board(pos))
    if not stopped:
        graphics.draw_board(game.board)

# Clean up and exit the game
pygame.display.quit()
pygame.quit()
sys.exit()
