"""
********************
    OBJECT CLASS
********************
"""

import logging as log
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
        position = (0, 0)
        while loop:
            x_position = randint(2, 14)
            y_position = randint(2, 14)
            position = x_position, y_position
            if self.check_object(position):
                if structure[position[1]][position[0]] == " ":
                    loop = False
        self.pos_not_object.append(position)
        self.counter += 1
        return position

    def check_object(self, position):
        """
        ## Check if the object exists ##
            :param position: position to check
            :return: True or False
        """
        check = True
        for i in range(self.counter):
            if position == self.pos_not_object[i]:
                log.error("Erreur position d'objet: {}".format(position))
                check = False
        return check
