"""
@author: Abdoulaye Niang
@date : 2024-02-26

Les jeux de Nim sont des jeux de stratégie pure, à 2 joueurs.
Ce jeu consiste à enlever 1, 2 ou 3 objets à chaque tour.
Le vainqueur est celui qui peut jouer en dernier.
"""

class NimGame:
    def __init__(self, player1:str, player2:str, number:int):
        self.player1 = player1
        self.player2 = player2
        self.number = number
        self.current_player = self.player1
        self.end_game = False
        self.winner = None


    def get_winner(self):
        return self.winner


    def get_number(self):
        return self.number


    def get_player1(self):
        return self.player1


    def get_player2(self):
        return self.player2


    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def check_end_game(self, v:int):
        self.number -= v
        if self.number <= 0:
            self.end_game = True
            self.winner = self.current_player


    def game(self):
        check = True
        while check:
            try:
                v = int(input(f'Tour {self.current_player} >> '))
                if v in (1,2,3) and (self.get_number() - v >= 0):
                    check = False
                    self.check_end_game(v)
                    self.change_player()
                    print(f'Restant {self.get_number()}',end=' ')
            except ValueError:
                pass
            

    def play(self):
        while not self.end_game:
            self.game()
        print(f'The Winner : {self.get_winner()}')
        exit (0)
