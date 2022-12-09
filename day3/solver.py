def part1(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    commonItems = map(lambda line: itemScore(findCommonItem(splitLine(line))), lines)
    return sum(commonItems)


def part2(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    triples = []
    for c in range(0, len(lines), 3):
        triples.append(lines[c:c+3])
    badges = map(lambda triple: itemScore(findCommonItem(triple)), triples)
    return sum(badges)


def splitLine(line: str) -> list[str]:
    splitPoint = int ((len(line.rstrip()))/2)
    return [line[:splitPoint], line[splitPoint:]]


def findCommonItem(itemList: list[str]) -> str:
    return next(filter(lambda item: findCommonItemList(item, itemList[1:]), itemList[0]))


def findCommonItemList(item: str, rucksacks: list[str]) -> bool:
    return len(list(filter(lambda rucksack: rucksack.find(item) > -1, rucksacks))) == len(rucksacks)


def itemScore(item: str) -> int:
    intAsciiValue = ord(item[0])
    # a => 97; A => 65
    return intAsciiValue - 96 if intAsciiValue >= 97 else intAsciiValue - (64 - 26)


if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
