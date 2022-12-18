from day11.value.operator import Operator


class Operation:
    def __init__(self, operator: Operator, secondArgument: int|str) -> None:
        self.__operator = operator
        self.__secondArgument = secondArgument

    def calculateNew(self, old: int) -> int:
        return self.__operator.calc(old, old if self.__secondArgument == 'old' else self.__secondArgument)
