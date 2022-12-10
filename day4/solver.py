def part1(filePath: str) -> int:
    inputFile = open(filePath, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    sectionRangePairs = map(lambda line: SectionRangePair.createFromLine(line), lines)
    return len(list(filter(lambda sectionRangePair: sectionRangePair.contains(), sectionRangePairs)))


class SectionRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def contains(self, other: 'SectionRange') -> bool:
        return other.start >= self.start and other.end <= self.end

    @classmethod
    def createFromString(cls, sectionRangeString: str) -> 'SectionRange':
        startEnd = sectionRangeString.split('-')
        return SectionRange(int(startEnd[0]), int(startEnd[1]))


class SectionRangePair:
    def __init__(self, section1: SectionRange, section2: SectionRange) -> None:
        self.section1 = section1
        self.section2 = section2

    @classmethod
    def createFromLine(cls, line: str) -> 'SectionRangePair':
        sections = line.rstrip().split(',')
        return SectionRangePair(SectionRange.createFromString(sections[0]), SectionRange.createFromString(sections[1]))

    def contains(self) -> bool:
        return self.section1.contains(self.section2) or self.section2.contains(self.section1)


if __name__ == '__main__':
    print(part1('input.txt'))
