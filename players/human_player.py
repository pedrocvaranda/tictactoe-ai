class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                move = input(f"Jogador ({self.symbol}), insira sua jogada (linha e coluna, ex: 1 2): ")
                row, col = map(int, move.split())
                if (row, col) in board.get_legal_moves():
                    return row, col
                else:
                    print("Jogada inválida!")
            except ValueError:
                print("Entrada inválida!")
