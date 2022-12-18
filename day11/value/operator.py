from enum import Enum


class Operator(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'

    def calc(self, a1: int, a2: int) -> int:
        if self == self.PLUS:
            return a1 + a2
        if self == self.MINUS:
            return a1 - a2
        if self == self.MULTIPLY:
            return a1 * a2
