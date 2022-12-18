from day11.value.item import Item, RemainderItem, SimpleItem
from day11.value.itemTest import ItemTest
from day11.value.monkey import Monkey
from day11.value.operation import Operation
from day11.value.operator import Operator


def main(filePath: str, rounds: int, divideStressLevelBy: int) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()

    lines = list(map(lambda line: line.strip(), lines))
    monkeys = parseInput(lines, divideStressLevelBy)

    for round in range(0, rounds):
        for monkey in monkeys:
            monkey.throwItems()

    monkeyInspectionCount = sorted(list(map(lambda monkey: monkey.inspectionCount, monkeys)))
    monkeyInspectionCount.reverse()
    return monkeyInspectionCount[0] * monkeyInspectionCount[1]


def parseInput(lines: list[str], divideStressLevelBy: int) -> list[Monkey]:

    # create list of monkeys first, since they are referenced in ItemTest (monkey to throw the item to)
    monkeys = [Monkey() for i in range(0, int((len(lines) + 1) / 7))]

    # append extra line s.t. last monkey object is also finished
    lines.append('')
    divisibleBy = 0
    trueMonkey = 0
    falseMonkey = 0
    itemTests = []
    for line in lines:
        if line == '':
            itemTests.append(ItemTest(divisibleBy, trueMonkey, falseMonkey))
        if line.startswith('Test:'):
            divisibleBy = int(line.split(' ')[-1])
        if line.startswith('If true:'):
            trueMonkey = monkeys[int(line.split(' ')[-1])]
        if line.startswith('If false:'):
            falseMonkey = monkeys[int(line.split(' ')[-1])]

    monkeyId = 0
    divisors = list(map(lambda itemTest: itemTest.getDivisor(), itemTests))
    for line in lines:
        if line == '':
            monkeys[monkeyId].itemTest = itemTests[monkeyId]
            monkeyId += 1
        if line.startswith('Starting items:'):
            lineSplit = line.split(':')
            if divideStressLevelBy == 1:
                monkeys[monkeyId].items = list(map(lambda itemValue: RemainderItem({divisor: int(itemValue) % divisor for divisor in divisors}), lineSplit[1].split(',')))
            else:
                monkeys[monkeyId].items = list(map(lambda itemValue: SimpleItem(int(itemValue)), lineSplit[1].split(',')))
        if line.startswith('Operation:'):
            lineSplit = line.split('=')
            splitCalc = lineSplit[1].strip().split(' ')
            monkeys[monkeyId].operation = Operation(Operator(splitCalc[1]), int(splitCalc[2]) if splitCalc[2].isnumeric() else splitCalc[2], divideStressLevelBy)

    return monkeys


if __name__ == '__main__':
    print(main('input.txt', 20, 3))
    print(main('input.txt', 10000, 1))
