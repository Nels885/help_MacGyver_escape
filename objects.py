from random import randrange

class Objects:
	""" Class Objects to pick up """


	def __init__(self):
		""" Initialize Class Objects """
		self.sprite_needle = "I"
		self.sprite_tube = "T"


	def random_position(self, structure):
		""" Creation of the random position of an object """

		while True:
			x_position = randrange(15)
			y_position = randrange(15)
			if structure[y_position][x_position] != "0":
				break
		return (x_position, y_position)
