from day9.value.move import Move
from day9.value.position import Position


def part1(filePath: str) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()

    moves = map(lambda line: Move.fromLine(line), lines)

    headPosition = Position(0, 0)
    tailPosition = Position(0, 0)
    visitedTailPositions = {tailPosition.toString()}

    for move in moves:
        for i in range(move.steps):
            headPosition.moveToDirection(move.direction)
            tailPosition.moveAccordingToHeadPosition(headPosition)
            visitedTailPositions.add(tailPosition.toString())

    return len(visitedTailPositions)


if __name__ == '__main__':
    print(part1('input.txt'))
