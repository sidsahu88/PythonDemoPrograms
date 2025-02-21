import unittest
from math import pi

from Python_Package_Demo.circle_area import area


class CircleAreaTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(2.1), pi * 2.1 ** 2)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, -2)

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, 2+5j)
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'radius')

# if __name__ == '__main__':
#    unittest.main()
