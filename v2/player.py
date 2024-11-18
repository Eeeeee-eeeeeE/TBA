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
        return True

    