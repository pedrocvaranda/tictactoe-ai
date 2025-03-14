class MinimaxBot:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        best_score = float('-inf')
        best_move = None

        for move in board.get_legal_moves():
            board.make_move(move[0], move[1], self.symbol)
            score = self.minimax(board, False)
            board.board[move[0]][move[1]] = " "  # Desfaz a jogada

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, is_maximizing):
        winner = board.has_winner()
        if winner == self.symbol:
            return 1
        elif winner:
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in board.get_legal_moves():
                board.make_move(move[0], move[1], self.symbol)
                score = self.minimax(board, False)
                board.board[move[0]][move[1]] = " "  # Desfaz a jogada
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            opponent_symbol = "O" if self.symbol == "X" else "X"
            for move in board.get_legal_moves():
                board.make_move(move[0], move[1], opponent_symbol)
                score = self.minimax(board, True)
                board.board[move[0]][move[1]] = " "  # Desfaz a jogada
                best_score = min(score, best_score)
            return best_score
