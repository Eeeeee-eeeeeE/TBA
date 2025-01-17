"""Description: Game class and Graphic class"""

# Import modules

import tkinter as tk
from tkinter import messagebox, PhotoImage

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

DEBUG = True

# Game class as written in class
class Game():
    """Game class"""

    def __init__(self):
        """ The constructor"""
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.possible_direction = set()

        self.text = "" #the text to display on the graphical interface
        self.warning = ""
        self.nb = 0 #nb of interactions with the player
        self.images = dict([('begining', 'begining.png')])

    def setup(self):
        """Setup the game"""

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

        wardrob_o = Room("wardrob_o", "la partie de gauche d'une grande salle lugubre sans fenêtre.")
        self.rooms.append(wardrob_o)
        self.images['wardrob_o'] = 'wardrob_o.png'
        wardrob_e = Room("wardrob_e", "la partie de droite d'une grande salle lugubre sans fenêtre.")
        self.rooms.append(wardrob_e)
        self.images['wardrob_e'] = 'wardrob_e.png'
        enigma = Room("Enigma", "une salle modeste. Devant vous se tient un petit monsieur à l'air malicieux.")
        self.rooms.append(enigma)
        self.images['Enigma'] = 'Enigma.png'
        nothing = Room("Nothing", "une salle vide.")
        self.rooms.append(nothing)
        self.images['Nothing'] = 'Nothing.png'
        brokenglass = Room("Brokenglass", "une salle dont le sol est couvert par une écatombe de fioles brisées. Le reflet du soleil sur ces fragments de verre brisé donne des couleurs irisées aux murs telle une mosaique des temps antiques.")
        self.rooms.append(brokenglass)
        self.images['Brokenglass'] = 'Brokenglass.png'
        glitter = Room("Glitter", "une salle où se dresse au milieu une satue à paillettes rose. Cette statue représente un homme, environ la quarantaine et demi, barbu de 12 jours, petites lunettes losange sur un nez imposant, une interminablement longue blouse de scientifique sur le dos, et deux yeux roses.")
        self.rooms.append(glitter)
        self.images['Glitter'] = 'Glitter.png'
        musty = Room("Musty", "une petit pièce humide et sombre. Les murs sont tapis d'une couche épaisse de moisissure.")
        self.rooms.append(musty)
        self.images['Musty'] = 'Musty.png'
        out = Room("Out", "une large pièce acceuillante vu sur un jardin. Il y fait un peu frais, le vent s'engouffre par le pas d'une petite porte dissimulée.")
        self.rooms.append(out)
        self.images['Out'] = 'Out.png'
        tree = Room("Tree", "une parcelle de terre sur laquelle s'élève un acassia centenaire. Gloire de la nature et de Gaya, son tron est épais comme une maison, ses branches ont la circonférence d'une centrale nucléaire et ses feuilles sont petite comme des petites libellules.  Malheureseument pour les dryades, cet arbre garde la trace de son exploitation : des balafres multiples décorent son tron.")
        self.rooms.append(tree)
        self.images['Tree'] = 'Tree.png'


        # Create exits for rooms

        wardrob_o.exits = {"N" : brokenglass, "E" : wardrob_e, "S" : None, "O" : None, "U" : None, "D" : nothing}
        wardrob_e.exits = {"N" : None, "E" : None, "S" : None, "O" : wardrob_o, "U" : None, "D" : enigma}
        enigma.exits = {"N" : None, "E" : None, "S" : None, "O" : nothing, "U" : wardrob_e, "D" : None}
        nothing.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : wardrob_o, "D" : None}
        brokenglass.exits = {"N" : None, "E" : glitter, "S" : wardrob_o, "O" : None, "U" : None, "D" : None}
        glitter.exits = {"N" : None, "E" : None, "S" : None, "O" : brokenglass, "U" : None, "D" : out}
        musty.exits = {"N" : None, "E" : out, "S" : None, "O" : None, "U" : None, "D" : None}
        out.exits = {"N" : None, "E" : tree, "S" : None, "O" : musty, "U" : glitter, "D" : None}
        tree.exits = {"N" : None, "E" : None, "S" : None, "O" : tree, "U" : None, "D" : None}

        #Setup items of the rooms
        truc = Item("truc", "un truc étrange", 50)
        wardrob_o.inventory["truc"] = truc
        brindille = Item("brindille", "un baton de bois à votre echelle", 0.2)
        wardrob_o.inventory["brindille"] = brindille

        #Setup characters of the rooms
        mister = Character("mister", "un mister étrange", wardrob_e, ["hola"], [wardrob_e, wardrob_o])
        wardrob_e.characters["mister"] = mister
        harry = Character("harry", "un lapin ferroce", wardrob_e, ["tu es à croquer", "j t'aime bien (mm si je pref les carottes)"], [wardrob_e, wardrob_o])
        wardrob_e.characters["harry"] = harry

        #Set of all the possible directions
        self.possible_direction = {k for r in self.rooms for k in r.exits.keys() }

        # Setup starting room
        self.player.current_room = wardrob_o

        #A ENLEVER POUR TESTER
        #Setup the text to display
        self.text = self.player.current_room.get_long_description()

    def get_current_text(self):
        """Returns the current question"""
        if self.nb == 0:  #if it is the first interaction of the game
            self.text = "\nEntrez votre nom: "
        elif self.nb == 1: #if it is the second interaction of the game
            self.text = f"\nBienvenue {self.player.name} dans ce jeu d'aventure !\nEntrez 'help' si vous avez besoin d'aide.\n"
        return self.text #DANS LES FICHIERS QUAND PRINT REMPLACER PAR MODIF GAME.TEXT

    def execute_command(self, command, list_of_words):
        """If the command is recognized (verified in treat_command), execute it (used in the methode treat_command of the Class Graphic)"""
        command.action(self, list_of_words, command.number_of_parameters)



