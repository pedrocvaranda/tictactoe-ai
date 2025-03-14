class OneLayerBot:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        # Verifica se pode vencer na próxima jogada
        for move in board.get_legal_moves():
            temp_board = Board()
            temp_board.board = [row[:] for row in board.board]
            temp_board.make_move(move[0], move[1], self.symbol)
            if temp_board.has_winner() == self.symbol:
                return move

        # Caso contrário, joga aleatoriamente
        return RandomBot(self.symbol).get_move(board)
