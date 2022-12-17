import unittest

from day11.solver import part1


class TestDay11(unittest.TestCase):
    def test_example_input_1(self):
        monkeyBusiness = part1('Fixtures/example_input.txt')
        self.assertEqual(10605, monkeyBusiness)


if __name__ == '__main__':
    unittest.main()
