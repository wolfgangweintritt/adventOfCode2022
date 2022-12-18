from day11.value.itemTest import ItemTest
from day11.value.monkey import Monkey
from day11.value.operation import Operation
from day11.value.operator import Operator


def part1(filePath: str, rounds: int) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()

    lines = list(map(lambda line: line.strip(), lines))
    monkeys = parseInput(lines)

    for round in range(0, rounds):
        for monkey in monkeys:
            monkey.throwItems()

    monkeyInspectionCount = sorted(list(map(lambda monkey: monkey.inspectionCount, monkeys)))
    monkeyInspectionCount.reverse()
    return monkeyInspectionCount[0] * monkeyInspectionCount[1]


def parseInput(lines: list[str]) -> list[Monkey]:
    divisibleBy = 0
    trueMonkey = 0
    falseMonkey = 0
    # create list of monkeys first, since they are referenced in ItemTest (monkey to throw the item to)
    monkeys = [Monkey() for i in range(0, int((len(lines) + 1) / 7))]

    # append extra line s.t. last monkey object is also finished
    lines.append('')
    monkeyId = 0
    for line in lines:
        if line == '':
            monkeys[monkeyId].itemTest = ItemTest(divisibleBy, trueMonkey, falseMonkey)
            monkeyId += 1
        if line.startswith('Starting items:'):
            lineSplit = line.split(':')
            monkeys[monkeyId].items = list(map(lambda item: int(item), lineSplit[1].split(',')))
        if line.startswith('Operation:'):
            lineSplit = line.split('=')
            splitCalc = lineSplit[1].strip().split(' ')
            monkeys[monkeyId].operation = Operation(Operator(splitCalc[1]), int(splitCalc[2]) if splitCalc[2].isnumeric() else splitCalc[2])
        if line.startswith('Test:'):
            divisibleBy = int(line.split(' ')[-1])
        if line.startswith('If true:'):
            trueMonkey = monkeys[int(line.split(' ')[-1])]
        if line.startswith('If false:'):
            falseMonkey = monkeys[int(line.split(' ')[-1])]

    return monkeys


if __name__ == '__main__':
    print(part1('input.txt', 20))
