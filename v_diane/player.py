# This file contains the Player class.

from beings import Beings #The parent class of Player

class Player():
    """
    This class represents a player.

    Attributes:
        name (str): Name of the player.
        current_room (Room): The current room.
        history (list) : The rooms where the player has already been.
        inventory(dict) : The inventory of the player.

    Methods:
        __init__(self, name, current_room) : The constructor.
        move(self, direction) : Moves the player in the given direction, if possible.
        get_history(self) : Return the history of where the player has been.

    """

    # Define the constructor.
    def __init__(self, name, current_room):
        Beings.__init__(self, name, current_room)
        self.history = []
        self.inventory = dict()
        self.inventory_weight_max = 40 
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        #add current_room to the hitory before moving to another room
        self.history.append(self.current_room)
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        #print the history
        print(self.get_history())
        return True

    def get_history(self):
        l_room =''
        for r in self.history :
            description_split =r.description.split('.')
            l_room = l_room + '- ' + description_split[0] + '\n'
        return f"Vous avez déjà visité les pièces suivantes:\n{l_room}"