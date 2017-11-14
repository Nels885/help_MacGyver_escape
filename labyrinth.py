"""
***********************
    LABYRINTH CLASS
***********************
"""

from constants import *


class Labyrinth:
    """### Class of the labyrinth structure ###"""

    def __init__(self, log, file):
        """
        ## Initialize class Labyrinth ##
        Initialization of variables used by class Labyrinth
            :param log: logging module
            :param file: file of the labyrinth structure
        """
        self.structure_laby = []
        self.pos_mgyver = (0, 0)
        self.lg = log
        self.structure(file)

    def structure(self, file):
        """
        ## Load structure Labyrinth ##
        load the file representing the structure
        of the labyrinth
            :param file: structure file
            :return: add structure in the attribute structure_laby
        """
        err_structure = False
        with open(file, "r") as f:
            structure_laby = []
            # add line of the file to structure_laby list
            for line in f:
                line_laby = []
                # add sprite of the line to line_laby list
                for sprite in line:
                    if sprite != "\n":
                        if sprite == "M":
                            self.pos_mgyver = line.index(NAME_MGYVER), len(structure_laby)
                        line_laby.append(sprite)
                    elif len(line_laby) > NB_SPRITE:
                        err_structure = True
                structure_laby.append(line_laby)

        if err_structure or len(structure_laby) > NB_SPRITE:
            raise Warning("Fichier structure, {} sprites max par côté".format(str(NB_SPRITE)))
        else:
            self.structure_laby = structure_laby

    def add_sprite(self, position, sprite):
        """
        ## Add sprite on the Labyrinth ##
            :param position: position in the labyrinth
            :param sprite: letter of the sprite
            :return: add the sprite in the labyrinth
        """
        self.structure_laby[position[1]][position[0]] = sprite

    def move_sprite(self, position, sprite):
        """
        ## Move sprite on the Labyrinth ##
            :param position: position in the labyrinth
            :param sprite: letter of the sprite
            :return: changing the position of sprite
        """
        if position != self.pos_mgyver:
            self.structure_laby[self.pos_mgyver[1]][self.pos_mgyver[0]] = " "
            self.structure_laby[position[1]][position[0]] = sprite
            self.pos_mgyver = position
            for line in range(15):
                self.lg.debug(self.structure_laby[line])
