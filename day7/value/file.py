from typing import Optional


class FileInterface:
    name = ''

    def getSize(self) -> int:
        pass


class File(FileInterface):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def getSize(self) -> int:
        return self.size


class Dir(FileInterface):
    def __init__(self, name: str, parent: Optional['Dir']):
        self.name = name
        self.parent = parent
        self.children = {}

    def getSize(self) -> int:
        return sum(list(map(lambda c: c.getSize(), self.children.values())))

    def addChild(self, child: FileInterface):
        self.children[child.name] = child

    def getSubDirs(self) -> list['Dir']:
        return list(filter(lambda c: isinstance(c, Dir), self.children.values()))

    def getParentDir(self) -> Optional['Dir']:
        return self.parent

    def getSubDirByName(self, subDirName) -> 'Dir':
        return self.children[subDirName]
