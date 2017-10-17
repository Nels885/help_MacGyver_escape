import labyrinth

lab = labyrinth.Labyrinth("laby.txt")

class Character:
    """ Class of the person to be evolved on the labyrinth """

    def __init__(self):
        """ Initialize class Character """
        self.x_position = 0
        self.y_position = 0
        self.x_pos_mgyver = y_pos_mgyver= 0
        self.x_pos_guardian = self.y_pos_guardian = 14

    def move(self, direction):
        # if press d key, move to the right
        if direction == "d" and self.x_position < 14:
            # if a wall present, don't move MacGyver
            if lab.structure()[self.y_position][self.x_position + 1] != "1":
                self.x_position += 1
        # if press q key, move to the left
        elif direction == "q" and self.x_position > 0:
            # if a wall present, don't move MacGyver
            if lab.structure()[self.y_position][self.x_position - 1] != "1":
                self.x_position -= 1
        # if press z key, move to the up
        elif direction == "z" and self.y_position > 0:
            # if a wall present, don't move MacGyver
            if lab.structure()[self.y_position - 1][self.x_position] != "1":
                self.y_position -= 1
        # if press s key, move to the down
        elif direction == "s" and self.y_position < 14:
            # if a wall present, don't move MacGyver
            if lab.structure()[self.y_position + 1][self.x_position] != "1":
                self.y_position += 1
