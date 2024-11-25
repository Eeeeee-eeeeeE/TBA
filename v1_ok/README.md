# TBA

Ce repo contient la première version modifiée du jeu d’aventure TBA (une première version).

Ce qui a été implémenté en plus de la v0 est un passage interdit entre la forêt et la tour, un sens unique du marécage vers la tour, la gestion de la commande vide 

## Structuration

Il y a pour le moment 5 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre .
