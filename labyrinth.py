import character
import objects

ch = character.Character()
ob = objects.Objects()

class Labyrinth:
    """ Class of the labyrinth structure """


    def __init__(self):
        """ ## Initialize class Labyrinth ##
        Initialization of variables used by class Labyrinth
            - guardian sprite
            - list integrating the labyrinth structure
            - position of Macgyver"""
        self.sprite_guardian = "G"
        self.structure_laby = []
        self.pos_mgyver = ch.pos_mgyver


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


    def display(self, position):
        """ Labyrinth display in the console """
        # moving of MacGyver on the labyrinth
        self.structure_laby[self.pos_mgyver[1]][self.pos_mgyver[0]] = " "
        self.pos_mgyver = position
        self.structure_laby[self.pos_mgyver[1]][self.pos_mgyver[0]] = ch.sprite_mgyver

        # display of labyrinth with objects and guardian
        for y in range (0, 15):
            line_modif = ""
            line = self.structure_laby[y]

            for sprite in line:
                if sprite == "F":
                    sprite = self.sprite_guardian
                elif sprite == "1":
                    sprite = ob.sprite_needle
                elif sprite == "2":
                    sprite = ob.sprite_tube
                line_modif += sprite
            # print each line of the labyrinth
            print("      {}".format(line_modif))
