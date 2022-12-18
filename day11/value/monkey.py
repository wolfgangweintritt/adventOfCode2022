from day11.value.item import Item
from day11.value.operation import Operation


class Monkey:
    inspectionCount: int
    itemTest: 'ItemTest'
    operation: Operation
    items: list[Item]

    def __init__(self) -> None:
        self.items = []
        self.operation = None
        self.itemTest = None
        self.inspectionCount = 0

    def throwItems(self) -> None:
        for item in self.items:
            self.inspectionCount += 1
            item.doCalculation(self.operation)
            monkeyToThrowTo = self.itemTest.executeTest(item)
            monkeyToThrowTo.catchItem(item)
        self.items = []

    def catchItem(self, item: Item) -> None:
        self.items.append(item)
