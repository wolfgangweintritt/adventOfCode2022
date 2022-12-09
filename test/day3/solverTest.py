import unittest

from day3.solver import part1, part2


class TestDay3(unittest.TestCase):
    def test_small_input_1(self):
        score = part1('Fixtures/small_input_1.txt')
        self.assertEqual(157, score)
        badgesScore = part2('Fixtures/small_input_1.txt')
        self.assertEqual(70, badgesScore)

    def test_small_input_2(self):
        score = part1('Fixtures/small_input_2.txt')
        self.assertEqual(104, score)
        badgesScore = part2('Fixtures/small_input_2.txt')
        self.assertEqual(51, badgesScore)


if __name__ == '__main__':
    unittest.main()
