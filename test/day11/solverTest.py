import unittest

from day11.solver import main


class TestDay11(unittest.TestCase):
    def test_example_input_1(self):
        monkeyBusiness = main('Fixtures/example_input.txt', 20, 3)
        self.assertEqual(10605, monkeyBusiness)
        monkeyBusiness = main('Fixtures/example_input.txt', 10000, 1)
        self.assertEqual(2713310158, monkeyBusiness)


if __name__ == '__main__':
    unittest.main()
