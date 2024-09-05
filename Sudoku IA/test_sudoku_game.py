# tests/test_sudoku_game.py

import unittest
import json
import numpy as np
from sudoku_utils import save_game, load_game

class TestSudokuUtils(unittest.TestCase):

    def setUp(self):
        self.board = np.array([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
        self.solution = np.copy(self.board)

    def test_save_load_game(self):
        save_game(self.board, self.solution)
        loaded_board, loaded_solution = load_game()
        np.testing.assert_array_equal(self.board, loaded_board, "Loaded board does not match the saved board.")
        np.testing.assert_array_equal(self.solution, loaded_solution, "Loaded solution does not match the saved solution.")

if __name__ == "__main__":
    unittest.main()
