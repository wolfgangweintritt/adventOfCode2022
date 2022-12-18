from day11.value.monkey import Monkey


class ItemTest:
    def __init__(self, divisibleBy: int, trueMonkey: Monkey, falseMonkey: Monkey) -> None:
        self.__divisibleBy = divisibleBy
        self.__trueMonkey = trueMonkey
        self.__falseMonkey  = falseMonkey

    def executeTest(self, number: int) -> Monkey:
        return self.__trueMonkey if number % self.__divisibleBy == 0 else self.__falseMonkey
