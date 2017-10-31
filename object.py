from random import randint


class Object:
    """ Class Object to pick up"""

    def __init__(self):
        """ Initialize Class Object"""
        self.pos_init_object = (0, 0)

    def random_position(self, structure):
        """ Creation of the random position of an object """
        while True:
            x_position = randint(2, 14)
            y_position = randint(2, 14)
            position = x_position, y_position
            if position == self.pos_init_object:
                continue
            elif structure[position[1]][position[0]] == " ":
                break
        self.pos_init_object = position
        return position