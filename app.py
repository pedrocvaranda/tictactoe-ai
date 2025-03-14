from flash import Flask, request, jsonify, send_file
from board import Board
from players.human_player import HumanPlayer
from players.minimax_bot import MinimaxBot
import os

app = Flask(__name__)
board = Board()
player1 = HumanPlayer("X")  # Jogador humano (X)
player2 = MinimaxBot("O")  # Bot (O)
current_player = player1  # Começa com humano

@app.route("/move", methods=["POST"])
def make_move():
    global current_player

    data = request.json
    row, col = data["row"], data["col"]

    if (row, col) in board.get_legal_moves():
        board.make_move(row, col, current_player.symbol)

        # Alternar para o bot se for a vez dele
        if not board.has_winner() and not board.is_full():
            current_player = player2
            bot_move = player2.get_move(board)
            board.make_move(bot_move[0], bot_move[1], player2.symbol)
            current_player = player1  # Volta para o humano

        return jsonify({"status": "success", "board": board.board, "winner": board.has_winner()})

    return jsonify({"status": "invalid move"})

@app.route("/reset", methods=["POST"])
def reset_game():
    global board, current_player
    board = Board()
    current_player = player1
    return jsonify({"status": "game reset"})

@app.route("/board_image")
def get_board_image():
    board.save_board_image("static/tic_tac_toe.png")
    return send_file("static/tic_tac_toe.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
