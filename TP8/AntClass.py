from enum import Enum

class Direction(Enum):
    TOP = 1
    BOT = 2
    RIGHT = 3
    LEFT = 4

class Turn(Enum):
    LEFT = 0
    RIGHT = 1
    AHEAD = 2