import unittest

from day2.solver import part1, part2


class TestDay2(unittest.TestCase):
    def test_empty_list(self):
        score = part1('Fixtures/empty.txt')
        self.assertEqual(0, score)

    def test_list_example_1(self):
        score = part1('Fixtures/small_input_1.txt')
        self.assertEqual(24, score)
        score = part2('Fixtures/small_input_1.txt')
        self.assertEqual(15, score)

    def test_list_example_2(self):
        score = part1('Fixtures/small_input_2.txt')
        self.assertEqual(15, score)
        score = part2('Fixtures/small_input_2.txt')
        self.assertEqual(12, score)


if __name__ == '__main__':
    unittest.main()
