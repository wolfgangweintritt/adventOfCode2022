from day2.value.game import Game


def part1(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return sum(map(lambda line: lineToPlayer2Score(line), lines))


def lineToPlayer2Score(line: str) -> int:
    game = Game.createFromLine(line)
    return game.scorePlayer2()


def part2(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return sum(map(lambda line: lineToPlayer2ScorePart2(line), lines))


def lineToPlayer2ScorePart2(line: str) -> int:
    game = Game.createFromLinePart2(line)
    return game.scorePlayer2()


if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
