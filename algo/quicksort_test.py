import unittest
import quicksort


class TestQuicksort(unittest.TestCase):
    def test_quicksort_pythonic(self):
        self.assertEqual(quicksort.quicksort_pythonic([8, 3, 9, 1, 3, -5, 10]), [-5, 1, 3, 3, 8, 9, 10])

    def test_quicksort_traditional(self):
        self.assertEqual(quicksort.quicksort_traditional([8, 3, 9, 1, 3, -5, 10]), [-5, 1, 3, 3, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
