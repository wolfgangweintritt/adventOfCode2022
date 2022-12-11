import re
from typing import Optional

from day7.value.file import Dir, File


def part1(filePath: str, maxDirSize: int) -> int:
    rootDir = createDirStructure(filePath)

    return sumDirsWithSizeAtMost(rootDir, maxDirSize)


def part2(filePath: str, diskSpace: int, unusedSpaceNeeded: int) -> int:
    rootDir = createDirStructure(filePath)
    currentlyUnusedSpace = diskSpace - rootDir.getSize()
    unusedSpaceDiff = unusedSpaceNeeded - currentlyUnusedSpace

    return findSmallestDirGteMinSize(rootDir, unusedSpaceDiff).getSize()


def createDirStructure(filePath: str) -> Dir:
    with open(filePath) as f:
        lines = f.read().splitlines()

    currentDir = None
    rootDir = None
    for line in lines:
        if line.startswith('$ cd '):
            if line == '$ cd ..':
                currentDir = currentDir.getParentDir()
            else:
                if currentDir == None:
                    rootDir = currentDir = Dir(line[5:], None)
                else:
                    currentDir = currentDir.getSubDirByName(line[5:])
        elif re.search('^\d', line) != None: # file
            lineSplit = line.split(' ')
            currentDir.addChild(File(lineSplit[1], int(lineSplit[0])))
        elif line.startswith('dir '): # subdir
            currentDir.addChild(Dir(line[4:], currentDir))

    return rootDir


def sumDirsWithSizeAtMost(d: Dir, maxSize: int) -> int:
    sizeSum = 0
    if d.getSize() <= maxSize:
        sizeSum += d.getSize()
    for subdir in d.getSubDirs():
        sizeSum += sumDirsWithSizeAtMost(subdir, maxSize)

    return sizeSum


def findSmallestDirGteMinSize(d: Dir, minDirSize: int) -> Optional['Dir']:
    minDir = d
    for subdir in d.getSubDirs():
        smallestSubdirGteMinSize = findSmallestDirGteMinSize(subdir, minDirSize)
        if (smallestSubdirGteMinSize != None and smallestSubdirGteMinSize.getSize() < minDir.getSize() and smallestSubdirGteMinSize.getSize() >= minDirSize):
            minDir = smallestSubdirGteMinSize

    return minDir if minDir.getSize() >= minDirSize else None


if __name__ == '__main__':
    print(part1('input.txt', 100000))
    print(part2('input.txt', 70000000, 30000000))
