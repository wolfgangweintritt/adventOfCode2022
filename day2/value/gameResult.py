from enum import Enum


class GameResult(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def fromString(cls, result):
        match result:
            case 'X':
                return GameResult.LOSS
            case 'Y':
                return GameResult.DRAW
            case 'Z':
                return GameResult.WIN
