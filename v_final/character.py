# This file contains the Character class.

from beings import Beings #The parent class of Character
import random
import copy

class Character:
    """
    This class represents a character.

    Attributes:
        name (str): Name of the pnj.
        description (str): The description of the pnj.
        current_room (Room): The current room.
        msgs (list): The list of the messages to print when interracting with the pnj.
        area (list): The list of the rooms that are accessible to the pnj.

    Methods:
        __init__(self, name, description, action, current_room, msgs) : The constructor.
        __str__(self) : The string representation of the command.
        move(self) : Moves the pnj or not.
        get_msg(self) : Print what the pnj has to say.

    """

    def  __init__(self, name, description, current_room, msgs, area):
        Beings.__init__(self, name, current_room)
        self.description = description
        self.msgs = msgs
        self.area = area

    def __str__(self):
        return  "{0} : {1}".format(self.name, self.description)
    
    # Define the move method.
    def move(self): 
        """
        Characters have one chance out of two to go to an adjacent room or not. 
        """
        #The list of the rooms the pnj can go in 
        rooms = copy.copy(self.area)
        rooms.remove(self.current_room)
        
        #The pnj has a 1/3 probability of going in one of those rooms
        if random.randint(0,2) == 1 and rooms != [] and rooms != None:
            room = random.choice(rooms)
            del self.current_room.characters[self.name]
            self.current_room = room
            self.current_room.characters[self.name] = self
            return True
        return False

    def get_msg(self, game):
        #if some conditions are met, a message is unlocked
        if self.name == "mister" :
            if "truc" in game.player.inventory :
                self.msg.insert(0, "\n truc trop super important")
        if self.name == "mister" :
            if "truc" in game.player.inventory :
                game.warning = f"Vous êtes mort."
                game.commands["quit"].action(game.command["quit"], ["quit"], game.command["quit"].numbers)
        #print the messages in a rotating manner
        msg = self.msgs.pop(0)
        game.text = "\n" + msg + "\n" + game.player.current_room.get_long_description() + game.player.get_history(game)
        self.msgs.append(msg) 