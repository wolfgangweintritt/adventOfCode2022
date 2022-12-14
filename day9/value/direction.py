from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @classmethod
    def fromString(cls, direction: str) -> 'Direction':
        match direction:
            case 'U':
                return Direction.UP
            case 'D':
                return Direction.DOWN
            case 'L':
                return Direction.LEFT
            case 'R':
                return Direction.RIGHT
