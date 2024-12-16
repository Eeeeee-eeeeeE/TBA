# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
# The MSG2 variable is used when the command go is used with an invalid direction.
MSG2 = "\nLa direction '{direction}' non reconnue."
# The MSG3 variable is used when the command back is used with an empty history.
MSG3 = "\nL'historique est vide."
# The MSG4 variable is used when the command take is used with a wrong object.
MSG4 = "\nL'objet '{item}' n'est pas dans {inventaire_ou_pièce}.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        
        #Remplace les differentes expressions possibles d'une même commande par le nom de la commande
        if direction in ("n", "Nord", "nord", "NORD") :
            direction = "N"
        elif direction in ("s", "Sud", "sud", "SUD") :
            direction = "S"
        elif direction in ("e", "Est", "est", "EST") :
            direction = "E"
        elif direction in ("o", "Ouest", "ouest", "OUEST") :
            direction = "O"
        elif direction in ("u", "Up", "up", "UP") :
            direction = "U"
        elif direction in ("d", "Down", "down", "DOWN") :
            direction = "D"

        #if the direction is valid
        if direction in game.possible_direction :
            # Move the player in the direction specified by the parameter.
            player.move(direction)
        else :
            command_word = list_of_words[0]
            print(MSG2.format(direction=direction))
            print(game.player.current_room.get_long_description())
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    def back(game, list_of_words, number_of_parameters):
        """
        If possible, the player goes back to the previous room.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if(len(game.player.history) > 0):
            game.player.current_room= game.player.history.pop()
            print(game.player.current_room.get_long_description())
            if(len(game.player.history) > 0):
                print(game.player.get_history())
            return True
        else :
            print(MSG3)
            print(game.player.current_room.get_long_description())
            return True

    def look(game, list_of_words, number_of_parameters):
        """
        Print the list of the items in the room.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(game.player.current_room.get_inventory())
        return True

    def take(game, list_of_words, number_of_parameters):
        """
        Take an item present in the room and put it in the player's inventory.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Get the object from the list of words.
        object = list_of_words[1]

        #If the object is not in the room, print an error message and return False..
        if object not in game.player.current_room.inventory :
            print(MSG4.format(item=object, inventaire_ou_pièce='la pièce'))
            return False
        
        # If possible, put the object in the inventory.
        game.player.inventory[object] = print(object)
        game.player.current_room.inventory.remove(object)
        print("\nVous avez pris l'object '{0}'.\n".format(object))
        return True

    def drop(game, list_of_words, number_of_parameters):
        """
        Drop an item present in the player's inventory and put it in the current room.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Get the object from the list of words.
        object = list_of_words[1]

        #If the object is not in the player's inventory, print an error message and return False.
        if object not in game.player.inventory :
            print(MSG4.format(item=object, inventaire_ou_pièce="l'inventaire"))
            return False
        
        # If possible, droop the object in the room.
        game.player.current_room.inventory.add(object)
        del game.player.inventory[object]
        print("\nVous avez déposé l'object '{0}'.\n".format(object))
        return True

    def check(game, list_of_words, number_of_parameters):
        """
        See what is in the player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(game.player.get_inventory())
        return True