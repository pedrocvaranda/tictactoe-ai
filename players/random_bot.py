import random

class RandomBot:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        return random.choice(board.get_legal_moves())
