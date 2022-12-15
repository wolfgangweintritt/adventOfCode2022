import unittest

from day10.solver import part1, part2


class TestDay10(unittest.TestCase):
    def test_example_input_1(self):
        signalStrengthSum = part1('Fixtures/example_input.txt')
        self.assertEqual(13140, signalStrengthSum)
        monitorOutput = part2('Fixtures/example_input.txt')
        self.assertEqual("""##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""", monitorOutput)

if __name__ == '__main__':
    unittest.main()
