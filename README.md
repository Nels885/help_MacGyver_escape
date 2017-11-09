# help_MacGyver_escape

You have to get MacGyver out of the labyrinth.
You must collect three items that are a small tube,
a needle and ether that will allow MacGyver to lull
the guard who is at the exit.

![Screenshot](https://github.com/Nels885/help_MacGyver_escape/tree/master/pictures/game_screenshot.png)

## dependencies:
- [Python 3.x](https://www.python.org) is required.
- [Pygame](http://www.pygame.org/news)

## Installation:

#### Linux Ubuntu/Debian:

Enter the following commands in the terminal. 

    $ sudo apt-get update
    $ sudo apt-get install python3-pip

    $ git clone https://github.com/Nels885/help_MacGyver_escape.git
    $ cd help_MacGyver_escape
    $ sudo pip3 install -r requirements.txt
    
#### Windows:

- Download the last version of [Python 3 for Windows](https://www.python.org/downloads/windows/).
Make sure you tick the Add Python to PATH checkbox on first page in Python installer.
- In the terminal:

    ```$ pip install -r requirements.txt```

#### Mac:

- Download the last version of [Python 3 for Mac](https://www.python.org/downloads/mac-osx/).
- In the terminal:

    ```$ pip3 install -r requirements.txt```

## Starting the game:
For basic usage, the script need a text file where 
the labyrinth structure will be saved (see laby.txt file).

    Example:
    $ python3 game.py laby.txt
    
Run program with -h or --help for explanations of options.