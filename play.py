import sys
from NimGame import NimGame

game = NimGame('Player 1', 'Player 2', 10)

"""
Passer 3 parametres pour representer
le player 1, player 2, et le nombre d'objet
"""
if __name__ == '__main__':
    if len(sys.argv) == 4:
        number = int(sys.argv[3])
        player1 = sys.argv[1]
        player2 = sys.argv[2]
        game = NimGame(player1, player2, number)
    print(f'Total stack = {game.get_number()}')
    game.play()
