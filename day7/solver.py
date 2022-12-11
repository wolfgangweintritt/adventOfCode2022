import re

from day7.value.file import Dir, File


def main(filePath: str, maxDirSize: int) -> int:
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

    return sumDirsWithSizeAtMost(rootDir, maxDirSize)

def sumDirsWithSizeAtMost(d: Dir, maxSize: int):
    sizeSum = 0
    if d.getSize() <= maxSize:
        sizeSum += d.getSize()
    for s in d.getSubDirs():
        sizeSum += sumDirsWithSizeAtMost(s, maxSize)

    return sizeSum



if __name__ == '__main__':
    print(main('input.txt', 100000))
