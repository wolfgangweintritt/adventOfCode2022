import unittest

from day8.solver import part1, part2


class TestDay8(unittest.TestCase):
    def test_example_input_1(self):
        visibleTrees = part1('Fixtures/example_input.txt')
        self.assertEqual(21, visibleTrees)
        maxScenicScore = part2('Fixtures/example_input.txt')
        self.assertEqual(8, maxScenicScore)


if __name__ == '__main__':
    unittest.main()
