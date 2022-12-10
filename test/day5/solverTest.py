import unittest

from day5.solver import main


class TestDay5(unittest.TestCase):
    def test_example_input(self):
        topCrates = main('Fixtures/example_input.txt', True)
        self.assertEqual('CMZ', topCrates)
        topCrates = main('Fixtures/example_input.txt', False)
        self.assertEqual('MCD', topCrates)

    def test_small_input(self):
        topCrates = main('Fixtures/small_input.txt', True)
        self.assertEqual('FDC', topCrates)
        topCrates = main('Fixtures/small_input.txt', False)
        self.assertEqual('ADF', topCrates)


if __name__ == '__main__':
    unittest.main()
