import unittest

from day7.solver import part1, part2


class TestDay7(unittest.TestCase):
    def test_example_input_1(self):
        dirSizes = part1('Fixtures/example_input.txt', 100000)
        self.assertEqual(95437, dirSizes)
        smallestDirGteMinSize = part2('Fixtures/example_input.txt', 70000000, 30000000)
        self.assertEqual(24933642, smallestDirGteMinSize)

    def test_simple_input_1(self):
        smallestDirGteMinSize = part2('Fixtures/simple_input_1.txt', 30, 4)
        self.assertEqual(4, smallestDirGteMinSize)
        smallestDirGteMinSize = part2('Fixtures/simple_input_1.txt', 41, 20)
        self.assertEqual(10, smallestDirGteMinSize)
        smallestDirGteMinSize = part2('Fixtures/simple_input_1.txt', 40, 20)
        self.assertEqual(10, smallestDirGteMinSize)
        smallestDirGteMinSize = part2('Fixtures/simple_input_1.txt', 39, 20)
        self.assertEqual(11, smallestDirGteMinSize)
        smallestDirGteMinSize = part2('Fixtures/simple_input_1.txt', 38, 20)
        self.assertEqual(13, smallestDirGteMinSize)
        smallestDirGteMinSize = part2('Fixtures/simple_input_1.txt', 37, 20)
        self.assertEqual(13, smallestDirGteMinSize)

if __name__ == '__main__':
    unittest.main()
