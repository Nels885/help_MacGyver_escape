"""
******************
    GAME CLASS
******************
"""

import logging as log

import pygame
from pygame.locals import *

import labyrinth
import character
import object
from constants import *


def ini_pygame():
    """
    ## Initialize module pygame for the game ##
    :return: windows, background and dict_sprites
    """
    # Pygame Initialize
    pygame.init()
    windows = pygame.display.set_mode((SIZE_SPRITE * NB_SPRITE, SIZE_SPRITE * NB_SPRITE))
    pygame.display.set_caption('Help MacGyver Escape')
    background = pygame.Surface(windows.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Sprites of labyrinth
    sprite_wall = pygame.image.load("pictures/wall.png").convert()
    sprite_ground = pygame.image.load("pictures/ground.png").convert()

    # Sprite of objects
    sprite_needle = pygame.image.load("pictures/needle.png").convert_alpha()
    sprite_tube = pygame.image.load("pictures/tube.png").convert_alpha()
    sprite_ether = pygame.image.load("pictures/ether.png").convert_alpha()

    # Sprite of characters
    sprite_guardian = pygame.image.load("pictures/murdoc.png").convert_alpha()
    sprite_mgyver = pygame.image.load("pictures/macgyver.png").convert_alpha()

    # Dictionary of sprites
    dict_sprites = {NAME_GROUND: sprite_ground, NAME_WALL: sprite_wall, NAME_GUARDIAN: sprite_guardian,
                    NAME_MGYVER: sprite_mgyver, NAME_OBJECT[0]: sprite_needle, NAME_OBJECT[1]: sprite_tube,
                    NAME_OBJECT[2]: sprite_ether}
    return windows, background, dict_sprites


class Game:
    """### Game class ###"""
    # List of messages to display
    WON_TEXT = "Vous avez GAGNé  :D !!!"
    LOST_TEXT = "Vous avez PERDU :( !!!"
    QUIT_TEXT = "Vous avez quitté le jeu"

    def __init__(self, file):
        """
        ## Initialize Labyrinth and sprite ##
            :param file: structure file
        """
        self.quit = False
        self.end_text = None
        self.windows, self.background, self.dict_sprites = ini_pygame()
        lab = labyrinth.Labyrinth(log, file)
        cha = character.Character(log, lab.pos_mgyver)
        obj = object.Object(log, lab.pos_mgyver)
        for number in range(NB_OBJECT):
            pos_object = obj.random_position(lab.structure_laby)
            lab.add_sprite(pos_object, NAME_OBJECT[number])
        lab.add_sprite(lab.pos_mgyver, NAME_MGYVER)
        self.structure = lab.structure_laby
        self.lab = lab
        self.cha = cha

    def check_keys(self):
        """
        ## checking keydown ##
            :return: New position of MacGyver
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.cha.move("up")
                if event.key == K_DOWN:
                    self.cha.move("down")
                if event.key == K_LEFT:
                    self.cha.move("left")
                if event.key == K_RIGHT:
                    self.cha.move("right")
                self.cha.check_position(self.lab.structure_laby)
        self.lab.move_sprite(self.cha.pos_mgyver, NAME_MGYVER)

    def display(self):
        """
        ## Load all sprites of the game ##
            :return: add all sprites to the window of pygame
        """
        for y in range(NB_SPRITE):
            x = 0
            line_modif = ""
            line = self.structure[y]
            for value in line:
                for key in self.dict_sprites.keys():
                    if value == key:
                        self.windows.blit(self.dict_sprites[key], (SIZE_SPRITE * x, SIZE_SPRITE * y))
                line_modif += value
                x += 1
        pygame.display.flip()

    def end_game(self):
        """
        ## Check end game ##
        Check if you are at the exit of the
        labyrinth with the objects
            :return: end game is True or False
        """
        if self.cha.pos_guardian:
            if self.cha.objects == NB_OBJECT:
                self.end_text = self.WON_TEXT
            else:
                self.end_text = self.LOST_TEXT
            endgame = False
        elif self.quit:
            self.end_text = self.QUIT_TEXT
            endgame = False
        else:
            endgame = True
        return endgame

    def end_screen(self):
        """
        ## Displays the end message ##
            :return: screen of endgame
        """
        font = pygame.font.Font(None, 36)
        text = font.render(self.end_text, 1, (250, 250, 250))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().centery
        self.background.blit(text, textpos)
        self.windows.blit(self.background, (0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)
