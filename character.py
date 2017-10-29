class Character:
    """ Class of the person to be evolved on the labyrinth """


    def __init__(self):
        """ Initialize class Character """
        self.sprite_guardian = "G"
        self.sprite_mgyver = "M"
        self.pos_mgyver = self.x_position, self.y_position = (1, 1)
        self.objects = 0


    def move(self, direction):
        self.direction = direction
        # if press d key, move to the right
        if self.direction == "d" and self.x_position < 14:
                self.x_position += 1
        # if press q key, move to the left
        elif self.direction == "q" and self.x_position > 0:
                self.x_position -= 1
        # if press z key, move to the up
        elif self.direction == "z" and self.y_position > 0:
                self.y_position -= 1
        # if press s key, move to the down
        elif self.direction == "s" and self.y_position < 14:
                self.y_position += 1
        self.pos_mgyver = (self.x_position, self.y_position)


    def check_position(self, structure):
        # if a wall present, don't move MacGyver
        check = structure[self.pos_mgyver[1]][self.pos_mgyver[0]]
        if check != "0":
            if check == "1" or check == "2":
                self.objects += 1
            return True
        else:
            if self.direction == "d":
                self.x_position -= 1
            elif self.direction == "q":
                self.x_position += 1
            elif self.direction == "z":
                self.y_position += 1
            elif self.direction == "s":
                self.y_position -= 1
            self.pos_mgyver = (self.x_position, self.y_position)
            return False
