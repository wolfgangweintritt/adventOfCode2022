import unittest

from day2.solver import main


class TestDay2(unittest.TestCase):
    def test_empty_list(self):
        score = main('Fixtures/empty.txt')
        self.assertEqual(0, score)

    def test_list_example_1(self):
        score = main('Fixtures/small_input_1.txt')
        self.assertEqual(24, score)

    def test_list_example_2(self):
        result = main('Fixtures/small_input_2.txt')
        self.assertEqual(15, result)


if __name__ == '__main__':
    unittest.main()
