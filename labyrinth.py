"""
***********************
    LABYRINTH CLASS
***********************
"""


class Labyrinth:
    """### Class of the labyrinth structure ###"""

    def __init__(self, pos_init):
        """
        ## Initialize class Labyrinth ##
        Initialization of variables used by class Labyrinth
            :param pos_init: initial position of MacGyver
        """
        self.structure_laby = []
        self.pos_init = pos_init
        self.max_x = self.max_y = 0

    def structure(self, file):
        """
        ## Load structure Labyrinth ##
        load the file representing the structure
        of the labyrinth
            :param file: structure file
            :return: add structure in the attribute structure_laby
        """
        max_x, max_y = self.max_x, self.max_y
        with open(file, "r") as f:
            structure_laby = []
            # add line of the file to structure_laby list
            for line in f:
                line_laby = []
                # add sprite of the line to line_laby list
                for sprite in line:
                    if sprite != "\n":
                        line_laby.append(sprite)
                    max_x += 1
                structure_laby.append(line_laby)
                max_y += 1
        self.max_x, self.max_y = max_x, max_y
        self.structure_laby = structure_laby

    def add_sprite(self, position, sprite):
        """
        ## Add sprite on the Labyrinth ##
            :param position: position in the labyrinth
            :param sprite: picture of the sprite
            :return: add the sprite in the labyrinth
        """
        self.structure_laby[position[1]][position[0]] = sprite

    def move_sprite(self, position, sprite):
        """
        ## Move sprite on the Labyrinth ##
            :param position: position in the labyrinth
            :param sprite: picture of the sprite
            :return: changing the position of sprite
        """
        self.structure_laby[self.pos_init[1]][self.pos_init[0]] = " "
        self.structure_laby[position[1]][position[0]] = sprite
        self.pos_init = position