class Graphic(tk.Tk, Game):
    """Class of the graphical interface with tkinter"""

    def __init__(self):
        """The constructor."""
        tk.Tk.__init__(self)
        Game.__init__(self)
        self.title("Jeu d'Aventure")
        self.geometry("800x800")
        self.background = PhotoImage(file = self.images["begining"])
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets of the interface"""
        # Background
        self.image_label = tk.Label(self, image = self.background)
        self.image_label.place(x=0, y=0, relwidth = 1, relheight = 1)
        # Text box to display text
        self.text_label = tk.Label(self, text=self.get_current_text(), font=("Arial", 14), wraplength=700)
        self.text_label.pack(pady=20)
        #Text area to enter the response
        self.answer_entry = tk.Entry(self, font=("Arial", 14), width=30)
        self.answer_entry.pack(pady=10)
        # Button to submit the answer. This button is what calls the fonction treat_command.
        self.submit_button = tk.Button(self, text="Soumettre", font=("Arial", 14), command=self.treat_command)
        self.submit_button.pack(pady=10)

    def treat_command(self):
        """Process the answer and move to the next question"""
        command_string = self.answer_entry.get()

        if self.nb == 1:
            self.setup()

        elif self.nb == 0:
            self.player = Player(command_string)

        elif  len(command_string) != 0 :
            # Split the command string into a list of words
            list_of_words = command_string.split(" ")

            command_word = list_of_words[0]

            # If the command is not recognized, display an error message
            if command_word not in self.commands.keys():
                messagebox.showwarning(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                self.execute_command(command, list_of_words)

        #If the game is not ended, update the graphical interface
        #(does not get the command from the player, it is the push of the submit_button that calls the treat_command)
        if not self.finished:
            self.update_widgets()
        else:
            self.end_game()

    def update_widgets(self):
        """Updates the displayed question"""
        #increases the numbers of interactions
        self.nb = self.nb + 1
        # Clear the response entry (clear what was written by the player)
        self.answer_entry.delete(0, tk.END)
        #Shows the new text / question
        self.text_label.config(text=self.get_current_text())
        #New image of the current room in the background
        if self.nb > 1 :
            self.background = PhotoImage(file = self.images[self.player.current_room.name]) #/self.images[self.player.current_room.name]
            self.image_label.config(image = self.background)
        #Popup (messagebox) if there is a warning
        if self.warning != "" :
            messagebox.showwarning(self.warning)
        self.warning = ""

    def end_game(self):
        """End of game"""
        messagebox.showinfo(self.warning)#"Jeu terminé", f"Votre score final est : "#{self.get_score()}/{len(self.questions)}
        self.quit_game()

    def quit_game(self):
        """Quit the game permanently"""
        self.destroy()

def main():
    """Start the game"""
    # Create a game object and play the game
    jeu = Graphic()
    #displays the main window on the screen and then waits for the user to take an action.
    jeu.mainloop()

if __name__ == "__main__":
    main()
