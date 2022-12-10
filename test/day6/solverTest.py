import unittest

from day6.solver import main


class TestDay6(unittest.TestCase):
    def test_example_input_1(self):
        markerPosition = main('Fixtures/example_input_1.txt', 4)
        self.assertEqual(7, markerPosition)
        markerPosition = main('Fixtures/example_input_1.txt', 14)
        self.assertEqual(19, markerPosition)

    def test_example_input_2(self):
        markerPosition = main('Fixtures/example_input_2.txt', 4)
        self.assertEqual(5, markerPosition)
        markerPosition = main('Fixtures/example_input_2.txt', 14)
        self.assertEqual(23, markerPosition)

    def test_example_input_3(self):
        markerPosition = main('Fixtures/example_input_3.txt', 4)
        self.assertEqual(6, markerPosition)
        markerPosition = main('Fixtures/example_input_3.txt', 14)
        self.assertEqual(23, markerPosition)

    def test_example_input_4(self):
        markerPosition = main('Fixtures/example_input_4.txt', 4)
        self.assertEqual(10, markerPosition)
        markerPosition = main('Fixtures/example_input_4.txt', 14)
        self.assertEqual(29, markerPosition)

    def test_example_input_5(self):
        markerPosition = main('Fixtures/example_input_5.txt', 4)
        self.assertEqual(11, markerPosition)
        markerPosition = main('Fixtures/example_input_5.txt', 14)
        self.assertEqual(26, markerPosition)


if __name__ == '__main__':
    unittest.main()
