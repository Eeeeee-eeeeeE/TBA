from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from inventory_caracter import InventoryCaracter
from character import Caracter 

import tkinter as tk
from tkinter import messagebox

import csv 

DEBUG = True

# Classe de base pour la logique du jeu
class GameLogic():

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.knowndirections = set() #ou attribut de clasee JE SAIS PAS???

        self.text = ""
        self.warning = ""
        self.nb = 0 #nb intructions

    self.donnees = "donnees.csv" #[game.player.name, game.player.current_room, gameplayer.history, game.player.inventory_carcater, game.knowndirection, game.rooms.numeroi.name, game.room.numeoi.description, game.room.niumeroi.exitsN,game.room.niumeroi.exitsS, game.room.niumeroi.exitsE, game.room.niumeroi.exitsO, game.room.niumeroi.exitsU, game.room.niumeroi.exitsD, game.room.ni.nameitem, game.room.ni.descriptionitem, game.room.ni.poiditem, game.room.ni.manecharact, game.room.ni.descriptinocaract, game.room.ni.roomcharact, game.room.ni.paroles ]
                            
    # Setup the game
    def setup(self):

        with open(self.donnees, mode='r', encoding='utf8') as f:
            r = csv.reader(f)
            l = list(r)
            if (len(l)==0):

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
                i = 1
                while l[5][i] != '\0' : 
                    l[5][i] = Room(l[5][i], l[6][i])
                    self.rooms.append(l[5][i])
                    i += 1

                # Create exits for rooms

                while l[5][i] != '\0' : #dans la liste normalement mtn c des obj pas des noms
                    l[5][i].exits = {"N" : l[6][i], "E" : l[7][i], "S" : l[8][i], "O" : l[9][i], "U" : l[10][i], "D" : l[11][i]}
                    i += 1
                    
                #Creation items
                i=0
                while l[5][i] != '\0': 
                    l[5][i].inventory_caracter = InventoryCaracter('Room')
                    j = 0
                    mots = ''
                    inventairename = []
                    while l[20][i][j] != '\0' : #les paroles sont dans la case comme tel "inventory1 \inventory2"
                        mots = mots + l[20][i][j]
                        if l[20][i][j] == '\' :
                            inventairename.append(mots)
                            mots = ''
                            j += 1
                    j = 0
                    mots = ''
                    inventairedescrib = []
                    while l[20][i][j] != '\0' : #les paroles sont dans la case comme tel "inventory1 \inventory2"
                        mots = mots + l[20][i][j]
                        if l[20][i][j] == '\' :
                            inventairedescrib.append(mots)
                            mots = ''
                            j += 1 
                    j = 0
                    mots = ''
                    inventairepoid = []
                    while l[20][i][j] != '\0' : #les paroles sont dans la case comme tel "inventory1 \inventory2"
                        mots = mots + l[20][i][j]
                        if l[20][i][j] == '\' :
                            inventairepoid.append(mots)
                            mots = ''
                            j += 1  
                    for j in range(0, len(inventairename)) :
                        l[5][i].inventory_caracter.inventory_dict = {inventairename[j] : Item(inventairename[j], inventairedescrib[j], float(inventairepoid[j])}
                    j = 0
                    mots = ''
                    charactersname = []
                    while l[20][i][j] != '\0' : #les paroles sont dans la case comme tel "balabal la \ blabla2"
                        mots = mots + l[20][i][j]
                        if l[20][i][j] == '\' :
                            charactersname.append(mots)
                            mots = ''
                        j += 1 
                    j = 0
                    mots = ''
                    charactersdescrip = []
                    while l[20][i][j] != '\0' : #les paroles sont dans la case comme tel "balabal la \ blabla2"
                        mots = mots + l[20][i][j]
                        if l[20][i][j] == '\' :
                            charactersdescrip.append(mots)
                            mots = ''
                        j += 1 
                    j = 0
                    mots = ''
                    lstparoles = []
                    while l[20][i][j] != '\0' : #les paroles sont dans la case comme tel "balabal la \ blabla2"
                        mots = mots + l[20][i][j]
                        if l[20][i][j] == '\' :
                            lstparoles.append(mots)
                            mots = ''
                        j += 1 
                    for j in range (0, len(charactersname)):
                        k = 0
                        mots = ''
                        paroles = []
                        while lstparoles[j][k] != '\0' : #les paroles sont dans la case comme tel "balabal la \ blabla2"
                            mots = mots + lstparoles[j][k]
                            if lstparoles[j][k] == '/' :
                                paroles.append(mots)
                                mots = ''
                            k += 1 
                        l[5][i].inventory_caracter.caracter_dict = {charactersname[j]: Item(charactersname[j], charactersdescrip, l[5][i], paroles}
                    i += 1

                #Création/Setup des directions connues PAS SURE IL A DIT DEUX LIGNES 
                self.knowndirections = set(self.rooms[0].exits.keys())

                # Setup player and starting room (et l'historique)

                self.player.current_room = l[1][0]
                self.player.history.append(self.player.current_room)
                self.player.inventory_caracter = InventoryCaracter('Player')
                #a faire pareil que l'auitre inventory 
                self.text = self.player.current_room.get_long_description()
            
            else :

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

                self.player.current_room = grassalone
                self.player.history.append(grassalone)
                self.player.inventory_caracter = InventoryCaracter('Player')
                self.text = self.player.current_room.get_long_description()

    def get_current_text(self):
        """Retourne la question actuelle"""
        if self.nb == 0:
            self.text = "\nEntrez votre nom: "
        elif self.nb == 1:
            self.text = f"\nBienvenue {self.player.name} dans ce jeu d'aventure !\nEntrez 'help' si vous avez besoin d'aide.\n"
        return self.text #DANS LES FICHIERS QUAND PRINT REMPLACER PAR MODIF GAME.TEXT

    def treat_command(self, command, list_of_words):
        """Vérifie la réponse et met à jour le score"""
        command.action(self, list_of_words, command.number_of_parameters)


# Classe de l'interface graphique avec tkinter
class GameApp(tk.Tk, GameLogic):
    def __init__(self):
        tk.Tk.__init__(self)
        GameLogic.__init__(self)
        self.title("Jeu d'Aventure")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        """Créer les widgets de l'interface"""
        # Zone de texte pour afficher le text
        self.text_label = tk.Label(self, text=self.get_current_text(), font=("Arial", 14), wraplength=350)
        self.text_label.pack(pady=20)

        # Zone de teste pour entrer la réponse
        self.answer_entry = tk.Entry(self, font=("Arial", 14), width=30)
        self.answer_entry.pack(pady=10)

        # Bouton pour soumettre la réponse
        self.submit_button = tk.Button(self, text="Soumettre", font=("Arial", 14), command=self.process_command)
        self.submit_button.pack(pady=10)

        # Bouton pour quitter le jeu
        #self.quit_button = tk.Button(self, text="Quitter", font=("Arial", 14), command=self.quit_game)
        #self.quit_button.pack(pady=10)

    def process_command(self):
        """Soumettre la réponse et passer à la question suivante"""
        command_string = self.answer_entry.get()

        if self.nb == 1:
            self.setup() 
        
        elif self.nb == 0:
            self.player = Player(command_string)

        elif  len(command_string) != 0 :
            # Split the command string into a list of words
            list_of_words = command_string.split(" ")

            command_word = list_of_words[0]

            # If the command is not recognized, print an error message
            if command_word not in self.commands.keys():
                messagebox.showwarning(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                self.treat_command(command, list_of_words)


        if not self.finished:
            self.update_widgets()
        else:
            self.end_game()

    def update_widgets(self):
        """Met à jour la question affichée"""
        self.nb = self.nb + 1
        self.answer_entry.delete(0, tk.END)  # Effacer l'entrée de la réponse
        self.text_label.config(text=self.get_current_text())
        if self.warning != "" :
            messagebox.showwarning(self.warning)
        self.warning = ""


    def end_game(self):
        """Fin du jeu, affiche le score"""
        messagebox.showinfo("Jeu terminé", f"Votre score final est : ")#{self.get_score()}/{len(self.questions)}
        self.quit_game()

    def quit_game(self):
        """Quitte le jeu"""
        self.destroy()

# Lancer le jeu
def main():
    jeu = GameApp()
    jeu.mainloop()

if __name__ == "__main__":
    main()