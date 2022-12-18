from day11.value.operator import Operator


class Operation:
    def __init__(self, operator: Operator, secondArgument: int|str, divideStressLevelBy: int) -> None:
        self.__operator = operator
        self.__secondArgument = secondArgument
        self.__divideStressLevelBy = divideStressLevelBy

    def calculateNew(self, old: int) -> int:
        secondArgument = old if self.__secondArgument == 'old' else self.__secondArgument
        return int(self.__operator.calc(old, secondArgument) / self.__divideStressLevelBy)
