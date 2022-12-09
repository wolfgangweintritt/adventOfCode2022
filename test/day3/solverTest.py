import unittest

from day3.solver import main


class TestDay3(unittest.TestCase):
    def test_small_input_1(self):
        score = main('Fixtures/small_input_1.txt')
        self.assertEqual(157, score)

    def test_small_input_2(self):
        score = main('Fixtures/small_input_2.txt')
        self.assertEqual(104, score)


if __name__ == '__main__':
    unittest.main()
