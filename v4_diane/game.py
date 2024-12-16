# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.possible_direction = set()
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O) ou horizontale (D, U)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : retour à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : affiche la liste des items dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : mettre un item de la pièce dans son inventaire", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : déposer un item de son inventaire dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : regarder ce qu'il y a dans son inventaire", Actions.check, 0)
        self.commands["check"] = check
        
        # Setup rooms

        wardrobeO = Room("WardrobeO", "la partie de gauche d'une grande salle lugubre sans fenêtre.")
        self.rooms.append(wardrobeO)
        wardrobeE = Room("WardrobeE", "a partie de droite d'une grande salle lugubre sans fenêtre.")
        self.rooms.append(wardrobeE)
        enigma = Room("Enigma", "une salle modeste. Devant vous se tient un petit monsieur à l'air malicieux.")
        self.rooms.append(enigma)
        nothing = Room("Nothing", "une salle vide.")
        self.rooms.append(nothing)
        brokenglass = Room("Brokenglass", "une salle dont le sol est couvert par une écatombe de fioles brisées. Le reflet du soleil sur ces fragments de verre brisé donne des couleurs irisées aux murs telle une mosaique des temps antiques.")
        self.rooms.append(brokenglass)
        glitter = Room("Glitter", "une salle où se dresse au milieu une satue à paillettes rose. Cette statue représente un homme, environ la quarantaine et demi, barbu de 12 jours, petites lunettes losange sur un nez imposant, une interminablement longue blouse de scientifique sur le dos, et deux yeux roses.")
        self.rooms.append(glitter)
        musty = Room("Musty", "une petit pièce humide et sombre. Les murs sont tapis d'une couche épaisse de moisissure.")
        self.rooms.append(musty)
        out = Room("Out", "une large pièce acceuillante vu sur un jardin. Il y fait un peu frais, le vent s'engouffre par le pas d'une petite porte dissimulée.")
        self.rooms.append(out)
        tree = Room("Tree", "une parcelle de terre sur laquelle s'élève un acassia centenaire. Gloire de la nature et de Gaya, son tron est épais comme une maison, ses branches ont la circonférence d'une centrale nucléaire et ses feuilles sont petite comme des petites libellules.  Malheureseument pour les dryades, cet arbre garde la trace de son exploitation : des balafres multiples décorent son tron.")
        self.rooms.append(tree)

        # Create exits for rooms

        wardrobeO.exits = {"N" : brokenglass, "E" : wardrobeE, "S" : None, "O" : None, "U" : None, "D" : nothing}
        wardrobeE.exits = {"N" : None, "E" : None, "S" : None, "O" : wardrobeO, "U" : None, "D" : enigma}
        enigma.exits = {"N" : None, "E" : None, "S" : None, "O" : nothing, "U" : wardrobeE, "D" : None}
        nothing.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : wardrobeO, "D" : None}
        brokenglass.exits = {"N" : None, "E" : glitter, "S" : wardrobeO, "O" : None, "U" : None, "D" : None}
        glitter.exits = {"N" : None, "E" : None, "S" : None, "O" : brokenglass, "U" : None, "D" : out}
        musty.exits = {"N" : None, "E" : out, "S" : None, "O" : None, "U" : None, "D" : None}
        out.exits = {"N" : None, "E" : tree, "S" : None, "O" : musty, "U" : glitter, "D" : None}
        tree.exits = {"N" : None, "E" : None, "S" : None, "O" : tree, "U" : None, "D" : None}

        #Set of all the possible directions
        self.possible_direction = {k for r in self.rooms for k in r.exits.keys() }
        
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = wardrobeE

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            if command_word != '':
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
