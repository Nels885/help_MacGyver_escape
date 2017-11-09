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

SIZE_SPRITE = 40
NB_SPRITE = 15
NB_OBJECTS = 3

# Class initializes
cha = character.Character()
lab = labyrinth.Labyrinth(cha.pos_mgyver)
obj = object.Object(cha.pos_mgyver)


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
        pos_mgyver = cha.pos_mgyver
        pos_needle = obj.random_position(lab.structure_laby)
        pos_tube = obj.random_position(lab.structure_laby)
        pos_ether = obj.random_position(lab.structure_laby)
        lab.add_sprite(pos_needle, "N")
        lab.add_sprite(pos_tube, "T")
        lab.add_sprite(pos_ether, "E")
        lab.add_sprite(pos_mgyver, cha.sprite_mgyver)

    def end_game(self, structure):
        """
        ## Check end game ##
        Check if you are at the exit of the
        labyrinth with the objects
            :param structure: attribute of labyrinth class
            :return: end game is True or False
        """
        if structure[cha.pos_mgyver[1]][cha.pos_mgyver[0]] == "F":
            if cha.objects == NB_OBJECTS:
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
                end = game.end_game(lab.structure_laby)

                # check position if wall or objects
                if not cha.check_position(lab.structure_laby):
                    log.info("Erreur de direction !!!")
                else:
                    lab.move_sprite(cha.pos_mgyver, cha.sprite_mgyver)
                    # display info messages or debug messages
                    log.info("Position MacGyver (x, y): {}, {}".format(int(cha.x_position), int(cha.y_position)))
                    log.info("Objets disponible: {}".format(int(cha.objects)))
                    for i in range(15):
                        log.debug(lab.structure_laby[i])

        # display of the Labyrinth
        lab.display(windows, SIZE_SPRITE)
        pygame.display.flip()
    game.end_screen()


if __name__ == "__main__":
    args = parse_arguments()
    if args.debug:
        log.basicConfig(level=log.DEBUG)
    elif args.verbose:
        log.basicConfig(level=log.INFO)
    try:
        laby_file = args.file
        game = Game(laby_file)

        # Pygame Initialize
        pygame.init()
        windows = pygame.display.set_mode((SIZE_SPRITE * NB_SPRITE, SIZE_SPRITE * NB_SPRITE))
        pygame.display.set_caption('Help MacGyver Escape')
        background = pygame.Surface(windows.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        main()
    # return an error when the name of file is incorrect
    except FileNotFoundError as err:
        log.error(err)


