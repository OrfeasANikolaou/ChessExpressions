import unittest

import my_re_functions as mrf


class TestChessExpressions(unittest.TestCase):
    def test_winner(self):
        self.assertEqual(mrf.winner(mrf.a_pgn_game), "ΙΣΟΠΑΛΙΑ")

    def test_elo(self):
        self.assertEqual(mrf.diff_elo(mrf.a_pgn_game), 7)

    def test_date(self):
        self.assertEqual(mrf.date_of_game(mrf.a_pgn_game), "09-04-2023")

    def test_moves(self):
        self.assertEqual(mrf.moves(mrf.a_pgn_game), 49)


if __name__ == "__main__":
    unittest.main()
