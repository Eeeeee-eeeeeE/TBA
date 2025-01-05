# Description: Game class and Graphic class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from inventory_caracter import InventoryCaracter
from character import Caracter 

import tkinter as tk
from tkinter import messagebox, PhotoImage

DEBUG = True

# Game class as written in class
class Game():

    # The constructor.
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.possible_direction = set() 

        self.text = "" #the text to display on the graphical interface
        self.warning = ""
        #SCORE EN FONCTION DU NB INTERACTION 
        self.nb = 0 #nb of interactions with the player 
        self.images = dict([('begining', 'begining.png')])

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

        wardrobeO = Room("WardrobeO", "la partie de gauche d'une grande salle lugubre sans fenêtre.")
        self.rooms.append(wardrobeO)
        wardrobeE = Room("WardrobeE", "la partie de droite d'une grande salle lugubre sans fenêtre.")
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

        #Setup items of the rooms
        truc = Item("truc", "un truc étrange", 50)
        wardrobeO.inventory["truc"] = truc
        brindille = Item("brindille", "un baton de bois à votre echelle", 0.2)
        wardrobeO.inventory["brindille"] = brindille

        #Setup characters of the rooms
        mister = Character("mister", "un mister étrange", wardrobeE, ["hola"], [wardrobeE, wardrobeO])
        wardrobeE.characters["mister"] = mister
        harry = Character("harry", "un lapin ferroce", wardrobeE, ["tu es à croquer", "j t'aime bien (mm si je pref les carottes)"], [wardrobeE, wardrobeO])
        wardrobeE.characters["harry"] = harry

        #Set of all the possible directions
        self.possible_direction = {k for r in self.rooms for k in r.exits.keys() }
        
        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "), wardrobeE)

        #A ENLEVER POUR TESTER
        #Setup the text to display
        self.text = self.player.current_room.get_long_description()

    #Returns the current question
    def get_current_text(self):
        if self.nb == 0:  #if it is the first interaction of the game
            self.text = "\nEntrez votre nom: "
        elif self.nb == 1: #if it is the second interaction of the game
            self.text = f"\nBienvenue {self.player.name} dans ce jeu d'aventure !\nEntrez 'help' si vous avez besoin d'aide.\n"
        return self.text #DANS LES FICHIERS QUAND PRINT REMPLACER PAR MODIF GAME.TEXT
    
    #If the command is recognized (verified in treat_command), execute it (used in the methode treat_command of the Class Graphic)
    def execute_command(self, command, list_of_words):
        command.action(self, list_of_words, command.number_of_parameters)


# Class of the graphical interface with tkinter
class Graphic(tk.Tk, GameLogic):
    # The constructor.
    def __init__(self):
        tk.Tk.__init__(self)
        GameLogic.__init__(self)
        self.title("Jeu d'Aventure")
        self.geometry("800x600")
        self.background = PhotoImage(file = self.images["begining"])
        self.create_widgets()

    #Create the widgets of the interface
    def create_widgets(self):
        # Background
        self.image_label = tk.Label(self, image = self.background)
        self.image_label.place(x=0, y=0, relwidth = 1, relheight = 1)
        # Text box to display text
        self.text_label = tk.Label(self, text=self.get_current_text(), font=("Arial", 14), wraplength=350)
        self.text_label.pack(pady=20)
        #Text area to enter the response
        self.answer_entry = tk.Entry(self, font=("Arial", 14), width=30)
        self.answer_entry.pack(pady=10)
        # Button to submit the answer. This button is what calls the fonction treat_command. 
        self.submit_button = tk.Button(self, text="Soumettre", font=("Arial", 14), command=self.treat_command)
        self.submit_button.pack(pady=10)

    #Process the answer and move to the next question
    def treat_command(self):
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
                self.treat_command(command, list_of_words)

        #If the game is not ended, update the graphical interface 
        #(does not get the command from the player, it is the push of the submit_button that calls the treat_command)
        if not self.finished:
            self.update_widgets()
        else:
            self.end_game()

    #Updates the displayed question
    def update_widgets(self):
        #increases the numbers of interactions
        self.nb = self.nb + 1
        # Clear the response entry (clear what was written by the player)
        self.answer_entry.delete(0, tk.END)
        #Shows the new text / question 
        self.text_label.config(text=self.get_current_text())
        #New image of the current room in the background 
        self.background = PhotoImage(file = self.images[self.player.currentroom.name])
        self.image_label = tk.Label(self, image = self.background)
        #Popup (messagebox) if there is a warning
        if self.warning != "" :
            messagebox.showwarning(self.warning)
        self.warning = ""

#OBLIGATOIRE : POUVOIR PERDRE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #End of game
    def end_game(self):
        messagebox.showinfo(self.warning)#"Jeu terminé", f"Votre score final est : "#{self.get_score()}/{len(self.questions)}
        self.quit_game()

    #Quit the game permanently
    def quit_game(self):
        self.destroy()

# Start the game
def main():
    # Create a game object and play the game
    jeu = Graphic()
    #displays the main window on the screen and then waits for the user to take an action.
    jeu.mainloop()

if __name__ == "__main__":
    main()