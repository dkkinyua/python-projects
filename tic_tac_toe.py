"""
A tic-tac-toe game instructed by Francis on a webinar in GOMYCODE on 25th July 2025.

"""
import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = []

        # Create the board layout
        def _create_board(self):
            display_fname = tk.Frame(master=self)
            display_frame.pack(fill=tk.X)
            self.display = tk.Label(
                master=display_fname,
                text="Readt?"
                font=font.Font(size=24, weight="bold")
            )
            self.display.pack()


def main():
    board = TicTacToeBoard()


main()
