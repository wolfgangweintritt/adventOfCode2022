import unittest

from day5.solver import part1


class TestDay5(unittest.TestCase):
    def test_example_input(self):
        containsCount = part1('Fixtures/example_input.txt')
        self.assertEqual('CMZ', containsCount)

    def test_small_input(self):
        containsCount = part1('Fixtures/small_input.txt')
        self.assertEqual('FDC', containsCount)


if __name__ == '__main__':
    unittest.main()
