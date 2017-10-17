#! /usr/bin/env python3
# coding: utf-8

import os
import labyrinth
import character
import objects

labyrinth = labyrinth.Labyrinth("laby.txt")
character = character.Character()

def main():

    os.system("clear")
    print("###################################\n"\
          "## Aidez MacGyver à s'échapper ! ##\n"\
          "###################################\n")

    msg = ['Appuyer sur la touche entrée si vous voulez jouer ou sinon sur Q pour quitter\n',
           'Deplacer MacGyver: "d" pour droite, "q" pour gauche, "z" pour haut, "s" pour bas\n']

    message = msg[0]
    while True:
        print("position X: ",int(character.x_position))
        print("position Y: ",int(character.y_position))
        entry = input(message)
        # if you press of Q key, tou quit the game
        if entry == "Q":
            break
        # if press q or d or z or s, move MacGyver
        elif entry == "q" or entry == "d" or entry == "z" or entry == "s":
            message = msg[1]
            character.move(entry)
        else:
            message = msg[1]

        labyrinth.display(character.x_position, character.y_position)


if __name__ == "__main__":
    main()
