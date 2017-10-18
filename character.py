class Character:
    """ Class of the person to be evolved on the labyrinth """


    def __init__(self):
        """ Initialize class Character """
        self.sprite_mgyver = "M"
        self.pos_mgyver = self.x_position, self.y_position = (1, 1)
        self.objects = 0


    def move(self, direction):
        # if press d key, move to the right
        if direction == "d" and self.x_position < 14:
                self.x_position += 1
        # if press q key, move to the left
        elif direction == "q" and self.x_position > 0:
                self.x_position -= 1
        # if press z key, move to the up
        elif direction == "z" and self.y_position > 0:
                self.y_position -= 1
        # if press s key, move to the down
        elif direction == "s" and self.y_position < 14:
                self.y_position += 1
        self.pos_mgyver = (self.x_position, self.y_position)


    def check_position(self, direction, structure):
        # if a wall present, don't move MacGyver
        check = structure[self.pos_mgyver[1]][self.pos_mgyver[0]]
        if check != "0":
            if check == "1" or check == "2":
                self.objects += 1
            return True
        else:
            if direction == "d":
                self.x_position -= 1
            elif direction == "q":
                self.x_position += 1
            elif direction == "z":
                self.y_position += 1
            elif direction == "s":
                self.y_position -= 1
            self.pos_mgyver = (self.x_position, self.y_position)
            return False
