from board import Board
from game import Game
from players import RandomBot, OneLayerBot, MinimaxBot, AlphaBetaBot, HumanPlayer

def main():
    print("Escolha os jogadores:")
    print("0 - Jogador Humano")
    print("1 - Bot Aleatório")
    print("2 - Bot de Uma Camada")
    print("3 - Bot Minimax")
    print("4 - Bot Minimax com Poda Alfa-Beta")

    choices = {
        "0": HumanPlayer,  # Adicionamos a opção do jogador humano
        "1": RandomBot,
        "2": OneLayerBot,
        "3": MinimaxBot,
        "4": AlphaBetaBot
    }

    player1_choice = input("Escolha o jogador 1 (X): ")
    player2_choice = input("Escolha o jogador 2 (O): ")

    if player1_choice not in choices or player2_choice not in choices:
        print("Escolha inválida! Saindo do programa.")
        return

    player1 = choices[player1_choice]("X")
    player2 = choices[player2_choice]("O")

    board = Board()
    game = Game(board, player1, player2)

    print("\nIniciando jogo...\n")
    game.play()

if __name__ == "__main__":
    main()
