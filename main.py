import sys

import pygame
from pygame.locals import *

from game import Game
from graphics import Graphics

game = Game()

graphics = Graphics()
graphics.show_window()

# Event Loop
stopped = False
while not stopped:
    for event in pygame.event.get():
        if event.type == QUIT:
            stopped = True
    if not stopped:
        graphics.draw_board(game.board)

# Clean up and exit the game
pygame.display.quit()
pygame.quit()
sys.exit()
