from enum import Enum
from day2.value.gameResult import GameResult


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def fromString(cls, input: str):
        match (input):
            case 'A' | 'X':
                return Shape.ROCK
            case 'B' | 'Y':
                return Shape.PAPER
            case 'C' | 'Z':
                return Shape.SCISSORS
    def compare(self, x: 'Shape') -> GameResult:
        if (x == Shape.PAPER and self == Shape.ROCK) or (x == Shape.SCISSORS and self == Shape.PAPER) or (x == Shape.ROCK and self == Shape.SCISSORS):
            return GameResult.WIN
        if x == self:
            return GameResult.DRAW

        return GameResult.LOSS
