# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = dict()
    
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
    
    def get_inventory(self):
        if self.inventory == {} :
            return f"Votre inventaire est vide."
        else :
            l_item = ''
            for i in self.inventory :
                l_item = l_item + '- ' + print(i) + '\n'
            return f"Vous disposez des items suivants :\n{l_item}"