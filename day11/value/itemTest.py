from day11.value.item import Item
from day11.value.monkey import Monkey


class ItemTest:
    def __init__(self, divisibleBy: int, trueMonkey: Monkey, falseMonkey: Monkey) -> None:
        self.__divisibleBy = divisibleBy
        self.__trueMonkey = trueMonkey
        self.__falseMonkey  = falseMonkey

    def getDivisor(self) -> int:
        return self.__divisibleBy

    def executeTest(self, item: Item) -> Monkey:
        return self.__trueMonkey if item.isDivisibleBy(self.__divisibleBy) else self.__falseMonkey
