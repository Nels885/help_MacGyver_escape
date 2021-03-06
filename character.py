"""
***********************
    CHARACTER CLASS
***********************
"""

from constants import *


class Character:
    """### Class of the person to be evolved on the labyrinth ###"""

    def __init__(self, log, pos_mgyver):
        """
        ## Initialize class Character ##
            :param log: logging module
            :param pos_mgyver: Initial position of MacGyver
        """
        self.lg = log
        self.direction = None
        self.names = "".join(NAME_OBJECT)
        self.pos_mgyver = self.x_position, self.y_position = pos_mgyver
        self.pos_guardian = False
        self.objects = 0

    def move(self, direction):
        """
        ## Moving the character ##
            :param direction: direction that the player has chosen
            :return: new character position
        """
        self.direction = direction
        # if press right key, move to the right
        if self.direction == "right" and self.x_position < 14:
                self.x_position += 1
        # if press left key, move to the left
        elif self.direction == "left" and self.x_position > 0:
                self.x_position -= 1
        # if press up key, move to the up
        elif self.direction == "up" and self.y_position > 0:
                self.y_position -= 1
        # if press down key, move to the down
        elif self.direction == "down" and self.y_position < 14:
                self.y_position += 1
        self.pos_mgyver = (self.x_position, self.y_position)

    def check_position(self, structure):
        """
        ## Check position of character ##
        if a wall present, don't move MacGyver
            :param structure: attribute of labyrinth class
            :return: True or False if a wall present
        """
        check = structure[self.pos_mgyver[1]][self.pos_mgyver[0]]
        if check != NAME_WALL:
            if check in self.names:
                self.objects += 1
            elif check == NAME_GUARDIAN:
                self.pos_guardian = True
            # display info messages or debug messages
            self.lg.info("Position MacGyver (x, y): {}, {}".format(int(self.x_position), int(self.y_position)))
            self.lg.info("Objets disponible: {}".format(int(self.objects)))
            return True
        else:
            if self.direction == "right":
                self.x_position -= 1
            elif self.direction == "left":
                self.x_position += 1
            elif self.direction == "up":
                self.y_position += 1
            elif self.direction == "down":
                self.y_position -= 1
            self.pos_mgyver = (self.x_position, self.y_position)
            self.lg.info("Erreur de direction !!!")
            return False
