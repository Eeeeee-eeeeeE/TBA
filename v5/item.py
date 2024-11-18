# Define the Item class.

class Item:
    """

    """

    # Define the constructor. 
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight
    
    # The string representation of the command.
    def __str__(self):
        return  "{0} : {1} ({2} kg)".format(self.name, self.description, self.weight)

