import os
from board import Board
from time import sleep
from PIL import Image

class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def play(self):
        while not self.board.is_full() and not self.board.has_winner():
            row, col, = self.current_player.get_move(self.board)
            if self.board.make_move(row, col, self.current_player.symbol):
                self.board.print_board()

                if os.path.exists("tic_tac_toe.png"):
                    img = Image.open("tic_tac_toe.png")
                    img.show()

                self.current_player = self.player1 if self.current_player == self.player2 else self.player2
                sleep(1)

        winner = self.board.has_winner()
        if winner:
            print(f"Jogador {winner} venceu!")
        else:
            print("Empate!")

        if os.path.exists("tic_tac_toe.png"):
            img = Image.open("tic_tac_toe.png")
            img.show()
