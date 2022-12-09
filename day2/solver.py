from day2.value.game import Game


def main(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return sum(map(lambda line: lineToPlayer2Score(line), lines))


def lineToPlayer2Score(line: str) -> int:
    game = Game.createFromLine(line)
    return game.scorePlayer2()


if __name__ == '__main__':
    print(main('input.txt'))
