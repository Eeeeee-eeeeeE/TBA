# Define the Inventory&Caracter class.

class InventoryCaracter:
    """

    """
    # Define the constructor. 
    def __init__(self, type):
        self.inventory_dict = {}
        self.caracter_dict = {}
        self.type = type

    def get_inventory(self):
        if len(self.inventory_dict) == 0 and len(self.caracter_dict) == 0:
            if self.type == 'Player':
                print("\nVotre inventaire est vide, vous ne possédez rien.\n")
            else:
                print("\nIl n'y a rien d'autre ici.\n")
        else: 
            if self.type == 'Player':
                print("\nVous disposez des items suivants :")
            else:
                print("\nIl y a :")
            for item_pnj in (self.inventory_dict.values() or self.caracter_dict.values()):
                print("- ", end='')
                print(item_pnj)
            print()

