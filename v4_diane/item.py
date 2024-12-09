class Item:
    """
    This class represents an item. An item is composed of a name, a description and its weight.

    Attributes:
        name (str): The name of the item/object.
        description (str): The description of the item.
        weight (int): The weight of the item.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.

    """

    # The constructor.
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight
    
    # The string representation of the item.
    def __str__(self):
        return  "{0} : {1} ({2} kg)".format(self.name, self.description, self.weight)

    