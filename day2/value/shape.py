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
    @classmethod
    def fromShapeAndResult(cls, player1Shape: 'Shape', neededResult: GameResult) -> 'Shape':
        player2Shapes = [Shape.ROCK, Shape.PAPER, Shape.SCISSORS]
        return next(filter(lambda player2Shape: player1Shape.compare(player2Shape) == neededResult, player2Shapes))

    def compare(self, x: 'Shape') -> GameResult:
        if (x == Shape.PAPER and self == Shape.ROCK) or (x == Shape.SCISSORS and self == Shape.PAPER) or (x == Shape.ROCK and self == Shape.SCISSORS):
            return GameResult.WIN
        if x == self:
            return GameResult.DRAW

        return GameResult.LOSS
