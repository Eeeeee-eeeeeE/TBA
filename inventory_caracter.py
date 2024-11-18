# Define the Inventory&Caracter class.

class InventoryCaracter:
    """

    """
    # Define the constructor. 
    def __init__(self, type):
        self.inventory_dict = {}
        self.caracter_dict = {}
        self.type = type

    def get_inventory(self, game):
        if len(self.inventory_dict) == 0 and len(self.caracter_dict) == 0:
            if self.type == 'Player':
                game.text = "\nVotre inventaire est vide, vous ne possédez rien.\n" + game.text
            else:
                game.text = "\nIl n'y a rien d'autre ici.\n" + game.text
        else: 
            if self.type == 'Player':
                game.text = "\nVous disposez des items suivants :\n"
            else:
                game.text = "\nIl y a :\n"
            for item_pnj in (self.inventory_dict.values() or self.caracter_dict.values()):
                game.text = game.text + "- " + item_pnj.__str__()
            game.text = game.text + "\n" + game.player.current_room.get_long_description() + game.player.get_history(game)

