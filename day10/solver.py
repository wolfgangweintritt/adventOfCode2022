from functools import reduce


def part1(filePath: str) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()

    moves = map(lambda line: Instruction.fromLine(line), lines)

    registerHistory = []
    registerValue = 1
    for move in moves:
        for c in range(move.cycles):
            registerHistory.append(registerValue)
            if c == move.cycles - 1:
                registerValue += move.addToRegister

    return reduce(
        lambda carry, value: carry + (value[1] * value[0]) if value[0] == 20 or (value[0] - 20) % 40 == 0 else carry,
        zip(list(range(1, len(registerHistory) + 1)), registerHistory),  # tuple (cycle (starting with 1), registerValue)
        0
    )


def part2(filePath: str) -> str:
    with open(filePath) as f:
        lines = f.read().splitlines()

    moves = map(lambda line: Instruction.fromLine(line), lines)

    crt = CRT(40, 1)
    for move in moves:
        for c in range(move.cycles):
            crt.drawPixel()
            if c == move.cycles - 1:
                crt.moveSprite(move.addToRegister)

    return crt.drawMonitor()


class CRT:
    pixels = []

    def __init__(self, screenSize: int, spritePosition: int) -> None:
        self.screenSize = screenSize
        self.spritePosition = spritePosition

    def drawPixel(self) -> None:
        currentLinePixelIdx = len(self.pixels) % self.screenSize
        if abs(currentLinePixelIdx - self.spritePosition) <= 1:
            self.pixels.append('#')
        else:
            self.pixels.append('.')

    def moveSprite(self, addToSpritePosition):
        self.spritePosition += addToSpritePosition

    def drawMonitor(self) -> str:
        monitor = ''
        for idx, pixel in enumerate(self.pixels):
            monitor += pixel
            if (idx + 1) % self.screenSize == 0:
                monitor += '\n'

        return monitor


class Instruction:
    def __init__(self, cycles: int, addToRegister: int) -> None:
        self.cycles = cycles
        self.addToRegister = addToRegister

    @classmethod
    def fromLine(cls, line: str) -> 'Instruction':
        lineSplit = line.split(' ')
        if len(lineSplit) == 1:
            return Instruction(1, 0)
        return Instruction(2, int(lineSplit[1]))


if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
