import unittest
import puzzles


class TestPuzzles(unittest.TestCase):
    def test_clock_angle(self):
        self.assertEqual(puzzles.clock_angle('05:15'), 67.5)
        self.assertEqual(puzzles.clock_angle('11:45', 'radians'), 1.4399)

    def test_trapped_rain_water(self):
        self.assertEqual(puzzles.trapped_rain_water([1, 6, 3, 5, 9, 2, 8, 3]), 10)

    def test_ideal_buy_and_sell_days(self):
        self.assertEqual(puzzles.ideal_buy_and_sell_days([5, 4, 3, 8, 7, 1, 6]), [2, 3])

    def test_possible_game_scores(self):
        self.assertEqual(puzzles.possible_game_scores(3), [[1, 1, 1], [1, 2], [2, 1], [3]])

    def test_find_duplicates(self):
        self.assertEqual(puzzles.find_duplicates([1, 3, 5, 3, 6]), [3])

    def test_count_matching_pairs(self):
        self.assertEqual(puzzles.count_matching_pairs([1, 3, 5, 7, 9], 10), 2)


if __name__ == '__main__':
    unittest.main()
