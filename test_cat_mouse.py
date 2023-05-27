import unittest
from cat_mouse import catAndMouse


class CatMouseTestCase(unittest.TestCase):
    def test_catAndMouse_cat_a(self):
        self.assertEqual(catAndMouse(4, 1, 3), "Cat A")

    def test_catAndMouse_cat_b(self):
        self.assertEqual(catAndMouse(1, 2, 3), "Cat B")

    def test_catAndMouse_mouse_c(self):
        self.assertEqual(catAndMouse(1, 3, 2), "Mouse C")

    def test_catAndMouse_invalid_x(self):
        with self.assertRaises(ValueError):
            catAndMouse(101, 2, 3)

    def test_catAndMouse_invalid_y(self):
        with self.assertRaises(ValueError):
            catAndMouse(1, 0, 3)

    def test_catAndMouse_invalid_z(self):
        with self.assertRaises(ValueError):
            catAndMouse(1, 2, 101)


if __name__ == "__main__":
    unittest.main()
