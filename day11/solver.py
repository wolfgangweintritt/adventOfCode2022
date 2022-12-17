def part1(filePath: str) -> int:
    with open(filePath) as f:
        lines = f.read().splitlines()
    pass


if __name__ == '__main__':
    print(part1('input.txt'))
