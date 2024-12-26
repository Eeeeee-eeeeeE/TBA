import random

# Define the Character class.
class Caracter():
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
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.current_room = current_room
        self.description = description
        self.msgs = msgs
    
    def __str__(self):
        return  "{0} : {1}".format(self.name, self.description)

    # Define the move method.
    def move(self): 
        
        rooms = []
        for room in self.current_room.exits.values():
            if room is not None:
                rooms.append(room)

        if random.random()%2 == 1 and rooms != []:
            room = random.choice(rooms)
            del self.current_room.inventory_caracter.caracter_dict[self.name]
            self.current_room = room
            self.current_room.inventory_caracter.caracter_dict[self.name] = self
            return True
        return False
    
    #A FAIRE PARLER INTERRESSANT QUE QUAND UN ITEM TROUVE
    def get_msg(self, game):
        msg = self.msgs.pop(0)
        game.text = "\n" + msg + "\n" + game.player.current_room.get_long_description() + game.player.get_history(game)
        self.msgs.append(msg) 


    