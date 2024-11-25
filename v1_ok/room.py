# Define the Room class.

class Room:
    """
    This class represents a place. A place is composed of a name, a description, a direction.

    Attributes:
        name (str): The name of the place.
        description (str): The description of the place.
        exits (dict): The exits of the place.

    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : Returns the adjacent place in the given direction if it exists.
        get_exit_string(self) : Returns a character string with the exits of the place.
        get_long_description(self) : Returns a description of the place with the place's description and the outputs of the place.

    Examples:

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
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
