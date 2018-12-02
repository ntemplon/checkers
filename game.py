from enum import Enum

from controller import *


class Piece:
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    class PieceKind(Enum):
        STANDARD = 0
        KING = 1

    class Team(Enum):
        RED_TEAM = 0
        WHITE_TEAM = 1

    def __init__(self, kind: PieceKind, team: Team):
        self.kind = kind
        self.team = team
        self.color = (0, 255, 0)
        if team == Piece.Team.RED_TEAM:
            self.color = Piece.RED
        elif team == Piece.Team.WHITE_TEAM:
            self.color = Piece.WHITE


class Square:
    def __init__(self, color=(0, 0, 0)):
        super()
        self.piece: Piece = None
        self.color = color


# Coordinates count from (0, 0) as the top left
class Board:
    BEIGE = (244, 218, 157)
    BLACK = (0, 0, 0)

    def __init__(self):
        # Initialize the list to be a 8x8 nested list of squares (hence the constructor call)
        self.squares = [[Square()] * 8] * 8

        # By default, each of the nested lists above will actually be the same list, referenced 8 times.  This fixes
        #  that by assigning each list to be a new, empty list
        for i in range(len(self.squares)):
            self.squares[i] = [None] * 8

        # This is a fancy way of setting a checkerboard pattern, with the top-left square being white
        for x in range(8):
            for y in range(8):
                if self.can_contain_piece(x, y):
                    self.squares[x][y] = Square(Board.BLACK)
                else:
                    self.squares[x][y] = Square(Board.BEIGE)

        for x in range(len(self.squares)):
            for y in range(0, 3):
                if self.can_contain_piece(x, y):
                    self.squares[x][y].piece = Piece(Piece.PieceKind.STANDARD, Piece.Team.RED_TEAM)
            for y in range(5, 8):
                if self.can_contain_piece(x, y):
                    self.squares[x][y].piece = Piece(Piece.PieceKind.STANDARD, Piece.Team.WHITE_TEAM)

    # Pieces can be placed on any black squares
    @staticmethod
    def can_contain_piece(x, y):
        return x % 2 != y % 2


class Move:
    def __init__(self, start_pos=(0, 0), pos_sequence=None):
        if pos_sequence is None:
            pos_sequence = [(0, 0)]
        self.start_pos = start_pos
        self.pos_sequence = pos_sequence


class Game:
    def __init__(self):
        self.board = Board()
        self.red_controller: Controller = PlayerController()
        self.white_controller: Controller = PlayerController()
