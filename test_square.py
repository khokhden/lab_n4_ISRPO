import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_area_float(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_int(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)


if __name__ == "__main__":
    unittest.main()
