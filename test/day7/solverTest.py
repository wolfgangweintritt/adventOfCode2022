import unittest

from day7.solver import main


class TestDay7(unittest.TestCase):
    def test_example_input_1(self):
        dirSizes = main('Fixtures/example_input.txt', 100000)
        self.assertEqual(95437, dirSizes)


if __name__ == '__main__':
    unittest.main()
