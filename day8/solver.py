import numpy as numpy


def part1(filePath: str) -> int:
    with open(filePath) as file:
        arr2d = [[int(char) for char in line.rstrip()] for line in file]

    forest = numpy.array(arr2d, int)
    linesOfSight = []
    for los in range(0, 4):
        if len(linesOfSight) <= los:
            linesOfSight.append([])
        for l, line in enumerate(forest):
            if len(linesOfSight[los]) <= l:
                linesOfSight[los].append([])
            for i in range(0, len(line)):
                linesOfSight[los][l].append(onlySmallerOrEqInLineBefore(line, i))
        forest = numpy.rot90(forest)  # rotate forest

    for los in range(1, 4):
        linesOfSight[los] = numpy.rot90(linesOfSight[los], -los)  # rotate line of sight arrays back

    sum = 0
    for lineIdx, line in enumerate(linesOfSight[0]):
        for colIdx, col in enumerate(line):
            if linesOfSight[0][lineIdx][colIdx] or linesOfSight[1][lineIdx][colIdx] or linesOfSight[2][lineIdx][colIdx] or linesOfSight[3][lineIdx][colIdx]:
                sum += 1

    return sum


def onlySmallerOrEqInLineBefore(line: str, idxToCheck: int) -> bool:
    for i in range(0, idxToCheck):
        if line[i] >= line[idxToCheck]:
            return False

    return True


if __name__ == '__main__':
    print(part1('input.txt'))
