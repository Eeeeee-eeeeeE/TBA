# This file contains the Character class.

from beings import Beings #The parent class of Character

class Character:
    """
    This class represents a character.

    Attributes:
        name (str): Name of the pnj.
        description (str): The description of the pnj.
        current_room (Room): The current room.
        msgs (list): The list of the messages to print when interracting with the pnj.

    Methods:
        __init__(self, name, description, action, current_room, msgs) : The constructor.
        __str__(self) : The string representation of the command.
        move(self) : Moves the pnj or not.
        get_msg(self) : Print what the pnj has to say.

    """

    def  __init__(self, name, description, current_room, msgs):
        Beings.__init__(self, name, current_room)
        self.description = description
        self.msgs = msgs

    def __str__(self):
        return  "{0} : {1}".format(self.name, self.description)
    
    # Define the move method.
    def move(self): 
        """
        Characters have one chance out of two to go to an adjacent room or not. 
        """
        rooms = []
        for room in self.current_room.exits.values():
            if room is not None:
                rooms.append(room)

        half = [0, 1]
        if random.choice(half) and rooms != []:
            room = random.choice(rooms)
            del self.current_room.characters[self.name]
            self.current_room = room
            self.current_room.characters[self.name] = self
            return True
        return False

    def get_msg(self):
        msg = self.msgs.pop(0)
        print("\n" + msg + "\n")
        self.msgs.append(msg) 

    