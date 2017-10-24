#! /usr/bin/env python3
# coding: utf-8

import os
import time
import labyrinth
import character
import objects
import logging as log
import argparse
import pygame
from pygame.locals import *

cha = character.Character()
lab = labyrinth.Labyrinth(cha.pos_mgyver)
obj = objects.Objects()
pygame.init()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="""Load labyrinth file.""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Display informations of MacGyver""")
    parser.add_argument("-d", "--debug", action='store_true', help="""Switch to debug mode!""")
    return parser.parse_args()

def endgame(structure):
    if structure[cha.pos_mgyver[1]][cha.pos_mgyver[0]] == "F":
        end_game = False
    else:
        end_game = True
    return end_game

def display(structure):
    for y in range (0, 15):
        line_modif = ""
        line = structure[y]
        for value in line:
            if value == "F":
                value = cha.sprite_guardian
            elif value == "1":
                value = obj.sprite_needle
            elif value == "2":
                value = obj.sprite_tube
            line_modif += value
        # print each line of the labyrinth
        print("      {}".format(line_modif))

def main():

    windows = pygame.display.set_mode((30 * (14 + 1), 30 * (14 + 1)))

    #icone = pygame.image.load("")

    args = parse_arguments()
    if args.debug:
        log.basicConfig(level=log.DEBUG)
    elif args.verbose:
        log.basicConfig(level=log.INFO)

    try:
        laby_file = args.file
        if laby_file == None:
            raise Warning("You must indicate a labyrinth file!")

        # List of messages to display
        msg = ['Appuyer sur la touche entrée si vous voulez jouer ou sinon sur Q pour quitter\n',
                'Deplacer MacGyver: "d" pour droite, "q" pour gauche, "z" pour haut, "s" pour bas\n',
                'Erreur de direction !!!\n',
                'Vous avez GAGNé :D !!!\n',
                'Vous avez PERDU :( !!!\n']

        # Initialize Labyrinth and sprite
        end = True
        message = msg[0]
        entry = None
        lab.structure(laby_file)
        pos_mgyver = cha.pos_mgyver
        pos_needle = obj.random_position(lab.structure_laby)
        pos_tube = obj.random_position(lab.structure_laby)
        lab.add_sprite(pos_needle, "1")
        lab.add_sprite(pos_tube, "2")
        lab.add_sprite(pos_mgyver, cha.sprite_mgyver)

        while end:

            time.sleep(.3)
            #os.system("clear")
            # print("###################################\n"\
            #     "## Aidez MacGyver à s'échapper ! ##\n"\
            #     "###################################\n")





            # entry = input("\n{}".format(message))
            # # if you press of Q key, you quit the game
            # if entry == "Q":
            #     break
            # # if press q or d or z or s, move MacGyver
            # elif entry == "q" or entry == "d" or entry == "z" or entry == "s":

            #message = msg[1]

            for event in pygame.event.get():
                if event.type == QUIT:
                    end = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        entry = "z"
                    if event.key == K_DOWN:
                        log.info("touche DOWN")
                        entry = "s"
                    if event.key == K_LEFT:
                        log.info("touche LEFT")
                        entry = "q"
                    if event.key == K_RIGHT:
                        log.info("touche RIGHT")
                        entry = "d"

                structure_laby = lab.structure_laby

                # display info messages or debug messages
                log.info("position X: {0}".format(int(cha.x_position)))
                log.info("position Y: {0}".format(int(cha.y_position)))
                log.info("Objets disponible: {0}".format(int(cha.objects)))
                log.debug(structure_laby)
                cha.move(entry)

                # check position if wall or objects
                if not cha.check_position(entry, structure_laby):
                    log.warning(msg[2])
                else:
                    lab.move_sprite(cha.pos_mgyver, cha.sprite_mgyver)

                if not endgame(structure_laby):
                    if cha.objects == 2:
                        end_msg = msg[3]
                    else:
                        end_msg = msg[4]
                    log.warning(end_msg)
                    end = False

                # display of the Labyrinth in the console
                display(structure_laby)



    # return an error when the name of file is incorrect
    except FileNotFoundError as err:
        log.error(err)
    # return an error when the name of file is absent
    except Warning as err:
        log.warning(err)




if __name__ == "__main__":
    main()
