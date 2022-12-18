from day11.value.operation import Operation


class Monkey:
    inspectionCount: int
    itemTest: 'ItemTest'
    operation: Operation
    items: list[int]

    def __init__(self) -> None:
        self.items = []
        self.operation = None
        self.itemTest = None
        self.inspectionCount = 0

    def throwItems(self) -> None:
        for item in self.items:
            self.inspectionCount += 1
            newItemValue = int(self.operation.calculateNew(item) / 3)
            monkeyToThrowTo = self.itemTest.executeTest(newItemValue)
            monkeyToThrowTo.catchItem(newItemValue)
        self.items = []

    def catchItem(self, item: int) -> None:
        self.items.append(item)
