class Labyrinth:
    """ Class of the labyrinth structure """

    def __init__(self, file):
        """ Initialize class Labyrinth """
        self.file = file
        self.sprite_mgyver = "M"
        self.sprite_guardian = "G"

    def structure(self):
        """ Load structure Labyrinth """
        with open(self.file, "r") as file:
            structure_laby = []
            # add line of the file to structure_laby list
            for line in file:
                line_laby = []
                # add sprite of the line to line_laby list
                for sprite in line.strip():
                    #print(sprite)
                    line_laby.append(sprite)
                    #print(line_laby)
                structure_laby.append(line_laby)
                #print(structure_laby
        return structure_laby

    def display(self, x_position, y_position):
        """ Labyrinth display in the console """
        border = "    ================="
        print("\n" + border)
        for i in range (0, 15):
            ligne = self.structure()[i]
            # moving of MacGyver on the labyrinth
            if i == y_position:
                ligne[x_position] = self.sprite_mgyver
            # formatting of the character string for each line of the labyrinth
            ligne_modif = "".join(ligne).replace("0"," ").replace("1","0").replace("f",self.sprite_guardian)
            # print each line of the labyrinth
            print("    |{}|".format(ligne_modif))
        print(border + "\n")
