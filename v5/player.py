# Define the Player class.
class Player():
    """
    Cette classe représente un joueur. Un joueur est caaractérisé par un nom et le lieu où il se trouve.

    Attributs:
        name (str): Le nom du joueur.
        current_room (Room): Le lieu où le joueur se trouve.

    Methodes:
        __init__(self, name) : Le constructeur.
        move(self, direction) : Change le lieu où est le joueur par le lieu dans la direction donnée et retourne true ssi c'est possible.

    Exemples:

    >>> player = Player("mrtest")
    >>> player.name
    'mrtest'
    >>> type(player.current_room)
    <class 'NoneType'>

    """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())

        # Affiche les lieux déjà visités puis ajoute le lieu présent à l'historique
        self.history.append(next_room)
        self.get_history()

        return True
    
    def get_history(self):
        # Si on est à la case départ on n'affiche pas l'historique
        # Sinon on affiche les pièces déjà visitées 
        #PEUT ETRE LE FAIRE AVEC UN RETOURNE F MAIS JCP COMMENT COMPREHENSION DE CHAINE PEUT ETRE    A FIARE 
        if len(self.history) != 1:
            print("Vous avez déjà visité les pièces suivantes dans cet ordre :")
            for room in self.history[:-1]:
                print("-", room.description.strip("dansdevant "))
            print()
        return True



    