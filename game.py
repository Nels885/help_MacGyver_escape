#! /usr/bin/env python3
# coding: utf-8

import os
import labyrinth
import character
import objects
import logging as log
import argparse


lab = labyrinth.Labyrinth()
cha = character.Character()
obj = objects.Objects()


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

        # List of messages to display
        msg = ['Appuyer sur la touche entrée si vous voulez jouer ou sinon sur Q pour quitter\n',
                'Deplacer MacGyver: "d" pour droite, "q" pour gauche, "z" pour haut, "s" pour bas\n',
                'Erreur de direction !!!\n',
                'Vous avez GAGNé :D !!!\n',
                'Vous avez PERDU :( !!!\n']

        end = True
        message = msg[0]
        entry = None
        lab.structure(laby_file)
        structure_laby = lab.structure_laby
        pos_needle = obj.random_position(structure_laby)
        pos_tube = obj.random_position(structure_laby)
        structure_laby[pos_needle[1]][pos_needle[0]] = "1"
        structure_laby[pos_tube[1]][pos_tube[0]] = "2"

        while end == True:

            os.system("clear")
            print("###################################\n"\
                "## Aidez MacGyver à s'échapper ! ##\n"\
                "###################################\n")

            if not cha.check_position(entry, structure_laby):
                log.warning(msg[2])

            if not endgame(structure_laby):
                if cha.objects == 2:
                    end_msg = msg[3]
                else:
                    end_msg = msg[4]
                log.warning(end_msg)
                break


            # display of the Labyrinth in the console
            lab.display(cha.pos_mgyver)

            # display info messages or debug messages
            log.info("position X: {0}".format(int(cha.x_position)))
            log.info("position Y: {0}".format(int(cha.y_position)))
            log.info("Objets disponible: {0}".format(int(cha.objects)))
            log.debug(structure_laby)

            entry = input("\n{}".format(message))
            # if you press of Q key, you quit the game
            if entry == "Q":
                break
            # if press q or d or z or s, move MacGyver
            elif entry == "q" or entry == "d" or entry == "z" or entry == "s":
                cha.move(entry)
            message = msg[1]
    # return an error when the name of file is incorrect
    except FileNotFoundError as err:
        log.error(err)
    # return an error when the name of file is absent
    except Warning as err:
        log.warning(err)




if __name__ == "__main__":
    main()
