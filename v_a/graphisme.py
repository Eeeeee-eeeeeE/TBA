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
        
        erlenmeyer = Room("Erlenmeyer", "une salle barba-intrigante et terrifiante. Vous êtes sur une table parsemée d'erlenmeyers qui vous semle géants et de poils de barbi-dur.")
        self.rooms.append(erlenmeyer)
        self.images['Erlenmeyer'] = 'Erlenmeyer.png'
        realisation = Room("Realisation", "une salle très haute de plafond. Un escalier en collimasson aux marches de géant et parcemé de moutons de poussière de la taille de votre barba-bras se dessine devant vous.")
        self.rooms.append(realisation)
        self.images['Realisation'] = 'Realisation.png'
        wardrob_o = Room("Wardrob_o", "une salle avec une armoire au nord qui cache une porte dérobée.")
        self.rooms.append(wardrob_o)
        self.images['Wardrob_o'] = 'Wardrob_o.png'
        wardrob_e = Room("Wardrob_e", "la partie de droite d'une grande salle lugubre sans fenêtre.")
        self.rooms.append(Wardrob_e)
        self.images['Wardrob_e'] = 'Wardrob_e.png'
        enigma = Room("Enigma", "une salle modeste. Devant vous se tient un petit barba-monsieur à l'air malicieux.")
        self.rooms.append(enigma)
        self.images['Enigma'] = 'Enigma.png'
        nothing = Room("Nothing", "une salle barba-vide.")
        self.rooms.append(nothing)
        self.images['Nothing'] = 'Nothing.png'
        cyclop = Room("cyclop", "un terrier sombre.")
        self.rooms.append(cyclop)
        self.images['cyclop'] = 'Cyclop.png'
        farm = Room("farm", "une partie du terrier où s'entassent des caméléons. Il semblerait que ce soit un élevage fait par, barba-barbarre, la marmotte borgne, elle les sort 2 fois par jour.")
        self.rooms.append(farmdowtown)
        self.images['farm'] = 'farm.png'

        brokenglass = Room("Brokenglass", "une salle dont le sol est couvert par une écatombe de fioles brisées. Le reflet du soleil sur ces fragments de verre brisé donne des couleurs irisées aux murs telle une mosaique des temps antiques.")
        self.rooms.append(brokenglass)
        self.images['Brokenglass'] = 'Brokenglass.png'
        glitter = Room("Glitter", "une salle où se dresse au milieu une statue à paillettes rose. Cette statue représente un homme, environ la quarantaine et demi, barbu de 12 jours, petites lunettes losange sur un nez imposant, une interminablement longue blouse de scientifique sur le dos, et deux yeux roses.")
        self.rooms.append(glitter)
        self.images['Glitter'] = 'Glitter.png'
        evil = Room("Evil", "un bureau sombre. Un vilain monsieur (un humain) est concentré. Des shémas de l'intestin grèle des barba-collègues sont dessinés sur les feuilles de son bureau.")
        self.rooms.append(evil)
        self.images['Evil'] = 'Evil.png'
        potionbook = Room("Potionbook", "une bibliothèque barba-luggubre. Des grimoires s'entassent un peu partout, c'est le barba-foutoir.")
        self.rooms.append(potionbook)
        self.images['Potionbook'] = 'Potionbook.png'
        musty = Room("Musty", "une petit pièce humide et sombre. Les murs sont tapis d'une couche barba-épaisse de moisissure.")
        self.rooms.append(musty)
        self.images['Musty'] = 'Musty.png'
        out = Room("Out", "une large pièce acceuillante vu sur un jardin. Il y fait un peu frais, le vent s'engouffre par le pas d'une petite porte dissimulée.")
        self.rooms.append(out)
        self.images['Out'] = 'Out.png'

        tree = Room("Tree", "une parcelle de terre sur laquelle s'élève un acassia centenaire. Gloire de la nature et de Gaya, son tron est épais comme une maison, ses branches ont la circonférence d'une centrale nucléaire et ses feuilles sont petite comme des petites libellules.  Malheureseument pour les dryades, cet arbre garde la trace de son exploitation : des balafres multiples décorent son tron.")
        self.rooms.append(tree)
        self.images['Tree'] = 'Tree.png'
        monkey = Room("Monkey", "l'arbre, devant vous il y a une cabanne. Derrière celle-ci est caché un barba-singe qui semble s'être échappé de la salle des essais cliniques.")
        self.rooms.append(monkey)
        self.images['Monkey'] = 'Monkey.png'
        bread = Room("Bread", "une étendu d'herbre. Chaque brin d'herbe vous arrive à l'épaule. Une miette de pain est juste devant vous.")
        self.rooms.append(bread)
        self.images['Bread'] = 'Bread.png'
        storage = Room("Storage", "une grange.")
        self.rooms.append(storage)
        self.images['Storage'] = 'Storage.png'

        # Create exits for rooms

        erlenmeyer.exits = {"N" : None, "E" : None, "S" : wardrob_e, "O" : realisation, "U" : None, "D" : None}
        realisation.exits = {"N" : None, "E" : brokenglass, "S" : None , "O" : None, "U" : None, "D" : None}
        wardrob_o.exits = {"N" : glitter, "E" : wardrob_e, "S" : None, "O" : None, "U" : None, "D" : None}
        wardrob_e.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : enigma}
        enigma.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : cyclop}
        nothing.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : wardrob_o, "D" : None}
        cyclop.exits = {"N" : None, "E" : farm, "S" : None, "O" : None, "U" : None, "D" : None}
        farm.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : nothing, "D" : None}
        
        brokenglass.exits = {"N" : None, "E" : None, "S" : None, "O" : glitter, "U" : None, "D" : None}
        glitter.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : evil, "D" : out}
        evil.exits = {"N" : None, "E" : potionbook, "S" : None, "O" : None, "U" : None, "D" : glitter}
        potionbook.exits = {"N" : None, "E" : None, "S" : None, "O" : evil, "U" : None, "D" : None}
        musty.exits = {"N" : None, "E" : None, "S" : None, "O" : out, "U" : brokenglass, "D" : None}
        out.exits = {"N" : None, "E" : musty, "S" : None, "O" : tree, "U" : glitter, "D" : None}
        
        tree.exits = {"N" : None, "E" : out, "S" : bread, "O" : None, "U" : monkey, "D" : None}
        monkey = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : tree}
        bread = {"N" : tree, "E" : None, "S" : None, "O" : storage, "U" : None, "D" : None}
        storage = {"N" : lake, "E" : bread, "S" : None, "O" : None, "U" : None, "D" : None}
        lake = {"N" : None, "E" : tree, "S" : storage, "O" : None, "U" : None, "D" : None}

        #Setup items of the rooms
        
        armoire = Item("armoire", "l'armoire entrouverte", 10000)
        wardrob_o.inventory["armoire"] = armoire
        cameleon = Item("cameleon", "un bébé caméléon", 50)
        farm.inventory["cameleon"] = cameleon

        bout_verre = Item("bout_verre", "une poignée de mini bouts de verres aussi jolis que des diaments", 0.2)
        brokenglass.inventory["bout_verre"] = bout_verre
        page = Item("page", "un bout de page déchiré avec griffonné dessus une recette de barba-pancake !grandissant! :\nfarine, eau, levure, banane", 0.2)
        potionbook.inventory["page"] = page

        seve = Item("seve", "une goutte de sève (issue du tronc)", 0.002)
        tree.inventory["seve"] = seve
        banane = Item("banane", "une barba-banane naine", 0.08)
        monkey.inventory["banane"] = banane
        pomme = Item("pomme", "un quartier de pomme ", 0.03)
        storage.inventory["pomme"] = pomme
        farine = Item("farine", "un petit reste de farine", 0.03)
        storage.inventory["farine"] = farine
        levure = Item("levure", "un petit reste de levure", 0.0005)
        storage.inventory["levure"] = levure
        sucre = Item("sucre", "une bonne poignée de grains de sucres", 0.0005)
        storage.inventory["sucre"] = sucre
        pomme = Item("pomme", "une pomme entière", 0.0005)
        storage.inventory["pomme"] = pomme
        eau = Item("eau", "une demi goutte d'eau", 0.005)
        lake.inventory["eau"] = eau


        #Setup characters of the rooms

        barba_petit = Character("barba_petit", "un barbapapa qui n'arrête pas de changer de forme", realisation, ["Bonjour", "Qui es-tu ?\nA : Je suis comme toi, je suis un barbapapa qui a rétréci.\nB : Je suis barba-perdu."], [realisation])
        realisation.characters["barba_petit"] = barba_petit
        mister = Character("mister", "un mister étrange", wardrob_e, ["hola"], [wardrob_e, wardrob_o])
        wardrob_e.characters["mister"] = mister
        marmotte = Character("marmotte", "un marmotte balèze", cyclop, ["A : Tu veux te battre avec moi ?\n B: Ou coopère et enfonce toi encore plus dans le terrier"], [cyclop, farm])
        cyclop.characters["mister"] = marmotte

        vilain = Character("vilain", "un monsieur à l'air vilain", evil, ["Hum", "Qui va là ? (il vous regarde droit dans les yeux mais ne vous voit pas grâce au caméléon qui vous rend invisible) Bon je ne voit personne."], [evil])
        evil.characters["vilain"] = vilain

        barba_monsieur = Character("barba_monsieur", "le barba-monsieur à l'air malicieux", enigma, ["Vous m'avez réveillé barba-fillou; Votre survie dépend maintenant de la réponse à cette question : Qu'est-ce qui est petit et qui barba-attend ? \na : Barbotine\nb : Barba-jonathan\nc : Vous\nd : Jonathan"], [enigma])
        enigma.characters["barba_monsieur"] = barba_monsieur

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
