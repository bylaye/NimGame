import sys
from NimGame import NimGame

game = NimGame('Player 1', 'Player 2', 10)

"""
Passer en parametre le nombre d'objet
"""
if __name__ == '__main__':
    if len(sys.argv) == 2:
        number = int(sys.argv[1])
    else:
        number = 20
    player1 = 'Player 1'
    player2 = 'Player 2'
    game = NimGame(player1, player2, number)
    print(f'Total stack = {game.get_number()}')
    game.play()
