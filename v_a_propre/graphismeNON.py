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

    def setup(self):
        """Setup the game"""

        # Setup commands
        self.commands["help"] = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter le jeu", Actions.quit, 0)
        descrip_go = " <direction> : se déplacer dans une direction cardinale (N, E, S, O)"
        self.commands["go"] = Command("go", descrip_go, Actions.go, 1)
        self.commands["back"] = Command("back", " : revenir en arrière", Actions.back, 0)
        look = Command("look", " : regarder les items présents dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        descrip_take = " <item> : prendre un des items présents dans la pièce"
        self.commands["take"] = Command("take", descrip_take, Actions.take, 1)
        drop = Command("drop", " : <item> enlever un des items que l'on possède", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : regarder les items que l'on possède", Actions.check, 0)
        self.commands["check"] = check
        self.commands["talk"] = Command("talk", " <someone> : parler à un pnj", Actions.talk, 1)

        self.setup_rooms()

    def setup_rooms1(self) :
        """Setup rooms wardrob_o and wardrob_e and enigma 
        (there is several setup_room functions because of pylint)"""

        descrip_wardrob_o =  "la partie de gauche d'une grande salle lugubre sans fenêtre."
        wardrob_o = Room("wardrob_o", descrip_wardrob_o)
        self.rooms.append(wardrob_o)
        descrip_wardrob_e = "la partie de droite d'une grande salle lugubre sans fenêtre."
        wardrob_e = Room("wardrob_e", descrip_wardrob_e)
        self.rooms.append(wardrob_e)
        descrip_enigma1 = "une salle modeste."
        descrip_enigma2 = "Devant vous se tient un petit monsieur à l'air malicieux."
        enigma = Room("Enigma", descrip_enigma1+descrip_enigma2)
        self.rooms.description(enigma)
        
        # Create exits for rooms
        wardrob_o.exits ={"N":brokenglass, "E":wardrob_e, "S":None, "O":None, "U":None, "D":nothing}
        wardrob_e.exits ={"N":None, "E":None, "S":None, "O":wardrob_o, "U":None, "D":enigma}
        enigma.exits ={"N":None, "E":None, "S":None, "O":nothing, "U":wardrob_e, "D":None}

        self.setup_rooms2()

    def setup_rooms2(self) :
        """Setup rooms nothing and brokenglass and glitter 
        (there is several setup_room functions because of pylint)"""

        nothing = Room("Nothing", "une salle vide.")
        self.rooms.append(nothing)
        descrip_bg1 = "une salle dont le sol est "
        descrip_bg2 = "couvert par une écatombe de fioles brisées."
        descrip_bg3 = "Le reflet du soleil sur ces fragments de verre brisé donne des"
        descrip_bg4 = " couleurs irisées aux murs telle une mosaique des temps antiques."
        brokenglass = Room("Brokenglass", descrip_bg1+descrip_bg2+descrip_bg3+descrip_bg4)
        self.rooms.append(brokenglass)
        descrip_glit1 = "une salle où se dresse au milieu une satue à paillettes rose. Cette statue"
        descrip_glit2 = " représente un homme, environ la quarantaine et demi, barbu de 12 jours,"
        descrip_glit3 = "petites lunettes losange sur un nez imposant, une interminablement "
        descrip_glit4 = "longue blouse de scientifique sur le dos, et deux yeux roses."
        glitter = Room("Glitter", descrip_glit1+descrip_glit2+descrip_glit3+descrip_glit4)
        self.rooms.append(glitter)
        
        # Create exits for rooms
        nothing.exits ={"N":None, "E":None, "S":None, "O":None, "U":wardrob_o, "D":None}
        brokenglass.exits ={"N":None, "E":glitter, "S":wardrob_o, "O":None, "U":None, "D":None}
        glitter.exits ={"N":None, "E":None, "S":None, "O":brokenglass, "U":None, "D":out}

        self.setup_rooms3()

    def setup_rooms3(self) :
        """Setup rooms musty and out and tree 
        (there is several setup_room functions because of pylint)"""

        descrip_musty1 = "une petit pièce humide et sombre. "
        descrip_musty2 ="Les murs sont tapis d'une couche épaisse de moisissure."
        musty = Room("Musty", descrip_musty1+descrip_musty2)
        self.rooms.append(musty)
        descrip_out1 ="une large pièce acceuillante vu sur un jardin. Il y fait un peu frais,"
        descrip_out2 = " le vent s'engouffre par le pas d'une petite porte dissimulée."
        out = Room("Out", descrip_out1+descrip_out2)
        self.rooms.append(out)
        descrip_tree1 = "une parcelle de terre sur laquelle s'élève un acassia centenaire."
        descrip_tree2 = " Gloire de la nature et de Gaya, son tron est épais comme une maison,"
        descrip_tree3 = "ses branches ont la circonférence d'une centrale nucléaire et ses feuilles"
        descrip_tree4 =  " sont petite comme des petites libellules. Malheureseument pour "
        descrip_tree5 = "les dryades, cet arbre garde la trace de son exploitation : "
        descrip_tree6 =  "des balafres multiples décorent son tron."
        a = descrip_tree1+descrip_tree2+descrip_tree3
        b = descrip_tree4+descrip_tree5+descrip_tree6
        tree = Room("Tree", a+b)
        self.rooms.append(tree)
        
        # Create exits for rooms
        musty.exits ={"N":None, "E":out, "S":None, "O":None, "U":None, "D":None}
        out.exits ={"N":None, "E":tree, "S":None, "O":musty, "U":glitter, "D":None}
        tree.exits ={"N":None, "E":None, "S":None, "O":tree, "U":None, "D":None}
        
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
            self.text = f"\nBienvenue {self.player.name} dans ce jeu d'aventure !\n"
            self.text = self.text + f"Entrez 'help' si vous avez besoin d'aide.\n"
        return self.text #DANS LES FICHIERS QUAND PRINT REMPLACER PAR MODIF GAME.TEXT

    def execute_command(self, command, list_of_words):
        """If the command is recognized (verified in treat_command), 
        execute it (used in the methode treat_command of the Class Graphic)"""
        command.action(self, list_of_words, command.number_of_parameters)

class BasicGraphic(tk.Tk) :
    """Class with the tkinter initialisation.
    Created because of "Too many instance attributes" of pylint (limit of 7 attributes)"""
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Jeu d'Aventure")
        self.geometry("800x800")

class Graphic(BasicGraphic, Game):
    """Class of the graphical interface with tkinter"""

    def __init__(self):
        """The constructor."""
        Game.__init__(self)
        BasicGraphic.__init__(self)
        self.background = PhotoImage(file = self.images["begining"])
        self.nb = 0 #nb of interactions with the player
        self.images = dict([('begining', 'begining.png')])

        self.create_widgets()

    def graphic_setup(self):
        """setup the images"""
        self.images['wardrob_e'] = 'wardrobE.png'
        self.images['Enigma'] = 'Enigma.png'
        self.images['Nothing'] = 'Nothing.png'
        self.images['wardrob_o'] = 'wardrobO.png'
        self.images['Glitter'] = 'Glitter.png'
        self.images['Brokenglass'] = 'Brokenglass.png'
        self.images['Musty'] = 'Musty.png'
        self.images['Out'] = 'Out.png'
        self.images['Tree'] = 'Tree.png'

    def create_widgets(self):
        """Create the widgets of the interface"""
        # Background
        self.image_label = tk.Label(self, image = self.background)
        self.image_label.place(x=0, y=0, relwidth = 1, relheight = 1)
        # Text box to display text
        t = self.get_current_text()
        self.text_label=tk.Label(self, text=t, font=("Arial", 14), wraplength=700)
        self.text_label.pack(pady=20)
        #Text area to enter the response
        self.answer_entry = tk.Entry(self, font=("Arial", 14), width=30)
        self.answer_entry.pack(pady=10)
        # Button to submit the answer. This button is what calls the fonction treat_command.
        t = "Soumettre"
        self.submit_button=tk.Button(self,text=t,font=("Arial", 14),command=self.treat_command)
        self.submit_button.pack(pady=10)

    def treat_command(self):
        """Process the answer and move to the next question"""
        command_string = self.answer_entry.get()

        if self.nb == 1:
            self.setup()
            self.graphic_setup()

        elif self.nb == 0:
            self.player = Player(command_string)

        elif  len(command_string) != 0 :
            # Split the command string into a list of words
            list_of_words = command_string.split(" ")

            command_word = list_of_words[0]

            # If the command is not recognized, display an error message
            if command_word not in self.commands:
                w1 = f"\nCommande '{command_word}' non reconnue. "
                w2 = "Entrez 'help' pour voir la liste des commandes disponibles.\n"
                messagebox.showwarning(w1+w2)
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                self.execute_command(command, list_of_words)

        #If the game is not ended, update the graphical interface
        #(does not get the command from the player,
        #it is the push of the submit_button that calls the treat_command)
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
            self.background = PhotoImage(file = self.images[self.player.current_room.name])
            #/self.images[self.player.current_room.name]
            self.image_label.config(image = self.background)
        #Popup (messagebox) if there is a warning
        if self.warning != "" :
            messagebox.showwarning(self.warning)
        self.warning = ""

    def end_game(self):
        """End of game"""
        messagebox.showinfo(self.warning)
        #"Jeu terminé", f"Votre score final est : "#{self.get_score()}/{len(self.questions)}
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
