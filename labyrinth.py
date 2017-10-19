class Labyrinth:
    """ Class of the labyrinth structure """


    def __init__(self,pos_init):
        """ ## Initialize class Labyrinth ##
        Initialization of variables used by class Labyrinth
            - guardian sprite
            - list integrating the labyrinth structure
            - position of Macgyver"""
        self.structure_laby = []
        self.pos_init = pos_init


    def structure(self, file):
        """ Load structure Labyrinth """

        with open(file, "r") as f:
            structure_laby = []
            # add line of the file to structure_laby list
            for line in f:
                line_laby = []
                # add sprite of the line to line_laby list
                for sprite in line:
                    #print(sprite)
                    if sprite != "\n":
                        line_laby.append(sprite)
                        #print(line_laby)
                structure_laby.append(line_laby)
                #print(structure_laby)
        self.structure_laby = structure_laby


    def add_sprite(self, position, sprite):
        """ Add sprite on the Labyrinth """
        self.structure_laby[position[1]][position[0]] = sprite


    def move_sprite(self, position, sprite):
        """ Move sprite on the Labyrinth """
        self.structure_laby[self.pos_init[1]][self.pos_init[0]] = " "
        self.structure_laby[position[1]][position[0]] = sprite
        self.pos_init = position
