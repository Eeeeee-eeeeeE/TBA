# This file contains the Inventory class.

class Inventory:
    """
    This class represents an inventory. An inventory is composed of a name, a description and its weight.

    Attributes:
        thing (Room or Player): The place or player to do the inventory about.

    Methods:
        get_inventory(thing) : Print the list of what is in the inventory.

    """
    
    def get_inventory(thing):
        try :
            thing.characters
        except AttributeError :
            if thing.inventory == {} :
                return f"\nVotre inventaire est vide.\n"
            else :
                l_item = ''
                total_weight = 0
                for i in thing.inventory.values() :
                    l_item = l_item + '- ' + "{0} : {1} ({2} kg)".format(i.name, i.description, i.weight) + '\n'
                    total_weight = total_weight + i.weight
                return f"\nVous disposez des items suivants :\n{l_item} \n Le poids total de ce que vous portez est de {total_weight} kg.\n" 
        else :
            if thing.inventory == dict() and thing.characters == dict()  :
                return f"\nIl n'y a rien ici.\n"
            else :
                l = ''
                for i in thing.inventory.values() :
                    l = l + '- ' + "{0} : {1} ({2} kg)".format(i.name, i.description, i.weight) + '\n'
                for c in thing.characters.values() :
                    l = l + '- ' + "{0} : {1}".format(c.name, c.description) + '\n'
                return f"\nOn voit :\n{l}"
        
            