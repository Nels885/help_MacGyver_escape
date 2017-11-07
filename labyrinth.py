import pygame

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

    def display(self, windows, size_sprite):
        """
        ## Load all sprites of the game ##
            :param windows: windows created by pygame
            :param size_sprite: size des sprites
            :return: add all sprites to the windows of pygame
        """
        sprite_wall = pygame.image.load("pictures/wall.png").convert()
        sprite_ground = pygame.image.load("pictures/ground.png").convert()
        sprite_needle = pygame.image.load("pictures/needle.png").convert_alpha()
        sprite_tube = pygame.image.load("pictures/tube.png").convert_alpha()
        sprite_ether = pygame.image.load("pictures/ether.png").convert_alpha()
        sprite_guardian = pygame.image.load("pictures/murdoc-32.png").convert_alpha()
        sprite_mgyver = pygame.image.load("pictures/macgyver-32-43.png").convert_alpha()

        for y in range (15):
            x = 0
            line_modif = ""
            line = self.structure_laby[y]
            for value in line:
                if value == " ":
                    windows.blit(sprite_ground, (size_sprite * x, size_sprite * y))
                if value == "0":
                    windows.blit(sprite_wall, (size_sprite * x, size_sprite * y))
                elif value == "F":
                    windows.blit(sprite_guardian, (size_sprite * x, size_sprite * y))
                elif value == "M":
                    windows.blit(sprite_mgyver, (size_sprite * x, size_sprite * y))
                elif value == "N":
                    windows.blit(sprite_needle, (size_sprite * x, size_sprite * y))
                elif value == "T":
                    windows.blit(sprite_tube, (size_sprite * x, size_sprite * y))
                elif value == "E":
                    windows.blit(sprite_ether, (size_sprite * x, size_sprite * y))
                line_modif += value
                x += 1
