import time
from functools import reduce


def main(filePath: str, topElves: int) -> int:
    with open(filePath) as fp:
        elves = fp.read().rstrip().split('\n\n')

        sumElves = list(map(lambda elveStr: elveToScore(elveStr), elves))

        return sum(sorted(sumElves)[-topElves:])


def elveToScore(elveStr: str) -> int:
    return reduce(lambda carry, elve: carry + int(elve) if elve.isdigit() else 0, elveStr.split('\n'), 0)


if __name__ == '__main__':
    start_time = time.time()
    print(main('input.txt', 1))
    print("--- %s seconds ---" % (time.time() - start_time))

    print(main('input.txt', 3))
    print("--- %s seconds ---" % (time.time() - start_time))
