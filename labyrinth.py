#!usr/bin/env python3

import json


def main():
    # load labyrinth file
    with open("laby_level1.json") as file:
        data = json.load(file)
        structure_laby = []
        # add line of the file to structure_laby list
        for line in data:
            line_laby = []
            # add sprite of the line to line_lady list
            for sprite in line:
                line_laby.append(sprite)
            structure_laby.append(line_laby)


    #print(structure_laby[0][0])
    print(structure_laby)

if __name__ == '__main__':
    main()
