import logging as lg
from random import randint


class Object:
    """### Class Object to pick up ###"""

    def __init__(self, pos_mgyver):
        """
        ## Initialize Class Object ##
        :param pos_mgyver: position of MacGyver on the labyrinth
        """
        self.pos_not_object = [pos_mgyver]
        self.counter = 1

    def random_position(self, structure):
        """
        ## Creation of the random position of an object ##
            :param structure: attribute of labyrinth class
            :return: random position of an object
        """
        loop = True
        while loop:
            x_position = randint(2, 14)
            y_position = randint(2, 14)
            position = x_position, y_position
            for i in range(self.counter):
                if position == self.pos_not_object[0]:
                    lg.error("Erreur position: {}".format(position))
                    break
                elif structure[position[1]][position[0]] == " ":
                    loop = False
        self.pos_not_object.append(position)
        self.counter += 1
        return position