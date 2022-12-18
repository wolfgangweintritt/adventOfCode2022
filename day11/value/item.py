from day11.value.operation import Operation


from typing import Protocol

class Item(Protocol):
    def isDivisibleBy(self, divisor: int) -> bool:
        ...

    def doCalculation(self, operation: Operation) -> None:
        ...


class RemainderItem(Item):
    def __init__(self, remainders: dict[int, int]) -> None:
        self.__remainders = remainders

    def isDivisibleBy(self, divisor: int) -> bool:
        return self.__remainders[divisor] == 0

    def doCalculation(self, operation: Operation) -> None:
        self.__remainders = {divisor: operation.calculateNew(remainder) % divisor for divisor, remainder in self.__remainders.items()}


class SimpleItem(Item):
    def __init__(self, value: int) -> None:
        self.__value = value

    def isDivisibleBy(self, divisor: int) -> bool:
        return self.__value % divisor == 0

    def doCalculation(self, operation: Operation) -> None:
        self.__value = operation.calculateNew(self.__value)
