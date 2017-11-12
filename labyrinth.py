"""
***********************
    LABYRINTH CLASS
***********************
"""


class Labyrinth:
    """### Class of the labyrinth structure ###"""

    def __init__(self, log, pos_init, max_sprites):
        """
        ## Initialize class Labyrinth ##
        Initialization of variables used by class Labyrinth
            :param log: logging module
            :param pos_init: initial position of MacGyver
            :param max_sprites: max sprites per side of labyrinth structure
        """
        self.max_sprites = max_sprites
        self.lg = log
        self.structure_laby = []
        self.pos_init = pos_init

    def structure(self, file):
        """
        ## Load structure Labyrinth ##
        load the file representing the structure
        of the labyrinth
            :param file: structure file
            :return: add structure in the attribute structure_laby
        """
        max_sprites = self.max_sprites
        err_structure = False
        with open(file, "r") as f:
            structure_laby = []
            # add line of the file to structure_laby list
            for line in f:
                line_laby = []
                # add sprite of the line to line_laby list
                for sprite in line:
                    if sprite != "\n":
                        line_laby.append(sprite)
                    elif len(line_laby) > max_sprites:
                        err_structure = True
                structure_laby.append(line_laby)

        if err_structure or len(structure_laby) > max_sprites:
            raise Warning("Fichier structure, {} sprites max par côté".format(str(max_sprites)))
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
        if position != self.pos_init:
            self.structure_laby[self.pos_init[1]][self.pos_init[0]] = " "
            self.structure_laby[position[1]][position[0]] = sprite
            self.pos_init = position
            for line in range(15):
                self.lg.debug(self.structure_laby[line])
