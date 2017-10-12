#!usr/bin/env python3

import os

class Labyrinth:
    """ Class of the labyrinth structure """

    def __init__(self, file):
        """ Initialize class Labyrinth """
        self.file = file
        self.sprite_mgyver = "M"
        self.sprite_guardian = "G"

    @property
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
                #print(structure_laby)
        return structure_laby

    def display(self, x_position, y_position):
        """ Labyrinth display in the console """
        self.x_position = x_position
        self.y_position = y_position
        border = "    ================="
        print("\n" + border)
        for i in range (0, 15):
            ligne = self.structure[i]
            # moving of MacGyver on the labyrinth
            if i == self.y_position:
                ligne[x_position] = self.sprite_mgyver
            # formatting of the character string for each line of the labyrinth
            ligne_modif = "".join(ligne).replace("0"," ").replace("1","0").replace("f",self.sprite_guardian)
            # print each line of the labyrinth
            print("    |{}|".format(ligne_modif))
        print(border + "\n")


class Character:
    """ Class of the person to be evolved on the labyrinth """

    def __init__(self, x_position, y_position):
        """ Initialize class Character """
        self.x_position = x_position
        self.y_position = y_position
        self.x_pos_mgyver = y_pos_mgyver= 0
        self.x_pos_guardian = self.y_pos_guardian = 14

    def move(self, direction):
        pass


class Objects:

    def __init__(self):
        pass

    def position(self):
        pass



def main():

    os.system("clear")
    x_position = y_position = 0
    print("###################################\n"\
          "## Aidez MacGyver à s'échapper ! ##\n"\
          "###################################\n")

    msg = ['Appuyer sur la touche entrée si vous voulez jouer ou sinon sur Q pour quitter\n',
           'Deplacer MacGyver: "d" pour droite, "q" pour gauche, "z" pour haut, "s" pour bas\n',
           'Erreur de direction, vous sortez du cadre\n']

    labyrinth = Labyrinth("laby.txt")
    message = msg[0]
    while True:
        print("position X: ",int(x_position))
        print("position Y: ",int(y_position))
        entry = input(message)
        # if you press of Q key, tou quit the game
        if entry == "Q":
            break
        # if press q or d or z or s, move MacGyver
        elif entry == "q" or entry == "d" or entry == "z" or entry == "s":
            message = msg[1]
            if entry == "d" and x_position < 14:
                # if a wall present, don't move MacGyver
                if labyrinth.structure[y_position][x_position + 1] != "1":
                    x_position += 1
            elif entry == "q" and x_position > 0:
                if labyrinth.structure[y_position][x_position - 1] != "1":
                    x_position -= 1
            elif entry == "z" and y_position > 0:
                if labyrinth.structure[y_position - 1][x_position] != "1":
                    y_position -= 1
            elif entry == "s" and y_position < 14:
                if labyrinth.structure[y_position + 1][x_position] != "1":
                    y_position += 1
            else:
                message = msg[2] + msg[1]
        else:
            message = msg[1]

        labyrinth.display(x_position, y_position)


if __name__ == '__main__':
    main()
