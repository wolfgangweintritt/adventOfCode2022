import unittest

from day8.solver import part1


class TestDay8(unittest.TestCase):
    def test_example_input_1(self):
        visibleTrees = part1('Fixtures/example_input.txt')
        self.assertEqual(21, visibleTrees)


if __name__ == '__main__':
    unittest.main()
