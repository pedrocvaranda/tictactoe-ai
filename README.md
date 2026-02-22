# 🎮 Tic-Tac-Toe AI

**Play against an unbeatable AI powered by the Minimax algorithm**

A fully interactive Tic-Tac-Toe game with a web interface and a provably optimal AI opponent — implemented from scratch in Python and served via Flask.

-----

## 🎯 What is This?

This project brings to life a classic **Tic-Tac-Toe** game where you can challenge an AI that never loses. The AI uses the **Minimax algorithm** to explore the full game tree and always select the optimal move.

**Key Features:**

- 🧠 **Unbeatable AI** via the Minimax algorithm — the AI plays perfectly in all scenarios
- 🌐 **Web-based interface** built with Flask, HTML, CSS, and JavaScript — playable in any browser
- 🎮 **Multiple player modes** — human vs. AI, AI vs. AI, and human vs. human
- 🗂️ **Clean, modular architecture** — board logic, game state, and players are fully decoupled
- 🖥️ **Terminal mode** available via `main.py` for command-line gameplay

-----

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/pedrocvaranda/tictactoe-ai.git
cd tictactoe-ai

# Install dependencies
pip install flask

# Launch the web app
python app.py
```

Then open your browser at `http://localhost:5000` and start playing!

### Terminal Mode

```bash
# Play directly in the terminal
python main.py
```

-----

## 🧠 Algorithm

### Minimax

The AI uses the **Minimax** algorithm to select moves. It recursively explores every possible future game state, assuming both players play optimally:

```
minimax(state, is_maximizing):
    if terminal(state):
        return score(state)

    if is_maximizing:
        return max(minimax(child, False) for child in children(state))
    else:
        return min(minimax(child, True) for child in children(state))
```

**Scores:**

|Outcome   |Score|
|----------|-----|
|AI wins   |+1   |
|Draw      |0    |
|Human wins|-1   |

Since Tic-Tac-Toe has a finite and small game tree (at most 9! = 362,880 states), Minimax explores it completely without any pruning — guaranteeing an optimal move in every situation.

### Why Is It Unbeatable?

Tic-Tac-Toe is a **solved game**. With optimal play from both sides, the result is always a draw. The AI never deviates from optimal play, so the best a human can achieve is a tie.

-----

## 📂 Project Structure

```
tictactoe-ai/
├── app.py              # Flask web server — routes and game API
├── board.py            # Board representation and win/draw detection
├── game.py             # Game loop and state management
├── main.py             # Terminal entry point
├── players/            # Player implementations (Human, AI)
├── static/             # CSS and JavaScript for the web interface
├── templates/          # HTML templates (Jinja2)
└── __pycache__/
```

-----

## 🧪 Examples

### Example 1: Using the Board Directly

```python
from board import Board

board = Board()
board.make_move(0, 'X')   # Top-left
board.make_move(4, 'O')   # Center
board.display()
```

### Example 2: Running an AI vs. AI Match

```python
from game import Game
from players.ai_player import AIPlayer

game = Game(player_x=AIPlayer('X'), player_o=AIPlayer('O'))
game.play()
```

### Example 3: Querying the Best Move

```python
from board import Board
from players.ai_player import AIPlayer

board = Board()
board.make_move(0, 'X')

ai = AIPlayer('O')
best_move = ai.get_move(board)
print(f"AI plays at position {best_move}")
```

-----

## 👨‍🔬 About the Author

**Pedro Coutinho Varanda**

- 🥇 **#1 Brazil** - National Astronomy Olympiad (OBA 2025, Perfect Score)
- 🥈 **#2 Brazil** - OBA 2023
- 🥉 **#3 Brazil** - OBA 2024
- 🎯 **3× Selected** - International Olympiad on Astronomy and Astrophysics (IOAA)
- 🥇 **4× Gold** - Canguru Mathematics Competition (2022-2025)

ML/AI enthusiast | Rio de Janeiro, Brazil 🇧🇷

[GitHub](https://github.com/pedrocvaranda) • [Email](mailto:pedrocvaranda@gmail.com)

-----

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
1. Create your feature branch (`git checkout -b feature/AmazingFeature`)
1. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
1. Push to the branch (`git push origin feature/AmazingFeature`)
1. Open a Pull Request

-----

## 📝 License

This project is licensed under the MIT License - see the <LICENSE> file for details.

-----

## 🔗 Related Projects

- [Varandian Optics Simulator](https://github.com/pedrocvaranda/varadian-optics-simulator) — Light propagation in curved spaces
- [Cash Allocation Model](https://github.com/pedrocvaranda/modelo_alocacao_caixa) — ML-based financial optimizer

-----



[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey.svg)](https://flask.palletsprojects.com)
[![Algorithm](https://img.shields.io/badge/Algorithm-Minimax-orange.svg)](https://en.wikipedia.org/wiki/Minimax)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/pedrocvaranda/tictactoe-ai)
