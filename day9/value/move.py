from day9.value.direction import Direction


class Move:
    def __init__(self, direction: Direction, steps: int) -> None:
        self.direction = direction
        self.steps = steps

    @classmethod
    def fromLine(cls, line: str) -> 'Move':
        lineSplit = line.split(' ')
        return Move(Direction.fromString(lineSplit[0]), int(lineSplit[1]))
