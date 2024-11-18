# Define the Inventory class.

class Inventory:
    """

    """
    # Define the constructor. 
    def __init__(self, type):
        self.dict = {}
        self.type = type

    def get_inventory(self):
        if len(self.dict) == 0:
            if self.type == 'Player':
                print("\nVotre inventaire est vide, vous ne possédez rien.\n")
            else:
                print("\nIl n'y a rien d'autre ici.\n")
        else: 
            if self.type == 'Player':
                print("\nVous disposez des items suivants :")
            else:
                print("\nIl y a :")
            for item in self.dict.values():
                print("- ", end='')
                print(item)
            print()

