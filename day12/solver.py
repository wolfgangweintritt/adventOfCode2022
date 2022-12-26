# Dijkstra variation
def part1(filePath: str) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()

    map = Map.fromLines(lines)

    map.startNode.distance = 0
    while (currentNode := map.visitUnvisitedSquareWithSmallestDistance()) != map.endNode:
        for neighborNode in map.getUnvisitedNeighbors(currentNode, True):
            map.updateNeighborDistance(currentNode, neighborNode)

    return currentNode.distance


def part2(filePath: str) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()

    map = Map.fromLines(lines)

    # go from E to any a/S (easier than to go from any a/S to E)
    # Start with E instead of S
    map.endNode.distance = 0
    while (currentNode := map.visitUnvisitedSquareWithSmallestDistance()).height != 1: # 1 = a
        for neighborNode in map.getUnvisitedNeighbors(currentNode, False):
            map.updateNeighborDistance(currentNode, neighborNode)

    return currentNode.distance


class Square:
    def __init__(self, x: int, y: int, height: str) -> None:
        if height == 'S':
            height = 'a'
        elif height == 'E':
            height = 'z'
        self.height = ord(height) - 96
        self.x = x
        self.y = y
        self.distance = 2**32

    def toKey(self) -> str:
        return "{}.{}".format(self.x, self.y)

    def __lt__(self, other: 'Square'):
        return self.distance < other.distance

    def isVisitableFrom(self, fromSquare: 'Square', startToFinish: bool):
        if startToFinish:
            return self.height <= fromSquare.height + 1

        return fromSquare.height <= self.height + 1


class Map:
    def __init__(self, unvisitedNodes: dict[str, Square], startNode: Square, endNode: Square):
        self.visitedNodes = {}
        self.unvisitedNodes = unvisitedNodes
        self.startNode = startNode
        self.endNode = endNode

    @classmethod
    def fromLines(cls, lines: list[str]):
        unvisitedNodes = {}
        for lineIdx, line in enumerate(lines):
            for colIdx, square in enumerate(line):
                squareObj = Square(lineIdx, colIdx, square)
                if square == 'S':
                    startNode = squareObj
                if square == 'E':
                    endNode = squareObj
                unvisitedNodes[squareObj.toKey()] = squareObj
        return Map(unvisitedNodes, startNode, endNode)

    def updateNeighborDistance(self, currentNode: Square, neighborNode: Square):
        neighborNode.distance = currentNode.distance + 1

    # visited neighbors can never be found with a shorter distance, so we don't need to worry about them
    def getUnvisitedNeighbors(self, node: Square, startToFinish: bool) -> list[Square]:
        neighborKeys = ["{}.{}".format(node.x - 1, node.y), "{}.{}".format(node.x + 1, node.y), "{}.{}".format(node.x, node.y - 1), "{}.{}".format(node.x, node.y + 1)]
        return list(map(lambda key: self.unvisitedNodes[key], filter(lambda key: key in self.unvisitedNodes and self.unvisitedNodes[key].isVisitableFrom(node, startToFinish), neighborKeys)))

    def visitUnvisitedSquareWithSmallestDistance(self) -> Square:
        neighborWithSmallestDistance = sorted(self.unvisitedNodes.values())[0]
        del self.unvisitedNodes[neighborWithSmallestDistance.toKey()]
        self.visitedNodes[neighborWithSmallestDistance.toKey()] = neighborWithSmallestDistance
        return neighborWithSmallestDistance


if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))
