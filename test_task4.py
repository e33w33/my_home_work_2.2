import unittest
import math
from task4 import circle_area
pi = math.pi


class TestSphereVolume(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(5), 4/3*pi*5**3)
        self.assertAlmostEqual(circle_area(3.7), 4/3*pi*3.7**3)
        self.assertAlmostEqual(circle_area(1), 4/3*pi)

    def test_string(self): self.assertRaises(ValueError, circle_area, 'four')
    def test_negative(self): self.assertEqual(circle_area(-5), 'Радиус сферы не может быть отрицательным')


if __name__ == '__main__':
    unittest.main()