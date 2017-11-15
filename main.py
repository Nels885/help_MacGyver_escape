#! /usr/bin/env python3
# coding: utf-8
"""
****************************
    Help MacGyver Escape
****************************
"""

import logging as log
import argparse

import game


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
        gam = game.Game(laby_file)
        end = True
        while end:

            # check
            gam.check_keys()

            # Display of the Labyrinth
            gam.display()

            # Check if it's the endgame
            end = gam.end_game()

        gam.end_screen()

    # return an error when the name of file is incorrect
    except Warning as err:
        log.error(err)
    except FileNotFoundError as err:
        log.error(err)


if __name__ == "__main__":
    main()



