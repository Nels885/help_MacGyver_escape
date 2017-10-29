#! /usr/bin/env python3
# coding: utf-8

import os
import logging as log
import argparse

import pygame
from pygame.locals import *

import labyrinth
import character
import objects

size_sprite = 40
nb_sprite = 15

# List of messages to display
wontext = "Vous avez GAGNé  :D !!!"
losttext = "Vous avez PERDU :( !!!"

# Class initializes
cha = character.Character()
lab = labyrinth.Labyrinth(cha.pos_mgyver)
obj = objects.Objects()

# Pygame Initialize
pygame.init()

windows = pygame.display.set_mode((size_sprite * nb_sprite, size_sprite * nb_sprite))
pygame.display.set_caption('Help MacGyver Escape')

background = pygame.Surface(windows.get_size())
background = background.convert()
background.fill((0, 0, 0))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="""Load labyrinth file.""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Display informations of MacGyver""")
    parser.add_argument("-d", "--debug", action='store_true', help="""Switch to debug mode!""")
    return parser.parse_args()


def endgame(structure):
    if structure[cha.pos_mgyver[1]][cha.pos_mgyver[0]] == "F":
        end_game = False
    else:
        end_game = True
    return end_game


def main():

    args = parse_arguments()
    if args.debug:
        log.basicConfig(level=log.DEBUG)
    elif args.verbose:
        log.basicConfig(level=log.INFO)

    try:
        laby_file = args.file
        if laby_file == None:
            raise Warning("You must indicate a labyrinth file!")

        # Initialize Labyrinth and sprite
        end = True
        entry = None
        lab.structure(laby_file)
        pos_mgyver = cha.pos_mgyver
        pos_needle = obj.random_position(lab.structure_laby)
        pos_tube = obj.random_position(lab.structure_laby)
        lab.add_sprite(pos_needle, "1")
        lab.add_sprite(pos_tube, "2")
        lab.add_sprite(pos_mgyver, cha.sprite_mgyver)

        while end:

            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endtext = "Vous avez quitté le jeu"
                    end = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        cha.move("z")
                    if event.key == K_DOWN:
                        cha.move("s")
                    if event.key == K_LEFT:
                        cha.move("q")
                    if event.key == K_RIGHT:
                        cha.move("d")

                    if not endgame(lab.structure_laby):
                        if cha.objects == 2:
                            endtext = wontext
                        else:
                            endtext = losttext
                        end = False

                    # check position if wall or objects
                    if not cha.check_position(lab.structure_laby):
                        log.info("Erreur de direction !!!")
                        pygame.time.delay(200)
                    else:
                        lab.move_sprite(cha.pos_mgyver, cha.sprite_mgyver)

                # display of the Labyrinth in the console
                lab.display(windows, size_sprite)
                pygame.display.flip()

                # display info messages or debug messages
                log.info("position X: {0}".format(int(cha.x_position)))
                log.info("position Y: {0}".format(int(cha.y_position)))
                log.info("Objets disponible: {0}".format(int(cha.objects)))
                log.debug(lab.structure_laby)

        font = pygame.font.Font(None, 36)
        text = font.render(endtext, 1, (250, 250, 250))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        textpos.centery = background.get_rect().centery
        background.blit(text, textpos)

        windows.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)

    # return an error when the name of file is incorrect
    except FileNotFoundError as err:
        log.error(err)
    # return an error when the name of file is absent
    except Warning as err:
        log.warning(err)



if __name__ == "__main__":
    main()
