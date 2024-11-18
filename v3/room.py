# Define the Room class.

class Room:
    """
    Cette classe représente un lieu. Un lieu est composé d'un nom, d'une descriptions et de sorties.

    Attributs:
        name (str): Le nom du lieu.
        description (str): La description du lieu.
        exits (dict) : Les sorties du lieu.

    Methodes:
        __init__(self, name, description) : Le constructeur.
        get_exit(self, direction) : Retourne le lieu dans la direction donnée si il existe.
        get_exit_string(self) : Retourne une chaîne de caractère avec les sorties du lieu.
        get_long_description(self) : Retourne une description du lieu avec la description et les sorties du lieu.

    Exemples:

    >>> room = Room("test", "dans un espace de test.")
    >>> room.name
    'test'
    >>> room.description
    'dans un espace de test.'
    >>> type(room.exits)
    <class 'dict'>
    >>> room.exits
    {}

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
