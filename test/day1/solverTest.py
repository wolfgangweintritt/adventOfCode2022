import unittest

from day1.solver import main


class TestDay1(unittest.TestCase):
    def test_empty_list(self):
        result = main('Fixtures/empty.txt', 1)
        self.assertEqual(0, result)

    def test_list_example_1(self):
        result = main('Fixtures/small_input_1.txt', 1)
        self.assertEqual(3000, result)

    def test_list_example_2(self):
        result = main('Fixtures/small_input_2.txt', 1)
        self.assertEqual(12000, result)

    def test_list_example_3(self):
        result = main('Fixtures/small_input_3.txt', 1)
        self.assertEqual(10, result)
        result = main('Fixtures/small_input_3.txt', 3)
        self.assertEqual(27, result)


if __name__ == '__main__':
    unittest.main()
