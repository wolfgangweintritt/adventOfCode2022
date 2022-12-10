import unittest

from day6.solver import part1


class TestDay6(unittest.TestCase):
    def test_example_input_1(self):
        markerPosition = part1('Fixtures/example_input_1.txt')
        self.assertEqual(7, markerPosition)

    def test_example_input_2(self):
        markerPosition = part1('Fixtures/example_input_2.txt')
        self.assertEqual(5, markerPosition)

    def test_example_input_3(self):
        markerPosition = part1('Fixtures/example_input_3.txt')
        self.assertEqual(6, markerPosition)

    def test_example_input_4(self):
        markerPosition = part1('Fixtures/example_input_4.txt')
        self.assertEqual(10, markerPosition)

    def test_example_input_5(self):
        markerPosition = part1('Fixtures/example_input_5.txt')
        self.assertEqual(11, markerPosition)


if __name__ == '__main__':
    unittest.main()
