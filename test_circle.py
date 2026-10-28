import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_area_int(self):
        res = area(3)
        self.assertAlmostEqual(res, 28.274333882308138)

    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.634954084936208)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)

    def test_perimeter_int(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 15.707963267948966)


if __name__ == "__main__":
    unittest.main()
