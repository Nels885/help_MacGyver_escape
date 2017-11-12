#! /usr/bin/env python3
# coding: utf-8
"""
****************************
    Help MacGyver Escape
****************************
"""

import logging as log
import argparse

import pygame
from pygame.locals import *

import labyrinth
import character
import object

# Constantes
SIZE_SPRITE = 40
NB_SPRITE = 15
NB_OBJECT = 3
NAME_OBJECT = ("N", "T", "E")
POS_MGYVER = (1, 1)
NAME_MGYVER = "M"

# Class initializes
cha = character.Character(NAME_OBJECT, POS_MGYVER)
lab = labyrinth.Labyrinth(POS_MGYVER)
obj = object.Object(cha.pos_mgyver)

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
DICT_SPRITES = {" ": sprite_ground, "0": sprite_wall, "F": sprite_guardian, NAME_MGYVER: sprite_mgyver,
                "N": sprite_needle, "T": sprite_tube, "E": sprite_ether}


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
        self.end_text = None
        lab.structure(file)
        for number in range(NB_OBJECT):
            pos_object = obj.random_position(lab.structure_laby)
            lab.add_sprite(pos_object, NAME_OBJECT[number])
        lab.add_sprite(POS_MGYVER, NAME_MGYVER)
        self.structure = lab.structure_laby

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
                for key in DICT_SPRITES.keys():
                    if value == key:
                        windows.blit(DICT_SPRITES[key], (SIZE_SPRITE * x, SIZE_SPRITE * y))
                line_modif += value
                x += 1

    def end_game(self):
        """
        ## Check end game ##
        Check if you are at the exit of the
        labyrinth with the objects
            :return: end game is True or False
        """
        if self.structure[cha.pos_mgyver[1]][cha.pos_mgyver[0]] == "F":
            if cha.objects == NB_OBJECT:
                self.end_text = self.WON_TEXT
            else:
                self.end_text = self.LOST_TEXT
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
        textpos.centerx = background.get_rect().centerx
        textpos.centery = background.get_rect().centery
        background.blit(text, textpos)
        windows.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)


def parse_arguments():
    """
    Arguments added to command line to get
    additional information
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="""Load labyrinth file.""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Display informations of MacGyver""")
    parser.add_argument("-d", "--debug", action='store_true', help="""Switch to debug mode!""")
    return parser.parse_args()


def main():
    """
    Main instruction for to run the game
    """
    args = parse_arguments()
    if args.debug:
        log.basicConfig(level=log.DEBUG)
    elif args.verbose:
        log.basicConfig(level=log.INFO)
    try:
        laby_file = args.file
        game = Game(laby_file)
        end = True
        while end:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.end_text = game.QUIT_TEXT
                    end = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        cha.move("up")
                    if event.key == K_DOWN:
                        cha.move("down")
                    if event.key == K_LEFT:
                        cha.move("left")
                    if event.key == K_RIGHT:
                        cha.move("right")
                    end = game.end_game()

                    # check position if wall or objects
                    if not cha.check_position(lab.structure_laby):
                        log.info("Erreur de direction !!!")
                    else:
                        lab.move_sprite(cha.pos_mgyver, NAME_MGYVER)
                        # display info messages or debug messages
                        log.info("Position MacGyver (x, y): {}, {}".format(int(cha.x_position), int(cha.y_position)))
                        log.info("Objets disponible: {}".format(int(cha.objects)))
                        for i in range(15):
                            log.debug(lab.structure_laby[i])

            # display of the Labyrinth
            game.display()
            pygame.display.flip()
        game.end_screen()

    # return an error when the name of file is incorrect
    except FileNotFoundError as err:
        log.error(err)


if __name__ == "__main__":
    main()



