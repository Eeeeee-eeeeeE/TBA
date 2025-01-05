# This file contains the Beings class.

class Beings:
    """
    This class represents a being. It is the parent class of Character and Player.

    Attributes:
        name (str): Name of the being.
        current_room (Room): The current room.

    Methods:
        __init__(self, current_room) : The constructor.
    """

    def  __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    