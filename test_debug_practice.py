import unittest

from debug_practice import calculate_average, find_maximum, is_even


class TestCalculateAverage(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_average([2, 4, 6]), 4)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4]), 2.5)

    def test_single_value(self):
        self.assertEqual(calculate_average([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-4, -2, 0]), -2)

    def test_empty_list_raises(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])


class TestIsEven(unittest.TestCase):
    def test_even_positive(self):
        self.assertTrue(is_even(8))

    def test_odd_positive(self):
        self.assertFalse(is_even(7))

    def test_zero_is_even(self):
        self.assertTrue(is_even(0))

    def test_negative_even(self):
        self.assertTrue(is_even(-4))

    def test_negative_odd(self):
        self.assertFalse(is_even(-3))


class TestFindMaximum(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(find_maximum([1, 5, 3, 9, 2]), 9)

    def test_single_value(self):
        self.assertEqual(find_maximum([4]), 4)

    def test_all_negative(self):
        self.assertEqual(find_maximum([-10, -3, -7]), -3)

    def test_mixed_signs(self):
        self.assertEqual(find_maximum([-5, 0, 2, -1]), 2)

    def test_duplicates(self):
        self.assertEqual(find_maximum([3, 3, 3]), 3)

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            find_maximum([])


if __name__ == "__main__":
    unittest.main()
