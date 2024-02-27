# NimGame
Nim Game

## Concept du Jeu
Les jeux de Nim sont des jeux de stratégie pure, à 2 joueurs.\
Ce jeu consiste à enlever 1, 2 ou 3 objets à chaque tour.\
Le vainqueur est celui qui peut jouer en dernier.\

## Lancer le programme
On peut lancer la partie avec la commande
```
python3 play.py
```

Output
> Total stack = 20
> Tour Player 1 >> 

Toutefois on peut aussi lancer la simulation en passant en parametre le nombre d'objet
```
python3 play.py 13
```

Output
```
Total stack = 13
Tour Player 1 >> 3
Restant 10 Tour Player 2 >> 2
Restant 8 Tour Player 1 >> 3
Restant 5 Tour Player 2 >> 1
Restant 4 Tour Player 1 >> 2
Restant 2 Tour Player 2 >> 2
Restant 0 The Winner : Player 2
```
