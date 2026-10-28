import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 10)
        self.assertEqual(res, 0.0)

    def test_area_int(self):
        res = area(3, 4)
        self.assertEqual(res, 6.0)

    def test_area_float(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 5.0)

    def test_perimeter_zero(self):
        res = perimeter(0, 4, 3)
        self.assertEqual(res, 7)

    def test_perimeter_int(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = perimeter(2.5, 4, 6)
        self.assertEqual(res, 12.5)


if __name__ == "__main__":
    unittest.main()
