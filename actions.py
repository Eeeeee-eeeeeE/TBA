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
#
MSG2 = "\nLa commande '{command_word}' ne peut pas prendre '{entered_world}' en paramêtre.\n\n" #besoin deux \n POURQUOI
#
MSG3 = "\nLa commande '{command_word}' ne peut pas être utilisée dans cette situation.\n"

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
        from game import DEBUG

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

        #Si la direction entrée n'est pas connue, affichage d'un message d'erreur
        if direction not in game.knowndirections :
            command_word = list_of_words[0]
            print(MSG2.format(command_word=command_word, entered_world=direction), end='')
            print(player.current_room.get_long_description())
            return False
        # Move the player in the direction specified by the parameter.
        player.move(direction)

        # Fait bouger les pnj
        for knownroom in game.rooms:
            for caracter in knownroom.inventory_caracter.caracter_dict.values():
                caracter.move()
                if DEBUG == True:
                    print("Est présent ", end='')
                    print(caracter)

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

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        #si le retourd en arrière est possible
        if len(player.history) == 1:
            command_word = list_of_words[0]
            print(MSG3.format(command_word=command_word))
        else:
            # Fait bouger les pnj
            for knownroom in game.rooms:
                for caracter in knownroom.inventory_caracter.caracter_dict.values():
                    caracter.move()
            # Retourd en arrière
            player.history.pop()
            player.current_room = player.history[-1]
            print(player.current_room.get_long_description())
            player.get_history()


    
    def look(game, list_of_words, number_of_parameters):
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player.current_room.inventory_caracter.get_inventory()


    def take(game, list_of_words, number_of_parameters):
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the object from the list of words.
        object = list_of_words[1]

        #Si la direction entrée n'est pas connue, affichage d'un message d'erreur
        if object not in player.current_room.inventory_caracter.inventory_dict.keys() :
            command_word = list_of_words[0]
            print(MSG2.format(command_word=command_word, entered_world=object), end='')
            return False
        
        # Attrape l'oject.
        player.inventory_caracter.inventory_dict[object] = player.current_room.inventory_caracter.inventory_dict.get(object)
        del player.current_room.inventory_caracter.inventory_dict[object]
        print("\nVous avez pris l'object {0}.\n".format(object))
        return True
    
    def drop(game, list_of_words, number_of_parameters):
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the object from the list of words.
        object = list_of_words[1]

        #Si la direction entrée n'est pas connue, affichage d'un message d'erreur
        if object not in player.inventory_caracter.inventory_dict.keys() :
            command_word = list_of_words[0]
            print(MSG2.format(command_word=command_word, entered_world=object), end='')
            return False
        
        # Attrape l'oject.
        player.current_room.inventory_caracter.inventory_dict[object] = player.inventory_caracter.inventory_dict.get(object)
        del player.inventory_caracter.inventory_dict[object]
        print("\nVous avez déposé l'object {0}.\n".format(object))
        return True


    def check(game, list_of_words, number_of_parameters):
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player.inventory_caracter.get_inventory()
        return True
    
    def talk (game, list_of_words, number_of_parameters):

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the pnj from the list of words.
        pnj = list_of_words[1]

        #
        if pnj not in player.current_room.inventory_caracter.caracter_dict.keys() :
            command_word = list_of_words[0]
            print(MSG2.format(command_word=command_word, entered_world=pnj), end='')
            print(player.current_room.get_long_description())
            return False
        #
        player.current_room.inventory_caracter.caracter_dict[pnj].get_msg()

        return True




