# Define the Player class.
class Player():
    
 """
    This class represents a player. A player is characterized by a name and the location where he is located.

    Attributes:
        name (str): The player's name.
        current_room (Room): The place where the player is located.

    Methods:
        __init__(self, name): The constructor.
        move(self, direction): Changes the location where the player is to the location in the given direction (and returns true) if possible.
    
    Examples:

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

    
