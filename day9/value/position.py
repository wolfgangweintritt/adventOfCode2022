from day9.value.direction import Direction


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def toString(self):
        return "{}.{}".format(self.x, self.y)

    def moveToDirection(self, direction: Direction):
        if direction == Direction.UP:
            self.y -= 1
        if direction == Direction.DOWN:
            self.y += 1
        if direction == Direction.LEFT:
            self.x -= 1
        if direction == Direction.RIGHT:
            self.x += 1

    def moveAccordingToHeadPosition(self, headPosition: 'Position'):
        diffX = headPosition.x - self.x
        diffY = headPosition.y - self.y
        if abs(diffX) <= 1 and abs(diffY) <= 1: # bordering, nothing to do
            return
        if (diffX == 0): # on same row, just move y
            self.y += (-1 if diffY < 0 else 1)
            return
        if (diffY == 0): # on same column, just move x
            self.x += (-1 if diffX < 0 else 1)
            return

        # move both x and y
        self.x += (-1 if diffX < 0 else 1)
        self.y += (-1 if diffY < 0 else 1)


