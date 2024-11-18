# Description: Game class

# Import modules

from v6.room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from inventory_caracter import InventoryCaracter
from character import Caracter

DEBUG = True

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.knowndirections = set() #ou attribut de clasee JE SAIS PAS???
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : regarder les items présents dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <item> : prendre un des items présents dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : <item> enlever un des items que l'on possède", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : regarder les items que l'on possède", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk", " <someone> : parler à un pnj", Actions.talk, 1)
        self.commands["talk"] = talk

        # Setup rooms

        grassalone = Room("GrassAlone", "devant une étendue de brins d'herbe qui font votre taille.")
        self.rooms.append(grassalone)
        den = Room("Den", "tombé dans un terrier sombre sous le sol. Devant vous se dresse un lapin aux poils gris et aux yeux éclarlates.")
        self.rooms.append(den)
        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)

        # Create exits for rooms

        grassalone.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : den}
        den.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : None, "O" : None}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}

        #Creation items
        grassalone.inventory_caracter = InventoryCaracter('Room')
        grassalone.inventory_caracter.inventory_dict = {'brindille' : Item("brindille", "un baton de bois à votre echelle", 0.2)} 
        den.inventory_caracter = InventoryCaracter('Room')
        den.inventory_caracter.caracter_dict = {'harry' : Caracter("harry", "un lapin ferroce", den, ["tu es à croquer", "j t'aime bien (mm si je pref les carottes)"])}
        forest.inventory_caracter = InventoryCaracter('Room')
        tower.inventory_caracter = InventoryCaracter('Room')
        cave.inventory_caracter = InventoryCaracter('Room')
        cottage.inventory_caracter = InventoryCaracter('Room')
        swamp.inventory_caracter = InventoryCaracter('Room')
        castle.inventory_caracter = InventoryCaracter('Room')

        #Création/Setup des directions connues PAS SURE IL A DIT DEUX LIGNES 
        self.knowndirections = set(self.rooms[0].exits.keys())

        # Setup player and starting room (et l'historique)

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = grassalone
        self.player.history.append(grassalone)
        self.player.inventory = InventoryCaracter('Player')

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

        #Si le joueur appuis sur Entrée à l'invite de commande, rien ne s'affiche
        if len(command_string) != 0 : #ou juste == '' voir si maniere plus ismple
        
            # Split the command string into a list of words
            list_of_words = command_string.split(" ")

            command_word = list_of_words[0]

            # If the command is not recognized, print an error message
            if command_word not in self.commands.keys():
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
