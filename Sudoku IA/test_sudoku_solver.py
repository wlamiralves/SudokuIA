# tests/test_sudoku_solver.py

import unittest
import numpy as np
from sudoku_solver import solve_sudoku, generate_sudoku

class TestSudokuSolver(unittest.TestCase):

    def test_solve_sudoku(self):
        board = np.array([
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
        solved_board = np.copy(board)
        solve_sudoku(solved_board)
        self.assertFalse(np.array_equal(board, solved_board), "The solver did not solve the board correctly.")

    def test_generate_sudoku(self):
        board = np.zeros((9, 9), dtype=int)
        generated_board = generate_sudoku(board, num_clues=30)
        self.assertTrue(np.any(generated_board != 0), "The board was not generated correctly.")

if __name__ == "__main__":
    unittest.main()
