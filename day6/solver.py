def part1(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    input = inputFile.read().rstrip()
    inputFile.close()

    for x in range(0, len(input) - 3):
        toCheck = input[x:x+4]
        if len(list(filter(lambda c: toCheck.count(c) > 1, toCheck))) == 0:
            return x+4

    return -1

if __name__ == '__main__':
    print(part1('input.txt'))
