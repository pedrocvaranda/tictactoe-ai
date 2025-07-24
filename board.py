#from PIL import Image, ImageDraw

class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def get_legal_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]

    def make_move(self, row, col, symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = symbol
            self.save_board_image("static/tic_tac_toe.png")
            return True
        return False

    def has_winner(self):
        lines = self.board + list(zip(*self.board))

        diagonals = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        ]

        for line in lines + diagonals:
            if line == ["X", "X", "X"]:
                return "X"
            if line == ["O", "O", "O"]:
                return "O"
        return None

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    #def save_board_image(self, filename):
        img = Image.new("RGB", (300, 300), "white")
        draw = ImageDraw.Draw(img)

        for i in range(1, 3):
            draw.line([(0, i * 100), (300, i * 100)], fill="black", width=5)
            draw.line([(i * 100, 0), (i * 100, 300)], fill="black", width=5)

        for r in range(3):
            for c in range(3):
                if self.board[r][c] != " ":
                    draw.text((c * 100 + 40, r * 100 + 30), self.board[r][c], fill="black")

        img.save(filename)
