"""This file contains the Inventory class."""

# pylint: disable=too-few-public-methods
class Inventory:
    """
    This class represents an inventory. 
    An inventory is composed of a name, a description and its weight.

    Attributes:
        thing (Room or Player): The place or player to do the inventory about.

    Methods:
        get_inventory(thing) : Print the list of what is in the inventory.

    """
    @staticmethod
    def get_inventory(game, thing):
        """Print the list of what is in the inventory.
        Be it the inventory of the player or the inventory of the room."""
        try :
            thing.characters
        except AttributeError :
            if thing.inventory == {} :
                game.text = "\nVotre inventaire est vide, vous ne possédez rien.\n"
                game.text += game.player.current_room.get_long_description()
                game.text += game.player.get_history()
            else :
                l_item = ''
                total_weight = 0
                for i in thing.inventory.values() :
                    l_item = l_item + '- '
                    l_item += "{0} : {1} ({2} kg)".format(i.name, i.description, i.weight) + '\n'
                    total_weight = total_weight + i.weight
                game.text = f"\nVous disposez des items suivants :\n{l_item}"
                game.text += f"\n Le poids total de ce que vous portez est de {total_weight} kg.\n"
                game.text += game.player.current_room.get_long_description()
                game.text += game.player.get_history()
        else :
            if thing.inventory == {} and thing.characters == {}  :
                game.text = "\nIl n'y a rien d'autre ici.\n"
                game.text += game.player.current_room.get_long_description()
                game.text += game.player.get_history()
            else :
                l = ''
                for i in thing.inventory.values() :
                    l = l + '- ' + f"{0} : {1} ({2} kg)".format(i.name, i.description, i.weight) + '\n'
                for c in thing.characters.values() :
                    l = l + '- ' + f"{0} : {1}".format(c.name, c.description) + '\n'
                game.text = f"\nOn voit :\n{l}" + game.player.current_room.get_long_description() + game.player.get_history()
