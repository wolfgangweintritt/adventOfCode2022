import unittest

from day4.solver import part1, part2


class TestDay4(unittest.TestCase):
    def test_example_input(self):
        containsCount = part1('Fixtures/example_input.txt')
        self.assertEqual(2, containsCount)
        overlapsCount = part2('Fixtures/example_input.txt')
        self.assertEqual(4, overlapsCount)

    def test_small_input(self):
        containsCount = part1('Fixtures/small_input.txt')
        self.assertEqual(7, containsCount)
        overlapsCount = part2('Fixtures/small_input.txt')
        self.assertEqual(7, overlapsCount)


if __name__ == '__main__':
    unittest.main()
