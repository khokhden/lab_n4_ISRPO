import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_float(self):
        res = area(2.5, 4)
        self.assertEqual(res, 10.0)

    def test_perimeter_zero(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_int(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_float(self):
        res = perimeter(2.5, 4)
        self.assertEqual(res, 13.0)