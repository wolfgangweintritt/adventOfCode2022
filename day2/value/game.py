from day2.value.shape import Shape


class Game:
    def __init__(self, player1: Shape, player2: Shape):
        self.player1 = player1
        self.player2 = player2

    @classmethod
    def createFromLine(cls, line: str):
        splitLine = line.rstrip().split(' ')
        return Game(Shape.fromString(splitLine[0]), Shape.fromString(splitLine[1]))

    def scorePlayer2(self) -> int:
        gameResult = self.player1.compare(self.player2)
        return gameResult.value + self.player2.value
