import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np
import time
import json
from sudoku_solver import solve_sudoku, generate_sudoku
from sudoku_utils import save_game, load_game

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku IA")
        self.board = np.zeros((9, 9), dtype=int)
        self.solution = np.zeros((9, 9), dtype=int)
        self.entry_widgets = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        for r in range(9):
            for c in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), borderwidth=1, relief='solid')
                entry.grid(row=r, column=c, padx=5, pady=5)
                self.entry_widgets[r][c] = entry

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_game)
        self.solve_button.grid(row=10, column=0, columnspan=9, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=11, column=0, columnspan=9, pady=10)

        self.check_button = tk.Button(self.root, text="Check Solution", command=self.check_solution)
        self.check_button.grid(row=12, column=0, columnspan=9, pady=10)

        self.compete_button = tk.Button(self.root, text="Compete Against Solver", command=self.compete_mode)
        self.compete_button.grid(row=13, column=0, columnspan=9, pady=10)

        self.save_button = tk.Button(self.root, text="Save Game", command=self.save_game)
        self.save_button.grid(row=14, column=0, columnspan=3, pady=10)

        self.load_button = tk.Button(self.root, text="Load Game", command=self.load_game)
        self.load_button.grid(row=14, column=3, columnspan=6, pady=10)

        self.timer_label = tk.Label(self.root, text="Time: 0s")
        self.timer_label.grid(row=15, column=0, columnspan=9, pady=10)
        self.start_time = None

    def reset_game(self):
        difficulty = simpledialog.askinteger("Difficulty", "Enter difficulty level (1-5):", minvalue=1, maxvalue=5)
        if not difficulty:
            return

        self.board = generate_sudoku(self.board, num_clues=20 + difficulty * 10)
        self.solution = np.copy(self.board)
        solve_sudoku(self.solution)
        self.update_entries()
        self.start_time = time.time()
        self.timer_label.config(text="Time: 0s")
        self.update_timer()

    def update_entries(self):
        for r in range(9):
            for c in range(9):
                value = self.board[r, c]
                entry = self.entry_widgets[r][c]
                entry.delete(0, tk.END)
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state='disabled')
                else:
                    entry.config(state='normal')

    def solve_game(self):
        temp_board = np.copy(self.board)
        start_time = time.time()
        if solve_sudoku(temp_board):
            elapsed_time = time.time() - start_time
            self.board = temp_board
            self.update_entries()
            tk.messagebox.showinfo("Sudoku", f"Solver finished in {int(elapsed_time)} seconds.")
        else:
            tk.messagebox.showinfo("Sudoku", "No solution exists")

    def check_solution(self):
        player_board = np.zeros((9, 9), dtype=int)
        for r in range(9):
            for c in range(9):
                value = self.entry_widgets[r][c].get()
                if value:
                    player_board[r, c] = int(value)
        
        if np.array_equal(player_board, self.solution):
            tk.messagebox.showinfo("Sudoku", "Congratulations! Your solution is correct!")
        else:
            tk.messagebox.showinfo("Sudoku", "The solution is incorrect. Try again.")

    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed_time}s")
            self.root.after(1000, self.update_timer)

    def compete_mode(self):
        self.reset_game()
        tk.messagebox.showinfo("Sudoku", "You have started the competition against the solver!")

    def save_game(self):
        game_data = {
            'board': self.board.tolist(),
            'solution': self.solution.tolist()
        }
        with open('saved_game.json', 'w') as f:
            json.dump(game_data, f)
        tk.messagebox.showinfo("Sudoku", "Game saved successfully!")

    def load_game(self):
        try:
            with open('saved_game.json', 'r') as f:
                game_data = json.load(f)
                self.board = np.array(game_data['board'])
                self.solution = np.array(game_data['solution'])
                self.update_entries()
                tk.messagebox.showinfo("Sudoku", "Game loaded successfully!")
        except FileNotFoundError:
            tk.messagebox.showwarning("Sudoku", "No saved game found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
