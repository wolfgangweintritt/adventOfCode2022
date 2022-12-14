import unittest

from day9.solver import part1, part2


class TestDay9(unittest.TestCase):
    def test_example_input_1(self):
        tailVisited = part1('Fixtures/example_input.txt')
        self.assertEqual(13, tailVisited)

    def test_example_input_part2(self):
        tailVisited = part2('Fixtures/example_input_part2.txt')
        self.assertEqual(36, tailVisited)


if __name__ == '__main__':
    unittest.main()
