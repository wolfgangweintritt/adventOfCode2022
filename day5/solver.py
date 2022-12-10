import re


def main(filePath: str, reverse: bool) -> str:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()

    lines = list(map(lambda line: line.rstrip('\n'), lines))

    numberOfStacks = int((len(lines[0]) + 1) / 4)
    stacks = [[] for i in range(numberOfStacks)]
    moves = []
    for line in lines:
        if line.startswith(' 1') or line == '':
            continue
        if line.startswith('move'):
            moves.append(Move.fromLine(line))
        else:
            for x in range(0, len(line), 4):
                crate = line[x + 1]
                if crate != ' ':
                    stacks[int(x / 4)].append(crate)

    # need to reverse stacks...
    for stack in stacks:
        stack.reverse()

    for move in moves:
        fromStack = stacks[move.fromColumn]
        toStack = stacks[move.toColumn]
        cratesToMove = fromStack[-move.amount:]
        if reverse:
            cratesToMove.reverse()
        toStack.extend(cratesToMove)
        fromStack[len(fromStack) - move.amount:] = []

    return ''.join(list(map(lambda stack: stack[-1], stacks)))


class Move:
    amount = None
    fromColumn = None
    toColumn = None

    def __init__(self, amount: int, fromColumn: int, toColumn: int) -> None:
        self.amount = amount
        self.fromColumn = fromColumn
        self.toColumn = toColumn

    @classmethod
    def fromLine(cls, line: str):
        numbers = re.findall('[0-9]+', line)
        return Move(int(numbers[0]), int(numbers[1]) - 1, int(numbers[2]) - 1)


if __name__ == '__main__':
    print(main('input.txt', True))
    print(main('input.txt', False))
