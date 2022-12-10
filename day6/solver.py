def main(filePath: str, distinctCharsLength: int) -> int:
    inputFile = open(filePath, 'r')
    input = inputFile.read().rstrip()
    inputFile.close()

    for x in range(0, len(input) - (distinctCharsLength - 1)):
        toCheck = input[x:x + distinctCharsLength]
        if len(list(filter(lambda c: toCheck.count(c) > 1, toCheck))) == 0:
            return x + distinctCharsLength

    return -1


if __name__ == '__main__':
    print(main('input.txt', 4))
    print(main('input.txt', 14))
