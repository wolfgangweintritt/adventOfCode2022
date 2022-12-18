import unittest

from day12.solver import part1


class TestDay12(unittest.TestCase):
    def test_example_input_1(self):
        minSteps = part1('Fixtures/example_input.txt')
        self.assertEqual(31, minSteps)


if __name__ == '__main__':
    unittest.main()
