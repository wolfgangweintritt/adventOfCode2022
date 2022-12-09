def main(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    commonItems = map(lambda line: itemScore(findCommonItem(splitLine(line))), lines)
    return sum(commonItems)


def splitLine(line: str) -> tuple[str, str]:
    splitPoint = int ((len(line.rstrip()))/2)
    return line[:splitPoint], line[splitPoint:]


def findCommonItem(lineSplit: tuple[str, str]) -> str:
    return next(filter(lambda item: lineSplit[1].find(item) > -1, lineSplit[0]))


def itemScore(item: str) -> int:
    intAsciiValue = ord(item[0])
    # a => 97; A => 65
    return intAsciiValue - 96 if intAsciiValue >= 97 else intAsciiValue - (64 - 26)


if __name__ == '__main__':
    print(main('input.txt'))
